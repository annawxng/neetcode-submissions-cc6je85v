import os, json, time, datetime, subprocess, urllib.request, urllib.error
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

def git_dates(relpath):
    try:
        log = subprocess.check_output(["git","-C",REPO,"log","--reverse","--format=%cs","--",relpath], text=True).split()
        return (log[0], log[-1]) if log else (None, None)
    except Exception:
        return (None, None)

# ── one-time: rename "date solved" -> "last practiced", add "first solved" ──
schema = api("GET", f"/databases/{SH_DB}")
props = (schema or {}).get("properties", {})
changes = {}
if "date solved" in props and "last practiced" not in props:
    changes["date solved"] = {"name": "last practiced"}
if "first solved" not in props:
    changes["first solved"] = {"date": {}}
if changes:
    api("PATCH", f"/databases/{SH_DB}", {"properties": changes})
    print("Schema updated:", list(changes))

# ── count submissions + first/last commit date per problem folder ──
info = {}
for root, dirs, files in os.walk(REPO):
    if "/.git" in root: continue
    subs = [f for f in files if f.startswith("submission") and f.endswith(".py")]
    if not subs: continue
    base = os.path.basename(root)
    first, last = git_dates(os.path.relpath(root, REPO))
    info[base] = {"count": len(subs), "first": first, "last": last}
print(f"Repo: {len(info)} problems")

# ── map Notion pages by slug ──
by_slug = {}
for p in query(SH_DB):
    pr = p["properties"]
    num = (pr.get("num times solved", {}) or {}).get("number") or 0
    for s in (slug_from((pr.get("neetcode link", {}) or {}).get("url")),
              slug_from((pr.get("q link", {}) or {}).get("url"))):
        if s: by_slug[s] = (p["id"], num)

# ── update counts + dates, comment on a reattempt ──
upd = com = 0
for slug, d in info.items():
    if slug not in by_slug: continue
    pid, cur = by_slug[slug]
    props = {"num times solved": {"number": d["count"]}}
    if d["last"]:  props["last practiced"] = {"date": {"start": d["last"]}}
    if d["first"]: props["first solved"]   = {"date": {"start": d["first"]}}
    api("PATCH", f"/pages/{pid}", {"properties": props}); upd += 1
    if d["count"] > cur:
        api("POST", "/comments", {"parent": {"page_id": pid},
            "rich_text": [{"type":"text","text":{"content":f"🔁 Reattempt logged — submission {d['count']} ({TODAY})"}}]})
        com += 1
    time.sleep(0.34)
print(f"Updated {upd} entries, {com} reattempt comments.")
