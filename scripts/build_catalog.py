#!/usr/bin/env python3
"""Merge curated repo metadata with measured book facts into data/catalog.js.

index.html loads catalog.js with a script tag, so the page works when opened
straight from disk, where fetch() of a local JSON file is blocked.
"""

from __future__ import annotations

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPOS = os.path.join(ROOT, "data", "repos.json")
BOOKS = os.path.join(ROOT, "data", "books.json")
OUT = os.path.join(ROOT, "data", "catalog.js")


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    repos = load(REPOS)
    books = load(BOOKS) if os.path.exists(BOOKS) else {"books": []}

    for entry in books["books"]:
        for repo in repos["repos"]:
            if repo["full_name"] == entry["repo"]:
                if entry["id"] not in repo["local_books"]:
                    repo["local_books"].append(entry["id"])
                break
        else:
            raise SystemExit(f"book {entry['id']} points at unknown repo {entry['repo']}")

    files = [f for b in books["books"] for f in b["files"]]
    catalog = {
        "checked_at": repos["checked_at"],
        "categories": repos["categories"],
        "repos": repos["repos"],
        "books": books["books"],
        "stats": {
            "repos": len(repos["repos"]),
            "categories": len(repos["categories"]),
            "titles": len(books["books"]),
            "files": len(files),
            "bytes": sum(f["bytes"] for f in files),
            "stars": sum(r["stars"] for r in repos["repos"]),
        },
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("window.CATALOG = ")
        json.dump(catalog, fh, ensure_ascii=False, indent=2)
        fh.write(";\n")
    print(f"wrote {OUT}: {json.dumps(catalog['stats'], ensure_ascii=False)}")


if __name__ == "__main__":
    main()
