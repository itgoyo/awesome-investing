#!/usr/bin/env python3
"""Turn content/*.md into the data the page loads, and into both READMEs.

Each chapter file holds a Chinese body and an English body separated by an
`<!-- en -->` marker. The manifest below owns titles, summaries and the books
each chapter points at, so no chapter file repeats that metadata.
"""

from __future__ import annotations

import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
DATA = os.path.join(ROOT, "data")

CHAPTERS = [
    {
        "id": "01-foundation",
        "num": "01",
        "zh": "投资的收益来源",
        "en": "Where Return Comes From",
        "zh_sum": "先弄清钱是谁赚的，再谈方法。收益的三个来源、你能控制的三件事、beta 与 alpha 的分界。",
        "en_sum": "Whose money you earn, the three sources of return, the three things you control, and the line between beta and alpha.",
        "books": ["touzi-zhong-zui-jiannan-de-shi", "congming-de-touzizhe"],
    },
    {
        "id": "02-statements",
        "num": "02",
        "zh": "读财报：排除法",
        "en": "Reading Statements: Exclusion, Not Precision",
        "zh_sum": "三张表的勾稽、经营现金流与自由现金流、杜邦分解看穿高 ROE、六个红旗。",
        "en_sum": "How the three statements reconcile, free cash flow, DuPont to see through a high ROE, six red flags.",
        "books": ["yibenshu-du-dong-caibao"],
    },
    {
        "id": "03-valuation",
        "num": "03",
        "zh": "估值与安全边际",
        "en": "Valuation and Margin of Safety",
        "zh_sum": "四把尺子各自的适用边界，DCF 为什么只能给区间，安全边际该留多厚。",
        "en_sum": "Which multiple fits which business, why DCF only yields a range, and how deep the discount must be.",
        "books": ["congming-de-touzizhe", "zhengquan-fenxi", "zenyang-xuanze-chengzhanggu", "touzi-zhong-zui-zhongyao-de-shi"],
    },
    {
        "id": "04-allocation",
        "num": "04",
        "zh": "资产配置与定投",
        "en": "Allocation and Regular Investing",
        "zh_sum": "先定股债比例再挑产品，再平衡的纪律，定投的真实数学与三个幻觉，三个隐性成本。",
        "en_sum": "Set the split before the product, rebalancing as discipline, the real arithmetic of averaging, three hidden costs.",
        "books": ["zhishu-jijin-zhinan", "gushi-changxian-fabao", "zichan-peizhi-de-yishu", "on-regular-investing", "dingtou-dala", "everybody-ought-to-be-rich"],
    },
    {
        "id": "05-psychology",
        "num": "05",
        "zh": "心理与骗局",
        "en": "Psychology and Fraud",
        "zh_sum": "六个反复出现的偏差，骗局的五段式结构，话术翻译表，以及畅销书该信哪一半。",
        "en_sum": "Six biases that keep returning, the five-part structure of a scam, a translation table for pitches, and what to trust in the bestsellers.",
        "books": ["wuhezhizhong", "fubaba-qiongbaba", "xiaogou-qianqian", "nawaer-baodian", "qiongchali-baodian"],
    },
    {
        "id": "06-quant",
        "num": "06",
        "zh": "量化的边界",
        "en": "The Limits of Quant",
        "zh_sum": "回测的四个坑、因子衰减与容量、机器学习在金融里为什么难，以及为什么这里不收藏策略代码。",
        "en_sum": "Four holes in a backtest, factor decay and capacity, why ML struggles in markets, and why no strategy code is archived here.",
        "books": [],
    },
    {
        "id": "07-web3",
        "num": "07",
        "zh": "Web3 与加密资产",
        "en": "Web3 and Crypto Assets",
        "zh_sum": "技术层解决了什么，经济层收益从谁来，DeFi 收益的四类拆解，五类骗局与六问尽调。",
        "en_sum": "What the technology actually solves, whose money funds the yield, four sources of DeFi return, five scams, six due-diligence questions.",
        "books": [],
    },
    {
        "id": "08-system",
        "num": "08",
        "zh": "建立自己的研究系统",
        "en": "Building Your Own Research System",
        "zh_sum": "信息分层、三层笔记、决策日志、复盘节奏、年度七问。",
        "en_sum": "Layering information, three-layer notes, a decision log, review cadence, seven annual questions.",
        "books": ["qiongchali-baodian", "touzi-zhong-zui-zhongyao-de-shi"],
    },
]

