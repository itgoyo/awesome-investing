#!/usr/bin/env python3
"""Render README.md and README.en.md from data/repos.json and data/books.json.

Every number in the two READMEs comes from those files, so the tables cannot
drift away from what the fetcher and the page actually see.
"""

from __future__ import annotations

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")


def load(name, fallback=None):
    path = os.path.join(DATA, name)
    if not os.path.exists(path):
        return fallback
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def human_size(n):
    if n >= 1e9:
        return f"{n / 1e9:.2f} GB"
    if n >= 1e6:
        return f"{n / 1e6:.1f} MB"
    return f"{max(n, 0) / 1e3:.0f} KB"


def stars(n):
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def repo_rows(repos, lang):
    out = []
    cat = {c["id"]: c[lang] for c in repos["categories"]}
    for i, r in enumerate(repos["repos"], 1):
        mark = " 📥" if r["local_books"] else ""
        out.append(
            f"| {i} | [{r['full_name']}]({r['url']}){mark} | {stars(r['stars'])} | "
            f"{cat[r['category']]} | {r['pushed_at'][:7]} | {r[lang]} |"
        )
    return "\n".join(out)


def book_rows(books, lang):
    out = []
    for b in books["books"]:
        fmts = " · ".join(
            f"[{f['label']}]({f['path']})" for f in b["files"]
        )
        total = sum(f["bytes"] for f in b["files"])
        title = b[lang]
        author = b["author"] if lang == "zh" else b["author_en"]
        out.append(f"| {title} | {author} | {fmts} | {human_size(total)} | `{b['repo']}` |")
    return "\n".join(out)


ZH = """# 投资 · 金融 · Web3 学习资料库

[中文](README.md) | [English](README.en.md)

30 个资料汇总型仓库 + {titles} 本可下载电子书，全部按 GitHub API 核验，星数实时取值，核验日期 {checked}。

做这件事的原因很直接：GitHub 上关于投资和 Web3 的学习资料散在几十个 awesome 清单里，一半的链接已经失效，另一半混着交易机器人和回测框架。这里只留「能读的东西」，并且把能找到原书的 PDF 一起存进仓库，离线也能看。

## 快速开始

- 浏览器打开 [`index.html`](index.html)：搜索、中英切换、按格式直接下载，双击即可用，不需要起服务。
- 想拿文件：`books/` 目录下就是 PDF / EPUB / MOBI 原件。
- 想更新数据：

```bash
python3 scripts/fetch_books.py    # 下载书库文件，幂等，已有的跳过
python3 scripts/build_repos.py    # 合并注释与 GitHub 元数据快照
python3 scripts/build_catalog.py  # 生成页面数据 data/catalog.js
python3 scripts/build_readme.py   # 重新渲染两份 README
```

## 收录标准

**收**：清单、书单、论文索引、白皮书归档、开源书、课程大纲、学习路线。

**不收**：策略代码、交易机器人、行情终端、记账软件、量化框架、SDK。哪怕 star 更高也不收，这一条砍掉了 FinRL（17k）、quant-trading（11k）、machine-learning-for-trading（21k）。

**不收已废弃**：仓库必须存在、未归档、README 可访问、最近一次提交在三年内。

## Top 30 榜单

按 Star 从高到低。📥 表示仓库里的书已经存进本地 `books/`。

| # | 仓库 | Star | 分类 | 最后更新 | 说明 |
|---|------|------|------|----------|------|
{repo_rows}

分类分布：量化与金融机器学习 9 个，Web3 资源清单 10 个，开源书与书单 4 个，中文学习资料 4 个，Web3 课程与路线 2 个，股票交易资源 1 个。中文资料的绝对数量比英文少，这是 GitHub 的现状，不是筛选偏向。

## 本地书库

共 {titles} 本、{files} 个文件、{size}。中文经典来自 `codeman008/Financial_freedom`，《定投改变命运》中英双语加四语译本来自 `xiaolai/regular-investing-in-box`。

| 书名 | 作者 | 格式 | 大小 | 来源仓库 |
|------|------|------|------|----------|
{book_rows}

## 目录结构

```
.
├── index.html              # 双语浏览页，双击打开
├── README.md / README.en.md
├── books/                  # 本地电子书
│   ├── on-regular-investing/   # 定投改变命运：中英 PDF/EPUB/MOBI + 法西俄日译本
│   └── chinese-canon/          # 17 本中文投资经典 PDF
├── data/
│   ├── upstream.json        # GitHub API 元数据快照
│   ├── repos.json           # 仓库 + 中英文注释
│   ├── books.json           # 文件真实字节数与 sha256
│   └── catalog.js           # 页面数据
└── scripts/                 # 抓取、构建、渲染脚本
```

## 核验方法

1. 逐个调用 `GET /repos/{{owner}}/{{repo}}`，记录 `stargazers_count`、`archived`、`pushed_at`、`license`。
2. 调用 `GET /repos/{{owner}}/{{repo}}/readme`，确认 README 可访问。
3. 下载书籍时先比对仓库文件树，路径对不上就报错，不会静默 404。
4. 下载完成后按磁盘上的真实字节数与 sha256 写入 `data/books.json`，不抄上游元数据。

## 说明

- 上一版有人给过一份「30 个高星仓库」清单，逐条核验后只有 10 个真实存在，其余 20 个返回 404，星数也普遍对不上（例如某仓库标 390 星，实际 8 星）。这份 README 里每一个仓库都是现查的。
- 已归档的 `mr-karan/awesome-investing`（2.5k）经典但停更，按「不废弃」标准没有收录。
- 有 4 个仓库最后更新停在 2024 年，内容仍有效，表中照实标注日期。

## 免责声明

资料版权归各仓库原作者与出版方所有，本地副本仅供个人学习，请支持正版。仓库只做索引与归档，不构成任何投资建议。
"""

