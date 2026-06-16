#!/usr/bin/env python3
"""
Builds tracker.json from a NeetCode-style submissions repo.

For every problem it records:
  - slug       (folder name, e.g. "course-schedule")
  - attempts   (how many submission files exist)
  - firstDate  (first time you committed a solution)
  - lastDate   (most recent time you worked on it)

Run automatically by .github/workflows/build-tracker.yml on every push.
"""
import subprocess, re, json, datetime

GENERIC = re.compile(r'^(submission[-_]?\d*|solution|sol|main|index|answer|code)$', re.I)
CODE_EXTS = {"py", "java", "cpp", "cc", "c", "js", "ts", "go", "kt",
             "swift", "rb", "cs", "rs", "scala", "php"}


def slug_for(path):
    parts = path.split("/")
    fname = parts[-1]
    if "." not in fname:
        return None
    stem, ext = fname.rsplit(".", 1)
    if ext.lower() not in CODE_EXTS:
        return None
    return parts[-2] if (GENERIC.match(stem) and len(parts) >= 2) else stem


log = subprocess.run(
    ["git", "log", "--name-only", "--format=__C__%ad", "--date=short"],
    capture_output=True, text=True).stdout

first, last = {}, {}
date = None
for line in log.splitlines():
    if line.startswith("__C__"):
        date = line[5:].strip()
        continue
    line = line.strip()
    if not line:
        continue
    s = slug_for(line)
    if not s:
        continue
    if s not in last or date > last[s]:
        last[s] = date
    if s not in first or date < first[s]:
        first[s] = date

attempts = {}
for f in subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.splitlines():
    s = slug_for(f.strip())
    if s:
        attempts[s] = attempts.get(s, 0) + 1

problems = [
    {"slug": s, "attempts": attempts.get(s, 1),
     "firstDate": first[s], "lastDate": last[s]}
    for s in sorted(last)
]

out = {"generated": datetime.date.today().isoformat(), "problems": problems}
with open("tracker.json", "w") as fh:
    json.dump(out, fh, indent=1)

print(f"Wrote tracker.json with {len(problems)} problems")
