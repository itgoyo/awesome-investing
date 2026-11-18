#!/usr/bin/env python3
"""Render README.md and README.en.md from the same manifest the page uses."""

from __future__ import annotations

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")


def load_site():
    with open(os.path.join(DATA, "site.js"), encoding="utf-8") as fh:
        raw = fh.read()
    return json.loads(raw.split("window.SITE = ", 1)[1].rstrip().rstrip(";"))


def human_size(n):
    if n >= 1e9:
        return f"{n / 1e9:.2f} GB"
    if n >= 1e6:
        return f"{n / 1e6:.1f} MB"
    return f"{max(n, 0) / 1e3:.0f} KB"


def chapter_rows(site, lang):
    rows = []
    for c in site["chapters"]:
        rows.append(
            f"| [{c['num']} {c[lang]}](content/{c['id']}.md) | {c[lang + '_sum']} | {len(c['related'])} |"
        )
    return "\n".join(rows)


def book_rows(site, lang):
    rows = []
    for b in site["books"]:
        fmts = " · ".join(f"[{f['label'].replace('中文', 'ZH')}]({f['path']})" for f in b["files"])
        total = human_size(sum(f["bytes"] for f in b["files"]))
        title = b[lang]
        author = b["author"] if lang == "zh" else b["author_en"]
        note = b["note_zh"] if lang == "zh" else b["note_en"]
        rows.append(f"| {title} | {author} | {note} | {fmts} | {total} |")
    return "\n".join(rows)


ZH = """# 投资学习手册

[中文](README.md) | [English](README.en.md)

八章判断框架，{titles} 本本地藏书，一个能搜索的双语页面。这里没有链接清单，只有从几十份开源资料里拆出来、重写过的内容。

## 这是什么

关于投资的资料不缺，缺的是筛选。开源仓库里塞满了策略代码、失效链接和半成品笔记，能用的部分散落在各处。这份手册做了三件事：

- 把资料里反复出现的机制抽出来，写成能直接用的判断标准。
- 把不可信的部分剔掉，包括过时的操作建议和有偏的方法论。
- 把能找到原书的 PDF 存进 `books/`，离线也能读。

## 怎么读

**完全新手**：先读第 04 章（配置与定投），再读第 05 章（心理与骗局）。先不亏钱，比先赚钱重要。书从《定投改变命运》或《小狗钱钱》开始。

**有点经验**：第 01 到第 03 章顺着读，重点在第 02 章的六个红旗和第 03 章的安全边际。配合《一本书读懂财报》和《聪明的投资者》第八、二十章。

**技术背景**：直接看第 06 章和第 07 章。这两章不给代码也不给标的，只给判断边界，目的是让你在看到漂亮回测或高年化时知道该问什么。

## 目录

| 章节 | 讲什么 | 相关读物 |
|------|--------|----------|
{chapter_rows}

## 本地书库

{titles} 本，{files} 个文件，{size}。每本都写了「读它解决什么问题」，也写了它的局限。

| 书名 | 作者 | 一句话 | 格式 | 大小 |
|------|------|--------|------|------|
{book_rows}

## 取舍说明

**为什么量化部分没有本地书。** 中文世界缺少写得好的量化入门书，市面上多是策略集合，读了对判断力没有帮助。这一章只保留回测的四个坑和机器学习的信噪比问题，够用。

**为什么 Web3 部分不给标的。** 标的信息半衰期以周计，写进手册第二天就过时。给判断框架比给名单有用，六问尽调在任何项目上都适用。

**哪些书有局限。** 《乌合之众》是 1895 年的观察随笔，不是实验研究。《富爸爸穷爸爸》的现金流框架值得记，具体操作建议带着强烈的时代与国别色彩。《纳瓦尔宝典》讲的是观念，不含可执行方法。书里能直接拿来用的，只有可验证的机制那一层。

**为什么删掉了仓库名录。** 上一版把几十个仓库列成表格。表格不产生理解，读者还是要一个个点开。这一版把内容拆开重写，来源只保留在版权声明里。

## 使用

浏览器直接打开 `index.html`，中英切换、搜索、按格式下载都可以用，不需要起服务。

重新生成：

```bash
python3 scripts/fetch_books.py   # 校验并补齐书库文件
python3 scripts/build_site.py    # 生成页面数据
python3 scripts/build_readme.py  # 渲染两份 README
```

## 目录结构

```
.
├── index.html          # 双语阅读页
├── content/            # 八章正文，每篇中英对照
├── books/              # 本地藏书，PDF / EPUB / MOBI
├── data/site.js        # 页面数据
└── scripts/            # 抓取、构建、渲染
```

## 免责声明

内容为学习框架，不构成投资建议。书库文件的版权归原作者与出版方所有，详见 [NOTICE.md](NOTICE.md)。
"""

