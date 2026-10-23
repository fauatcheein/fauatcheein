"""Fetch visitor counts per country from GoatCounter and write _data/visitors.json.

Run daily by .github/workflows/visitor-stats.yml, which sets the site code
("fauatcheein"). Needs one secret in the GitHub repository
(Settings > Secrets and variables > Actions > Secrets):
  GOATCOUNTER_TOKEN  API token from GoatCounter (Settings > API tokens, read statistics)
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

CODE = os.environ.get("GOATCOUNTER_CODE", "").strip()
TOKEN = os.environ.get("GOATCOUNTER_TOKEN", "").strip()
SINCE = os.environ.get("STATS_SINCE", "2026-10-01").strip()
OUT = os.path.join(os.path.dirname(__file__), "..", "_data", "visitors.json")

if not CODE or not TOKEN:
    print("GOATCOUNTER_CODE or GOATCOUNTER_TOKEN not set; nothing to do.")
    sys.exit(0)

BASE = f"https://{CODE}.goatcounter.com/api/v0"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
RANGE = {"start": f"{SINCE}T00:00:00Z", "end": NOW}


def get(path, **params):
    url = f"{BASE}{path}?{urllib.parse.urlencode({**RANGE, **params})}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


countries = {}
names = {}
offset = 0
while True:
    page = get("/stats/locations", limit=100, offset=offset)
    for row in page.get("stats", []):
        code = (row.get("id") or "").upper()
        if len(code) != 2:          # skip "unknown" locations
            continue
        countries[code] = countries.get(code, 0) + int(row.get("count", 0))
        names[code] = row.get("name") or code
    if not page.get("more") or not page.get("stats"):
        break
    offset += len(page["stats"])

total = sum(countries.values())
try:
    total = int(get("/stats/total").get("total", total))
except Exception as exc:  # the per-country sum is a good fallback
    print("total endpoint failed:", exc)

data = {
    "updated": NOW,
    "since": SINCE,
    "total": total,
    "countries": dict(sorted(countries.items(), key=lambda kv: -kv[1])),
    "names": names,
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write("\n")
print(f"{len(countries)} countries, {total} visits")
