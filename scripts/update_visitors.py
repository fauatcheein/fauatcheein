"""Fetch visitor counts per country from GoatCounter and write _data/visitors.json.

Run daily by .github/workflows/visitor-stats.yml, which sets the site code
("fauatcheein"). Needs one secret in the GitHub repository
(Settings > Secrets and variables > Actions > Secrets):
  GOATCOUNTER_TOKEN  API token from GoatCounter (Settings > API tokens, read statistics)
"""
import json
import os
import sys
import urllib.error
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
NOW = datetime.now(timezone.utc)
# Date format that GoatCounter accepted on the first successful run; the second is a fallback.
RANGES = [
    {"start": f"{SINCE}T00:00:00Z", "end": NOW.strftime("%Y-%m-%dT%H:%M:%SZ")},
    {"start": SINCE, "end": NOW.strftime("%Y-%m-%d")},
]


def fail(msg):
    # "::error::" lines show up as a readable summary on the GitHub Actions run page
    msg = msg.replace(TOKEN, "[token]").replace("\n", " ")
    print(f"::error::{msg}")
    sys.exit(1)


def get(path, **params):
    url = f"{BASE}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "fauatcheein-website-stats",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:400]
        raise RuntimeError(f"GoatCounter {path} returned HTTP {exc.code}: {body}") from None
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach GoatCounter ({exc.reason})") from None


def fetch_locations():
    errors = []
    for rng in RANGES:
        try:
            rows, offset = [], 0
            while True:
                params = {**rng, "limit": 100}
                if offset:
                    params["offset"] = offset
                page = get("/stats/locations", **params)
                rows += page.get("stats") or []
                if not page.get("more") or not page.get("stats") or offset > 1000:
                    return rows, rng
                offset = len(rows)
        except RuntimeError as exc:
            errors.append(str(exc))
            if "HTTP 401" in str(exc) or "HTTP 403" in str(exc):
                break   # a permission problem will not be fixed by another date format
    fail(" | ".join(errors))


rows, RANGE = fetch_locations()
countries, names = {}, {}
for row in rows:
    code = (row.get("id") or "").upper()
    if len(code) != 2:          # skip "unknown" locations
        continue
    countries[code] = countries.get(code, 0) + int(row.get("count", 0))
    names[code] = row.get("name") or code

total = sum(countries.values())
try:
    total = int(get("/stats/total", **RANGE).get("total", total))
except Exception as exc:  # the per-country sum is a good fallback
    print("total endpoint failed:", exc)

data = {
    "updated": NOW.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "since": SINCE,
    "total": total,
    "countries": dict(sorted(countries.items(), key=lambda kv: -kv[1])),
    "names": names,
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write("\n")
print(f"{len(countries)} countries, {total} visits")