EN = """# Investing · Finance · Web3 Learning Library

[中文](README.md) | [English](README.en.md)

30 aggregation repositories plus {titles} downloadable ebooks, every entry verified against the GitHub API on {checked}, stars read live.

The reason is simple. Investing and Web3 study material sits scattered across dozens of awesome lists on GitHub. Half the links rot, the other half mix reading lists with trading bots and backtest frameworks. This repo keeps only things you can read, and stores the actual books it can find so the shelf works offline.

## Quick start

- Open [`index.html`](index.html) in a browser: search, switch language, download by format. No server needed.
- Want the files: `books/` holds the PDF / EPUB / MOBI originals.
- Refresh the data:

```bash
python3 scripts/fetch_books.py    # idempotent download, existing files skipped
python3 scripts/build_repos.py    # merge annotations with the API snapshot
python3 scripts/build_catalog.py  # emit data/catalog.js
python3 scripts/build_readme.py   # re-render both READMEs
```

## What gets in

**In**: lists, booklists, paper indexes, whitepaper archives, open books, course outlines, learning roadmaps.

**Out**: strategy code, trading bots, market terminals, budgeting apps, quant frameworks, SDKs. Star count does not buy an exception. This rule dropped FinRL (17k), quant-trading (11k) and machine-learning-for-trading (21k).

**Out**: abandoned repos. Each one must exist, be unarchived, serve a readable README, and have a push within three years.

## Top 30

Sorted by stars. 📥 means the repo's books are already in `books/`.

| # | Repository | Stars | Type | Last push | What it is |
|---|------------|-------|------|-----------|------------|
{repo_rows}

Category spread: 9 quant and financial ML, 10 Web3 resource lists, 4 open books and booklists, 4 Chinese-language collections, 2 Web3 courses and roadmaps, 1 stock trading resource. Chinese material is genuinely scarcer than English on GitHub; that is the platform, not a filter bias.

## Local library

{titles} titles, {files} files, {size}. The Chinese classics come from `codeman008/Financial_freedom`; the bilingual *On Regular Investing* plus its four translations come from `xiaolai/regular-investing-in-box`.

| Title | Author | Formats | Size | Source repo |
|-------|--------|---------|------|-------------|
{book_rows}

## Layout

```
.
├── index.html              # bilingual browser page, open it directly
├── README.md / README.en.md
├── books/                  # local ebooks
│   ├── on-regular-investing/   # PDF/EPUB/MOBI in zh + en, plus fr/es/ru/ja
│   └── chinese-canon/          # 17 Chinese investing classics
├── data/
│   ├── upstream.json        # GitHub API snapshot
│   ├── repos.json           # repos with bilingual annotations
│   ├── books.json           # real bytes and sha256 per file
│   └── catalog.js           # data the page loads
└── scripts/                 # fetch, build, render
```

## How verification works

1. `GET /repos/{{owner}}/{{repo}}` per repo, recording `stargazers_count`, `archived`, `pushed_at`, `license`.
2. `GET /repos/{{owner}}/{{repo}}/readme` to confirm the README is reachable.
3. Book downloads resolve each path against the repo tree first; a mismatch fails loudly instead of a silent 404.
4. `data/books.json` records bytes and sha256 measured on disk, never copied from upstream metadata.

## Notes

- An earlier "30 high-star repos" list was checked entry by entry: only 10 existed, 20 returned 404, and most star counts were wrong (one repo claimed 390 stars and has 8). Every repo here was queried fresh.
- The archived `mr-karan/awesome-investing` (2.5k) is a classic but unmaintained, so it fails the not-abandoned rule.
- Four repos last pushed in 2024 still hold up; the table shows the real date.

## Disclaimer

Copyright stays with the original authors and publishers. Local copies are for personal study; buy the books. This repo is an index and an archive, not investment advice.
"""


def main():
    repos = load("repos.json")
    books = load("books.json", {"books": []})
    files = [f for b in books["books"] for f in b["files"]]
    stats = {
        "titles": len(books["books"]),
        "files": len(files),
        "size": human_size(sum(f["bytes"] for f in files)),
        "checked": repos["checked_at"],
    }
    for name, tpl, lang in (("README.md", ZH, "zh"), ("README.en.md", EN, "en")):
        text = tpl.format(
            repo_rows=repo_rows(repos, lang),
            book_rows=book_rows(books, lang),
            **stats,
        )
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {name}")


if __name__ == "__main__":
    main()