BOOK_NOTES = {
    "on-regular-investing": (
        "把定投从操作讲成认知，适合作为第一本，中英双语任选。",
        "Turns averaging from a tactic into a way of thinking. Best first book, available in Chinese or English.",
    ),
    "on-regular-investing-translations": (
        "同一本书的法、西、俄、日译本，用来对照术语，不必通读。",
        "The same book in French, Spanish, Russian and Japanese. Useful for terminology, not for reading cover to cover.",
    ),
    "dingtou-dala": (
        "短讲义，一小时读完，先看它再决定要不要读全书。",
        "A short lecture, one sitting. Read it before deciding whether to open the full book.",
    ),
    "everybody-ought-to-be-rich": (
        "1929 年的原始短文，定投思想的历史起点，读三页就够。",
        "The 1929 essay where the averaging argument starts. Three pages.",
    ),
    "congming-de-touzizhe": (
        "安全边际与市场先生，价值投资的语法书，重点在第八、二十章。",
        "Margin of safety and Mr Market. The grammar of value investing, concentrated in chapters 8 and 20.",
    ),
    "zhengquan-fenxi": (
        "比《聪明的投资者》更硬，当工具书查阅，不建议通读。",
        "Harder than The Intelligent Investor. Use it as a reference, not a read-through.",
    ),
    "qiongchali-baodian": (
        "多元思维模型与逆向思考，读演讲部分即可，其余是编排。",
        "Mental models and inversion. The speeches carry it; the rest is arrangement.",
    ),
    "zenyang-xuanze-chengzhanggu": (
        "十五要点是一份可执行的问清单，成长股研究的原始框架。",
        "The fifteen points are a usable question list. The original growth-investing framework.",
    ),
    "zenyang-xuanze-chengzhanggu-quanyi": (
        "同一本书的全译本，与前一本二选一，译文更完整。",
        "A fuller translation of the same book. Pick one of the two.",
    ),
    "touzi-zhong-zui-jiannan-de-shi": (
        "本土案例最多，讲行业格局与定价权，比翻译书更贴近 A 股。",
        "The most local cases. Industry structure and pricing power, closer to A-shares than any translation.",
    ),
    "touzi-zhong-zui-zhongyao-de-shi": (
        "周期、风险、第二层思维，备忘录体的典范，适合反复翻。",
        "Cycles, risk and second-level thinking in memo form. Worth rereading.",
    ),
    "yibenshu-du-dong-caibao": (
        "中文财报入门最省时间的一本，读完能看懂三张表的关系。",
        "The fastest Chinese introduction to statements. You finish able to read the three together.",
    ),
    "zhishu-jijin-zhinan": (
        "指数基金的估值与定投实操，工具性强，注意成书较早。",
        "Practical index-fund valuation and averaging. Tool-like, though written a while ago.",
    ),
    "gushi-changxian-fabao": (
        "用两百年数据看长期收益来源，专治短期焦虑。",
        "Two centuries of data on where long-run return comes from. A cure for short-term anxiety.",
    ),
    "zichan-peizhi-de-yishu": (
        "资产配置的教科书式综述，图表多，适合当手册查。",
        "A textbook survey of asset allocation, chart-heavy, good as a manual.",
    ),
    "gupiao-zuoshou-huiyilu": (
        "交易者心理的经典叙事，当故事读，别当方法学。",
        "The classic narrative of a trader's psychology. Read it as a story, not a method.",
    ),
    "wuhezhizhong": (
        "1895 年的观察随笔，取其直觉，弃其论断，它不是实验研究。",
        "An 1895 essay of observation. Take the intuition, drop the claims. It is not research.",
    ),
    "fubaba-qiongbaba": (
        "现金流思维的入门读物，核心一句值得记，操作建议有过时之处。",
        "An entry point to cash-flow thinking. One idea worth keeping, the tactics are dated.",
    ),
    "xiaogou-qianqian": (
        "给孩子或零基础的人，讲储蓄、目标与延迟满足。",
        "For children or complete beginners. Saving, goals and delayed gratification.",
    ),
    "nawaer-baodian": (
        "讲财富与幸福的关系，偏观念，不含可执行方法。",
        "On wealth and happiness. Conceptual, no executable method.",
    ),
    "nawaer-baodian-caifu": (
        "同书的另一版本，内容高度重复，与前一本选一即可。",
        "Another edition of the same book. Highly duplicative, pick one.",
    ),
}


