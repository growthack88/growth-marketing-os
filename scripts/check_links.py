#!/usr/bin/env python3
"""Validate that every relative markdown link in the repo resolves to a real file."""
import os, re, sys

broken = []
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if not d.startswith(".git")]
    for fn in files:
        if not fn.endswith(".md"):
            continue
        path = os.path.join(root, fn)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for m in re.finditer(r"\[([^\]]*)\]\(([^)]+)\)", text):
            target = m.group(2).split("#")[0].strip()
            if not target or target.startswith(("http", "mailto:", "<")):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(root, target))):
                broken.append(f"{path}: ({m.group(2)})")

if broken:
    print("BROKEN LINKS:")
    print("\n".join(broken))
    sys.exit(1)
print("All relative links OK")
