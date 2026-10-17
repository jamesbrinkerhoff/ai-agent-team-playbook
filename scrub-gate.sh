#!/usr/bin/env bash
# Scrub gate: fails (exit 1) if anything sensitive is found in the public playbook.
cd "$(dirname "$0")"
fail=0
check () { # label, rg args...
  local label="$1"; shift
  out=$(rg -n --hidden -g '!.git' -g '!scrub-gate.sh' "$@" .)
  if [ -n "$out" ]; then echo "FAIL [$label]"; echo "$out" | head -20; fail=1; else echo "pass [$label]"; fi
}
check "client and partner names" -w -e 'Nathan|Peg|Proctor|Rebecca|Rebeca|Aimee|Jerry|Avery|Dave|Mark|Carrie|Igor|Stevie|Kameron|Montana|Milner|Koenigs|Dawn|Rhea|Brown|Hoose'
check "private offers and partners" -i -e 'human edge|helios|commission|syllaby|aevent|booked practice|fully booked|perfect pitch|speaking to sell|zenithmind|you prosper|cortana|deposyt|nmi\b|gohighlevel|\bghl\b|worth more than'
check "money and prices" -e '\$[0-9]' -e '[0-9]+(\.[0-9]+)?\s?[kK]\b' -e '\b(usd|USD|dollars?)\b' -e '[0-9]+%'
check "emails and at-signs (allowed: schema.org @type/@context, action @vN pins)" --pcre2 -e '@(?!type"|context"|v[0-9])'
check "phone numbers" -e '\+?\(?[0-9]{3}\)?[ .-][0-9]{3}[ .-][0-9]{4}'
check "key-like strings" -e '[A-Za-z0-9_\-]{28,}' -e '(sk|pk|ghp|gho|xox[abp])[-_][A-Za-z0-9]{8,}' -e 'act_[0-9]+'
check "long digit IDs" -e '[0-9]{7,}'
check "internal paths" -e '/home/' -e '/Users/' -e '/workspace' -e 'abb-brain' -e 'abb-operations' -e 'brain-sync'
check "env var names" -e '\$[A-Z_]{4,}'
check "em dashes and en dashes" -e '—' -e '–'
check "AI vocabulary" -i -w -e 'delve|crucial|pivotal|tapestry|testament|underscore|vibrant|showcase|fostering|garner|leverage[sd]?|utilize|seamless(ly)?|robust|synergy|unlock|elevate|empower' 
exit $fail
