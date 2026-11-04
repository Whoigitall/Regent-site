#!/usr/bin/env python3
"""Refuse to ship a page that carries a forbidden phrase.

The main site is static HTML: build.py splits master.html into pages and the
pages are copied to the server as they are. So the gate sits in two places:
build.py calls this after writing the pages, and deploy.sh calls it before
copying. Both stop on a match.

The phrases (case-insensitive regular expressions) and the files allowed to
carry them live in forbidden-phrases.json next to this script. The check reads
the BUILT pages, not the master, because the built pages are what a visitor
reads.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent


def main() -> int:
    cfg = json.loads((HERE / "forbidden-phrases.json").read_text())
    phrases = [(p, re.compile(p, re.IGNORECASE)) for p in cfg["phrases"]]
    allow = [re.compile(p, re.IGNORECASE) for p in cfg.get("allow", [])]
    files = sorted(set(HERE.glob("*.html")) | set(HERE.glob("*.txt")))
    files = [f for f in files if f.name != "master.html"]
    hits: list[tuple[str, str, str]] = []
    scanned = 0
    for f in files:
        if any(a.search(f.name) for a in allow):
            continue
        scanned += 1
        text = f.read_text(errors="replace")
        for label, rx in phrases:
            m = rx.search(text)
            if not m:
                continue
            start = max(0, m.start() - 70)
            end = min(len(text), m.end() + 70)
            hits.append((f.name, label, re.sub(r"\s+", " ", text[start:end])))
    if scanned == 0:
        print("forbidden-phrases: nothing scanned; refusing to pass an empty check", file=sys.stderr)
        return 1
    if hits:
        print(f"\nforbidden-phrases: {len(hits)} match(es) in the built pages. Stopping.\n", file=sys.stderr)
        for name, label, snippet in hits:
            print(f"  {name}\n    phrase:  /{label}/i\n    context: …{snippet}…\n", file=sys.stderr)
        print('Fix the copy in master.html and rerun build.py (or, if the wording is legitimate on that page, add the file to "allow").', file=sys.stderr)
        return 1
    print(f"forbidden-phrases: {scanned} built pages clean ({len(phrases)} phrases)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
