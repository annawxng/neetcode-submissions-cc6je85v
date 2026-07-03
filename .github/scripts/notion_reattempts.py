import os, json, time, datetime, urllib.request, urllib.error
TOKEN = os.environ["NOTION_TOKEN"]
SH_DB = "c807e5936ab08351a00681aca68fd731"
HDR = {"Authorization":"Bearer "+TOKEN,"Notion-Version":"2022-06-28","Content-Type":"application/json"}
REPO = os.environ.get("GITHUB_WORKSPACE", ".")
TODAY = datetime.date.today().isoformat()

def api(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request("https://api.notion.com/v1"+path, data=data, headers=HDR, method=method)
    for _ in range(4):
        try:
            with urllib.request.urlopen(req) as r: return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429: time.sleep(1.5); continue
            print("  ! API", e.code, e.read().decode()[:200]); return None
    return None

def query(db):
    out, cur = [], None
    while True:
        b = {"page_size":100}
        if cur: b["start_cursor"] = cur
        d = api("POST", f"/databases/{db}/query", b)
        if not d: break
        out += d["results"]
        if not d.get("has_more"): break
        cur = d["next_cursor"]
    return out

def slug_from(url):
    if not url: return None
    u = url.split("?")[0].rstrip("/")
    return u.split("/problems/")[-1] if "/problems/" in u else None

# 1. count submission files per problem folder
counts = {}
for root, dirs, files in os.walk(REPO):
    if "/.git" in root: continue
    subs = [f for f in files if f.startswith("submission") and f.endswith(".py")]
    if subs:
        counts[os.path.basename(root)] = counts.get(os.path.basename(root), 0) + len(subs)
print(f"Repo: {len(counts)} problems with submissions")

# 2. map Notion pages by slug (neetcode link and/or leetcode q link)
by_slug = {}
for p in query(SH_DB):
    pr = p["properties"]
    num = (pr.get("num times solved", {}) or {}).get("number") or 0
    for s in (slug_from((pr.get("neetcode link", {}) or {}).get("url")),
              slug_from((pr.get("q link", {}) or {}).get("url"))):
        if s: by_slug[s] = (p["id"], num)

# 3. update counts, comment when it went up
updated = commented = 0
for slug, count in counts.items():
    if slug not in by_slug: continue
    pid, cur = by_slug[slug]
    if count == cur: continue
    api("PATCH", f"/pages/{pid}", {"properties":{"num times solved":{"number":count}}})
    updated += 1
    if count > cur:
        api("POST", "/comments", {"parent":{"page_id":pid},
            "rich_text":[{"type":"text","text":{"content":f"🔁 Reattempt logged — submission {count} ({TODAY})"}}]})
        commented += 1
    time.sleep(0.34)
print(f"Updated {updated} counts, added {commented} reattempt comments.")
