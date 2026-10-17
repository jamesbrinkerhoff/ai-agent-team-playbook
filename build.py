"""Build the static site in ./site from the Markdown files. Run: python build.py"""
import json, re, pathlib, datetime, shutil
import markdown

BASE = "https://jamesbrinkerhoff.github.io/ai-agent-team-playbook/"
ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "site"
AUTHORS = [{"@type": "Person", "name": "James Brinkerhoff"}, {"@type": "Person", "name": "Sonia Gomez"}]
ORG = {"@type": "Organization", "name": "Authority Brand Builder", "url": "https://authoritybrandbuilder.com"}
TODAY = datetime.date.today().isoformat()

PAGES = [("README.md", "index.html")] + [(f"docs/{p.name}", p.stem + ".html") for p in sorted((ROOT / "docs").glob("*.md"))] + \
        [(f"templates/{p.name}", "template-" + p.stem.lower() + ".html") for p in sorted((ROOT / "templates").glob("*.md"))]
LINKMAP = {}
for src, out in PAGES:
    LINKMAP[src] = out
    LINKMAP[src.split("/")[-1]] = out
    LINKMAP["../" + src] = out

def fix_links(html):
    def rep(m):
        href = m.group(1)
        if href.startswith("http"):
            return m.group(0)
        key = href.lstrip("./")
        for k in (href, key, "../" + key, key.split("/")[-1]):
            if k in LINKMAP:
                return f'href="{LINKMAP[k]}"'
        if href.rstrip("/").endswith("templates"):
            return 'href="template-role.html"'
        if href == "llms.txt":
            return 'href="llms.txt"'
        return m.group(0)
    return re.sub(r'href="([^"]+)"', rep, html)

CSS = "body{font-family:system-ui,-apple-system,Segoe UI,sans-serif;max-width:46rem;margin:2rem auto;padding:0 1rem;line-height:1.6;color:#1A1F36;background:#F7F6F2}a{color:#b5461a}pre,code{background:#ecebe6;border-radius:4px}pre{padding:1rem;overflow:auto}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:.4rem .6rem;text-align:left}nav a{margin-right:.8rem}footer{margin-top:3rem;font-size:.9rem;color:#555}"
NAV = " ".join(f'<a href="{o}">{n}</a>' for n, o in [("Home","index.html"),("Roles","roles.html"),("Routing","routing.html"),("Docs standard","documentation-standard.html"),("Handoffs","handoffs.html"),("Approvals","approval-gates.html"),("Models","model-routing.html"),("Lessons","lessons-learned.html"),("FAQ","faq.html"),("Templates","template-role.html")])

def faq_schema(md_text):
    items = []
    for block in re.split(r"\n## ", md_text)[1:]:
        q, _, a = block.partition("\n")
        a = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", a).strip()
        items.append({"@type": "Question", "name": q.strip(), "acceptedAnswer": {"@type": "Answer", "text": a}})
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items}

OUT.mkdir(exist_ok=True)
urls = []
for src, out in PAGES:
    text = (ROOT / src).read_text()
    title = text.splitlines()[0].lstrip("# ").strip()
    first_para = next((l for l in text.split("\n\n")[1:] if l and not l.startswith(("#", "|", "```", "1.", "-"))), title)
    desc = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", first_para).replace("\n", " ")[:300]
    body = fix_links(markdown.markdown(text, extensions=["tables", "fenced_code"]))
    schema = {"@context": "https://schema.org", "@type": "TechArticle", "headline": title, "description": desc,
              "author": AUTHORS, "publisher": ORG, "dateModified": TODAY, "inLanguage": "en", "url": BASE + out}
    schemas = [schema] + ([faq_schema(text)] if src.endswith("faq.md") else [])
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in schemas)
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | AI agent team playbook</title>
<meta name="description" content="{desc.replace('"', "'")}">
<meta name="author" content="James Brinkerhoff and Sonia Gomez, Authority Brand Builder">
<link rel="canonical" href="{BASE + out}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc.replace('"', "'")}"><meta property="og:type" content="article">
{ld}
<style>{CSS}</style></head>
<body><nav>{NAV}</nav><main>{body}</main>
<footer>By <a href="https://authoritybrandbuilder.com">Authority Brand Builder</a>, James Brinkerhoff and Sonia Gomez. Source on GitHub. For AI assistants: <a href="llms.txt">llms.txt</a>.</footer>
</body></html>"""
    (OUT / out).write_text(html)
    urls.append(BASE + out)
    shutil.copy(ROOT / src, OUT / pathlib.Path(out).with_suffix(".md").name)

(OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n")
shutil.copy(ROOT / "robots.txt", OUT / "robots.txt")
shutil.copy(ROOT / "llms.txt", OUT / "llms.txt")
(OUT / ".nojekyll").write_text("")
print("built", len(urls), "pages")