def md_to_html(text):
    """Convert the small markdown subset these chapters use."""
    out = []
    para = []
    list_kind = None

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def close_list():
        nonlocal list_kind
        if list_kind:
            out.append(f"</{list_kind}>")
            list_kind = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_para()
            close_list()
            continue
        if line.startswith("### "):
            flush_para(); close_list()
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            flush_para(); close_list()
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("- "):
            flush_para()
            if list_kind != "ul":
                close_list(); out.append("<ul>"); list_kind = "ul"
            out.append(f"<li>{inline(line[2:])}</li>")
        elif re.match(r"^\d+\.\s", line):
            flush_para()
            if list_kind != "ol":
                close_list(); out.append("<ol>"); list_kind = "ol"
            out.append(f"<li>{inline(re.sub(r'^\d+\.\s', '', line))}</li>")
        elif line.strip() == "---":
            flush_para(); close_list()
            out.append("<hr>")
        elif line.startswith("> "):
            flush_para(); close_list()
            out.append(f"<blockquote>{inline(line[2:])}</blockquote>")
        else:
            close_list()
            para.append(line.strip())
    flush_para()
    close_list()
    return "\n".join(out)


def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def load_books():
    path = os.path.join(DATA, "books.json")
    with open(path, encoding="utf-8") as fh:
        books = json.load(fh)["books"]
    for b in books:
        b.pop("repo", None)
        for f in b["files"]:
            f.pop("upstream", None)
    return books


def human_size(n):
    if n >= 1e9:
        return f"{n / 1e9:.2f} GB"
    if n >= 1e6:
        return f"{n / 1e6:.1f} MB"
    return f"{max(n, 0) / 1e3:.0f} KB"


def parse_chapter(cid):
    with open(os.path.join(CONTENT, cid + ".md"), encoding="utf-8") as fh:
        raw = fh.read()
    parts = re.split(r"<!--\s*en\s*-->", raw, maxsplit=1)
    if len(parts) != 2:
        raise SystemExit(f"{cid}.md is missing the <!-- en --> marker")
    zh = parts[0].replace("<!-- zh -->", "").strip()
    en = parts[1].strip()
    en_html = md_to_html(en)
    if en_html.startswith("<hr>"):
        en_html = en_html[4:].lstrip()
    return md_to_html(zh), en_html


def build_chapters(books):
    index = {b["id"]: b for b in books}
    chapters = []
    for meta in CHAPTERS:
        zh_html, en_html = parse_chapter(meta["id"])
        related = [index[i] for i in meta["books"] if i in index]
        chapters.append(
            {
                **meta,
                "zh_html": zh_html,
                "en_html": en_html,
                "related": [{"id": b["id"], "zh": b["zh"], "en": b["en"],
                             "author": b["author"], "author_en": b["author_en"],
                             "files": b["files"]} for b in related],
            }
        )
    return chapters


def main():
    books = load_books()
    chapters = build_chapters(books)
    files = [f for b in books for f in b["files"]]
    site = {
        "chapters": chapters,
        "books": [
            {**b, "note_zh": BOOK_NOTES.get(b["id"], ("", ""))[0],
             "note_en": BOOK_NOTES.get(b["id"], ("", ""))[1]}
            for b in books
        ],
        "stats": {
            "chapters": len(chapters),
            "titles": len(books),
            "files": len(files),
            "bytes": sum(f["bytes"] for f in files),
            "words_zh": sum(len(re.findall(r"[\u4e00-\u9fff]", c["zh_html"])) for c in chapters),
        },
    }
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, "site.js"), "w", encoding="utf-8") as fh:
        fh.write("window.SITE = ")
        json.dump(site, fh, ensure_ascii=False, indent=1)
        fh.write(";\n")
    print("wrote data/site.js", site["stats"])
    return site


if __name__ == "__main__":
    main()