EN = """# An Investing Handbook

[中文](README.md) | [English](README.en.md)

Eight chapters of judgment frameworks, {titles} books on the local shelf, one searchable bilingual page. There is no link directory here, only material taken apart and rewritten.

## What this is

Investing material is not scarce. Filtering is. Open repositories are full of strategy code, dead links and half-finished notes, with the usable part scattered across all of it. This handbook does three things.

- Extracts the mechanisms that keep reappearing and writes them as usable standards.
- Removes what does not hold, including dated tactics and biased methods.
- Keeps the actual PDFs it could find in `books/`, so the shelf works offline.

## How to read it

**Complete beginner.** Start with chapter 04 (allocation and averaging), then 05 (psychology and fraud). Not losing comes before earning. Begin with *On Regular Investing*.

**Some experience.** Read 01 to 03 in order. The six red flags in 02 and the margin of safety in 03 carry the most weight. Pair with *Financial Statements in One Book* and chapters 8 and 20 of *The Intelligent Investor*.

**Technical background.** Go straight to 06 and 07. Neither offers code nor tickers, only the boundaries of judgment, so that a beautiful backtest or a double-digit APY tells you what to ask.

## Contents

| Chapter | What it covers | Books |
|---------|----------------|-------|
{chapter_rows}

## Local library

{titles} titles, {files} files, {size}. Each entry says what problem the book solves, and where it stops being useful.

| Title | Author | Why it is here | Formats | Size |
|-------|--------|----------------|---------|------|
{book_rows}

## Editorial choices

**No quant book on the shelf.** Chinese-language quant writing is mostly strategy collections, which do not improve judgment. The chapter keeps the four backtest holes and the signal-to-noise problem, which is enough.

**No tickers in the Web3 chapter.** Asset-level information has a half-life of weeks. A framework outlasts it; the six due-diligence questions apply to any project.

**Where the books fall short.** *The Crowd* is an 1895 essay, not research. *Rich Dad Poor Dad* has a durable cash-flow idea wrapped in tactics bound to one market and era. *The Almanack of Naval Ravikant* is philosophy without method. What transfers is the layer you can verify.

**Why the repository roster is gone.** The previous version listed dozens of projects as a table. A table produces no understanding; the reader still opens each one. This version rewrites the content and keeps provenance only in the copyright notice.

## Using it

Open `index.html` in a browser. Language switch, search and downloads all work without a server.

Rebuild:

```bash
python3 scripts/fetch_books.py   # verify and complete the shelf
python3 scripts/build_site.py    # emit page data
python3 scripts/build_readme.py  # render both READMEs
```

## Layout

```
.
├── index.html          # bilingual reader
├── content/            # eight chapters, zh and en in one file
├── books/              # PDF / EPUB / MOBI
├── data/site.js        # page data
└── scripts/            # fetch, build, render
```
"""


def main():
    site = load_site()
    files = [f for b in site["books"] for f in b["files"]]
    common = {
        "titles": site["stats"]["titles"],
        "files": site["stats"]["files"],
        "size": human_size(sum(f["bytes"] for f in files)),
    }
    for name, tpl, lang in (("README.md", ZH, "zh"), ("README.en.md", EN, "en")):
        text = tpl.format(
            chapter_rows=chapter_rows(site, lang),
            book_rows=book_rows(site, lang),
            **common,
        )
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
            fh.write(text)
        print("wrote", name)


if __name__ == "__main__":
    main()
