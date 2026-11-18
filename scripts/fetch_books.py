#!/usr/bin/env python3
"""Download every book file in the catalog from its upstream public repo.

Each book entry names its upstream repo plus the exact path inside that repo.
Paths are resolved against the repo tree first, so a typo fails loudly instead
of producing a silent 404. Downloads are idempotent: an existing file with the
recorded size is kept as is unless --force is passed.

Writes data/books.json with the facts measured on disk (bytes, sha256), never
with numbers copied from upstream metadata.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".cache", "trees")
OUT = os.path.join(ROOT, "data", "books.json")


def book(pid, zh, en, author, author_en, category, tags, repo, edition_zh, edition_en, files):
    return {
        "id": pid,
        "zh": zh,
        "en": en,
        "author": author,
        "author_en": author_en,
        "category": category,
        "tags": tags,
        "repo": repo,
        "edition_zh": edition_zh,
        "edition_en": edition_en,
        "files": [(src, dest, label) for src, dest, label in files],
    }


XIAOLAI = "xiaolai/regular-investing-in-box"
FREEDOM = "codeman008/Financial_freedom"
BASE = "books/on-regular-investing"

BOOKS = [
    book(
        "on-regular-investing",
        "定投改变命运", "On Regular Investing",
        "李笑来", "Li Xiaolai",
        "定投", ["定投", "长期主义", "普通投资者", "开源书"],
        XIAOLAI,
        "作者开源全书，中英双语，PDF / EPUB / MOBI 三种格式齐全",
        "Author-released open book, Chinese and English, in PDF / EPUB / MOBI",
        [
            ("docs/pdf/on-regularinvesting-cn.pdf", f"{BASE}/OnRegularInvesting-zh.pdf", "中文 PDF"),
            ("docs/epub/OnRegularInvesting_cn.epub", f"{BASE}/OnRegularInvesting-zh.epub", "中文 EPUB"),
            ("docs/mobi/OnRegularInvesting_cn.mobi", f"{BASE}/OnRegularInvesting-zh.mobi", "中文 MOBI"),
            ("docs/pdf/on-regularinvesting-en.pdf", f"{BASE}/OnRegularInvesting-en.pdf", "EN PDF"),
            ("docs/epub/OnRegularInvesting_en.epub", f"{BASE}/OnRegularInvesting-en.epub", "EN EPUB"),
            ("docs/mobi/OnRegularInvesting_en.mobi", f"{BASE}/OnRegularInvesting-en.mobi", "EN MOBI"),
        ],
    ),
    book(
        "on-regular-investing-translations",
        "定投改变命运（多语言译本）", "On Regular Investing (translations)",
        "李笑来", "Li Xiaolai",
        "定投", ["定投", "译本"],
        XIAOLAI,
        "法、西、俄、日四语译本，社区翻译",
        "French, Spanish, Russian and Japanese translations from the community",
        [
            ("Translations/French.pdf", f"{BASE}/translations/OnRegularInvesting-fr.pdf", "FR PDF"),
            ("Translations/Spanish/Spanish.pdf", f"{BASE}/translations/OnRegularInvesting-es.pdf", "ES PDF"),
            ("Translations/Russian.pdf", f"{BASE}/translations/OnRegularInvesting-ru.pdf", "RU PDF"),
            (
                "Translations/Japanese/積立投資\u3000李笑来の自己修練.pdf",
                f"{BASE}/translations/OnRegularInvesting-ja.pdf",
                "JA PDF",
            ),
        ],
    ),
    book(
        "dingtou-dala",
        "定投——大佬的自我修养", "Regular Investing: A Veteran's Discipline",
        "李笑来", "Li Xiaolai",
        "定投", ["定投", "短篇", "讲义"],
        XIAOLAI,
        "同一仓库内的定投讲义 PDF，篇幅短，适合先读",
        "A short lecture PDF from the same repo, a good warm-up read",
        [("定投-大佬的自我修养.pdf", f"{BASE}/DingTou-Dala-Ziwo-Xiuyang.pdf", "中文 PDF")],
    ),
    book(
        "everybody-ought-to-be-rich",
        "人人都该富有（1929）", "Everybody Ought to Be Rich (1929)",
        "约翰·拉斯科布", "John J. Raskob",
        "市场史", ["历史文献", "定投起源", "公共领域"],
        XIAOLAI,
        "1929 年拉斯科布原版短文，定投思想的源头文献",
        "The 1929 Raskob essay that started the dollar-cost-averaging argument",
        [("EverybodyOughtToBeRich.pdf", f"{BASE}/EverybodyOughtToBeRich-1929.pdf", "EN PDF")],
    ),
]

# Chinese investing canon mirrored in codeman008/Financial_freedom, one entry each.
CANON = [
    ("congming-de-touzizhe", "聪明的投资者", "The Intelligent Investor",
     "本杰明·格雷厄姆", "Benjamin Graham", "价值投资", ["价值投资", "安全边际", "经典"],
     "《聪明的投资者》(美)本杰明·格雷厄姆.pdf"),
    ("zhengquan-fenxi", "证券分析", "Security Analysis",
     "本杰明·格雷厄姆 / 戴维·多德", "Benjamin Graham & David Dodd", "价值投资", ["价值投资", "估值", "经典"],
     "《证券分析》本杰明•格雷厄姆.pdf"),
    ("qiongchali-baodian", "穷查理宝典", "Poor Charlie's Almanack",
     "彼得·考夫曼 编", "Peter D. Kaufman (ed.)", "价值投资", ["芒格", "多元思维模型"],
     "《穷查理宝典》.pdf"),
    ("zenyang-xuanze-chengzhanggu", "怎样选择成长股", "Common Stocks and Uncommon Profits",
     "菲利普·费雪", "Philip Fisher", "价值投资", ["成长股", "费雪", "十五要点"],
     "《怎样选择成长股》.pdf"),
    ("zenyang-xuanze-chengzhanggu-quanyi", "怎样选择成长股（最新全译版）", "Common Stocks and Uncommon Profits (full translation)",
     "菲利普·费雪", "Philip Fisher", "价值投资", ["成长股", "全译本"],
     "《怎样选择成长股最新全译版》.pdf"),
    ("touzi-zhong-zui-jiannan-de-shi", "投资中最简单的事", "The Simplest Thing in Investing",
     "邱国鹭", "Qiu Guolu", "价值投资", ["A股", "本土实践", "行业格局"],
     "《投资中最简单的事》.pdf"),
    ("touzi-zhong-zui-zhongyao-de-shi", "投资最重要的事", "The Most Important Thing",
     "霍华德·马克斯", "Howard Marks", "价值投资", ["周期", "风险", "备忘录"],
     "《投资最重要的事》.pdf"),
    ("yibenshu-du-dong-caibao", "一本书读懂财报", "Financial Statements in One Book",
     "肖星", "Xiao Xing", "财报分析", ["财报", "入门", "三张表"],
     "《一本书读懂财报（全新修订版）》.pdf"),
    ("zhishu-jijin-zhinan", "指数基金投资指南", "The Index Fund Guide",
     "银行螺丝钉", "Yinhang Luosiding", "指数基金", ["指数基金", "定投", "估值表"],
     "《指数基金投资指南》.pdf"),
    ("gushi-changxian-fabao", "股市长线法宝（第5版）", "Stocks for the Long Run (5th ed.)",
     "杰里米·西格尔", "Jeremy Siegel", "资产配置", ["长期收益", "数据实证"],
     "《股市长线法宝（原书第5版）》.pdf"),
    ("zichan-peizhi-de-yishu", "资产配置的艺术", "The Art of Asset Allocation",
     "戴维·达斯特", "David Darst", "资产配置", ["资产配置", "组合管理"],
     "《资产配置的艺术(高清)》.pdf"),
    ("gupiao-zuoshou-huiyilu", "股票作手回忆录", "Reminiscences of a Stock Operator",
     "埃德温·勒菲弗", "Edwin Lefèvre", "市场史", ["交易史", "利弗莫尔", "传记"],
     "《股票作手回忆录》.pdf"),
    ("wuhezhizhong", "乌合之众", "The Crowd: A Study of the Popular Mind",
     "古斯塔夫·勒庞", "Gustave Le Bon", "投资心理", ["群体心理", "认知偏差"],
     "《乌合之众》古斯塔夫·勒庞.pdf"),
    ("fubaba-qiongbaba", "富爸爸，穷爸爸", "Rich Dad Poor Dad",
     "罗伯特·清崎", "Robert Kiyosaki", "理财入门", ["现金流", "资产与负债", "入门"],
     "《富爸爸,穷爸爸》.pdf"),
    ("xiaogou-qianqian", "小狗钱钱", "Kira and a Dog Named Money",
     "博多·舍费尔", "Bodo Schäfer", "理财入门", ["儿童理财", "入门", "储蓄"],
     "《小狗钱钱》.pdf"),
    ("nawaer-baodian", "纳瓦尔宝典", "The Almanack of Naval Ravikant",
     "埃里克·乔根森", "Eric Jorgenson", "理财入门", ["财富", "杠杆", "幸福"],
     "《纳瓦尔宝典》.pdf"),
    ("nawaer-baodian-caifu", "纳瓦尔宝典：财富和幸福指南", "The Almanack of Naval Ravikant (alt. edition)",
     "埃里克·乔根森", "Eric Jorgenson", "理财入门", ["财富", "杠杆", "版本差异"],
     "《纳瓦尔宝典财富和幸福指南》.pdf"),
]

for pid, zh, en, author, author_en, cat, tags, src in CANON:
    BOOKS.append(
        book(
            pid, zh, en, author, author_en, cat, tags, FREEDOM,
            "社区镜像 PDF，扫描版为主，阅读体验不如正版电子书",
            "Community-mirrored PDF, mostly scanned, inferior to a licensed ebook",
            [(src, f"books/chinese-canon/{src}", "PDF")],
        )
    )


TAG_EN = {
    "定投": "DCA", "长期主义": "long term", "普通投资者": "retail investor",
    "开源书": "open book", "译本": "translation", "短篇": "short read", "讲义": "lecture notes",
    "历史文献": "historical", "定投起源": "origin of DCA", "公共领域": "public domain",
    "价值投资": "value investing", "安全边际": "margin of safety", "经典": "classic",
    "估值": "valuation", "芒格": "Munger", "多元思维模型": "mental models",
    "成长股": "growth stocks", "费雪": "Fisher", "十五要点": "15 points", "全译本": "full translation",
    "A股": "A-shares", "本土实践": "China practice", "行业格局": "industry structure",
    "周期": "cycles", "风险": "risk", "备忘录": "memos", "财报": "statements",
    "入门": "beginner", "三张表": "three statements", "指数基金": "index funds",
    "估值表": "valuation table", "长期收益": "long-run returns", "数据实证": "empirical data",
    "资产配置": "asset allocation", "组合管理": "portfolio", "交易史": "trading history",
    "利弗莫尔": "Livermore", "传记": "biography", "群体心理": "crowd psychology",
    "认知偏差": "cognitive bias", "现金流": "cash flow", "资产与负债": "assets vs liabilities",
    "儿童理财": "kids money", "储蓄": "saving", "财富": "wealth", "杠杆": "leverage",
    "幸福": "happiness", "版本差异": "edition variant",
}


def tree_paths(repo, refresh=False):
    os.makedirs(CACHE, exist_ok=True)
    cache_file = os.path.join(CACHE, repo.replace("/", "__") + ".json")
    if os.path.exists(cache_file) and not refresh:
        with open(cache_file, encoding="utf-8") as fh:
            return json.load(fh)
    try:
        raw = subprocess.run(
            ["gh", "api", f"repos/{repo}/git/trees/HEAD?recursive=1", "--jq", ".tree[].path"],
            capture_output=True, text=True, check=True, timeout=180,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        sys.exit(f"cannot read tree of {repo}: {exc}")
    paths = [p for p in raw.splitlines() if p.strip()]
    with open(cache_file, "w", encoding="utf-8") as fh:
        json.dump(paths, fh, ensure_ascii=False)
    return paths


def resolve(repo, wanted, paths):
    if wanted in paths:
        return wanted
    tail = wanted.rsplit("/", 1)[-1]
    hits = [p for p in paths if p.endswith(tail)]
    if len(hits) == 1:
        return hits[0]
    if hits:
        sys.exit(f"ambiguous path {wanted!r} in {repo}: {hits}")
    sys.exit(f"path {wanted!r} not found in {repo}")


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download(url, dest, force=False):
    if os.path.exists(dest) and os.path.getsize(dest) > 0 and not force:
        return "kept"
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    tmp = dest + ".part"
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "awesome-investing-fetch"})
            with urllib.request.urlopen(req, timeout=120) as resp, open(tmp, "wb") as out:
                while True:
                    chunk = resp.read(1 << 20)
                    if not chunk:
                        break
                    out.write(chunk)
            os.replace(tmp, dest)
            return "new"
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == 3:
                if os.path.exists(tmp):
                    os.remove(tmp)
                sys.exit(f"download failed after 3 attempts: {url} ({exc})")
            time.sleep(2 * attempt)
    return "new"


def main(force=False):
    trees = {}
    out = []
    total_new = 0
    for entry in BOOKS:
        repo = entry["repo"]
        if repo not in trees:
            trees[repo] = tree_paths(repo, refresh=force)
        paths = trees[repo]
        files = []
        for src, dest, label in entry["files"]:
            real = resolve(repo, src, paths)
            url = "https://raw.githubusercontent.com/{}/{}/{}".format(
                repo, "HEAD", urllib.parse.quote(real)
            )
            dest_abs = os.path.join(ROOT, dest)
            state = download(url, dest_abs, force=force)
            if state == "new":
                total_new += 1
                print(f"  + {dest} ({os.path.getsize(dest_abs) / 1e6:.1f} MB)")
            else:
                print(f"  = {dest}")
            files.append(
                {
                    "label": label,
                    "path": dest,
                    "bytes": os.path.getsize(dest_abs),
                    "sha256": sha256(dest_abs),
                    "upstream": url,
                }
            )
        out.append({**{k: v for k, v in entry.items() if k != "files"},
                    "tags_en": [TAG_EN.get(g, g) for g in entry["tags"]],
                    "files": files})

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"books": out}, fh, ensure_ascii=False, indent=2)
    bills = sum(f["bytes"] for b in out for f in b["files"])
    print(f"\n{len(out)} titles, {sum(len(b['files']) for b in out)} files, "
          f"{bills / 1e6:.0f} MB on disk, {total_new} downloaded now")


if __name__ == "__main__":
    main(force="--force" in sys.argv)
