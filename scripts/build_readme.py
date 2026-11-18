#!/usr/bin/env python3
"""Render README.md and README.en.md as navigation pages from the page manifest."""

from __future__ import annotations

import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
CONTENT = os.path.join(ROOT, "content")

CAT_EN = {
    "定投": "Dollar-cost averaging",
    "价值投资": "Value investing",
    "财报分析": "Financial statements",
    "指数基金": "Index funds",
    "资产配置": "Asset allocation",
    "市场史": "Market history",
    "投资心理": "Psychology",
    "理财入门": "Money basics",
}

CAT_NOTE_ZH = {
    "定投": "先把「长期买同一件事」想清楚，再谈买什么。",
    "价值投资": "安全边际、能力圈、周期。整套框架的地基。",
    "财报分析": "目标只是排除坏公司，不必成为会计。",
    "指数基金": "承认选不出个股时的默认答案。",
    "资产配置": "决定长期结果的大部分，比选股重要。",
    "市场史": "用长周期数据压住短期情绪。",
    "投资心理": "知道偏差存在，比「克服」更现实。",
    "理财入门": "给零基础的人，也给孩子。",
}

CAT_NOTE_EN = {
    "定投": "Decide that you will buy the same thing for years before deciding what it is.",
    "价值投资": "Margin of safety, circle of competence, cycles. The foundation of everything here.",
    "财报分析": "The goal is to rule companies out, not to become an accountant.",
    "指数基金": "The default answer once you admit you cannot pick single stocks.",
    "资产配置": "It sets most of your long-run outcome, more than stock picking does.",
    "市场史": "Long-run data is the cheapest cure for short-run panic.",
    "投资心理": "Knowing a bias exists is more realistic than trying to defeat it.",
    "理财入门": "For complete beginners, and for children.",
}


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


def enc(path):
    """Encode characters that break a markdown link target."""
    return (path.replace("%", "%25").replace("(", "%28")
                .replace(")", "%29").replace(" ", "%20"))


def fix_targets(text, paths):
    """Rewrite local link targets so parentheses and spaces survive markdown."""
    for path in sorted(set(paths), key=len, reverse=True):
        text = text.replace("(" + path + ")", "(" + enc(path) + ")")
    return text


def render(tpl, **kw):
    for key, val in kw.items():
        tpl = tpl.replace("{" + key + "}", str(val))
    return tpl


def book_blocks(site, lang):
    order = list(CAT_EN.keys())
    groups = {k: [] for k in order}
    for b in site["books"]:
        groups.setdefault(b["category"], []).append(b)
    chunks = []
    for cat in order:
        items = groups.get(cat) or []
        if not items:
            continue
        heading = cat if lang == "zh" else CAT_EN[cat]
        note = CAT_NOTE_ZH[cat] if lang == "zh" else CAT_NOTE_EN[cat]
        lines = [f"### {heading}", "", f"> {note}", ""]
        for b in items:
            title = b[lang]
            author = b["author"] if lang == "zh" else b["author_en"]
            book_note = b["note_zh"] if lang == "zh" else b["note_en"]
            files = b["files"]
            total = human_size(sum(f["bytes"] for f in files))
            first = files[0]
            label = first["label"] if lang == "zh" else first["label"].replace("中文", "ZH")
            sep = "。" if lang == "zh" else ". "
            lines.append(f"- [{title}]({first['path']}) - {author} · {total} · {label}{sep}{book_note}")
            if len(files) > 1:
                rest = " · ".join(
                    f"[{f['label'] if lang == 'zh' else f['label'].replace('中文', 'ZH')}]({f['path']})"
                    for f in files[1:]
                )
                prefix = "  - 其他格式：" if lang == "zh" else "  - Other formats: "
                lines.append(prefix + rest)
        chunks.append("\n".join(lines))
    return "\n\n".join(chunks)


def cat_nav(site, lang):
    present = {b["category"] for b in site["books"]}
    seen = [c for c in CAT_EN if c in present]
    seen += [c for c in present if c not in seen]
    parts = []
    for cat in seen:
        name = cat if lang == "zh" else CAT_EN[cat]
        anchor = name.lower().replace(" ", "-")
        parts.append(f"[{name}](#{anchor})")
    return " · ".join(parts)


ZH = """<div align="center">

# 投资学习手册

**八章判断框架 · {titles} 本本地藏书 · {size} 离线可读**

资料不缺，缺的是筛选。这里没有仓库名录，只有拆开、重写过的判断标准。

[在线阅读](index.html) · [English](README.en.md) · [书库](#书库) · [版权声明](NOTICE.md)

![chapters](https://img.shields.io/badge/chapters-8-e0b155?style=flat-square)
![books](https://img.shields.io/badge/books-{titles}-e0b155?style=flat-square)
![files](https://img.shields.io/badge/files-{files}-e0b155?style=flat-square)
![size](https://img.shields.io/badge/size-{size_badge}-e0b155?style=flat-square)

</div>

&nbsp;

# 前言

开源仓库里关于投资、金融、Web3 的资料很多，能用的很少。策略代码会过期，标的推荐半衰期以周计，失效链接比有效链接多。真正留下来的，是那些讲清了「钱从哪来、风险在哪、怎么验证」的机制。

这份手册把几十份资料拆开，按判断流程重排成八章，每一章都落成能直接用的标准：六个财报红旗、四把估值尺子、骗局的五段式结构、回测的四个坑、DeFi 收益的四类拆解、尽调六问。讲不清收益来源的说法，无论包装多专业，都没有进正文。

书的部分没有照单全收。21 本里，每一本都标了「读它解决什么问题」，也标了它在哪里失效。

**三条原则：**

- 只留机制，不留结论。结论会过期，机制不会。
- 只给判断标准，不给标的。给名单是在替你做决定。
- 能验证的才写。无法验证的说法，标注为「无法验证」。

# **导航：**

[按问题查](#按问题查) | [书库](#书库) | [术语速查](#术语速查) | [骗局速查](#骗局速查) | [交易所与社群](#交易所与社群) | [声明](#声明)

## 按问题查

不必从头读。带着问题进来，找到对应那一节。

| 你想弄清楚 | 看哪章 | 关键概念 |
| :--- | :--- | :--- |
| 这笔钱到底是谁赚的 | [01](content/01-foundation.md) | 三个收益来源、beta 与 alpha |
| 这家公司财报有没有问题 | [02](content/02-statements.md) | 六个红旗、经营现金流与净利润背离 |
| 高 ROE 是真本事还是加杠杆 | [02](content/02-statements.md) | 杜邦分解三拆 |
| 现在这个价格贵不贵 | [03](content/03-valuation.md) | PE / PB / EV-EBITDA / PS 各自的边界 |
| DCF 算出来的「内在价值」能信吗 | [03](content/03-valuation.md) | 只能给区间，做敏感性分析 |
| 该拿多少仓位买股票 | [04](content/04-allocation.md) | 先定股债比例，再挑产品 |
| 定投到底有没有用 | [04](content/04-allocation.md) | 定投的真实数学、三个幻觉 |
| 一跌就想卖，涨了就拿不住 | [05](content/05-psychology.md) | 损失厌恶、锚定、决策日志 |
| 有人拉我进群，年化 30% | [05](content/05-psychology.md) | 骗局五段式、话术翻译表 |
| 回测年化 80% 能不能信 | [06](content/06-quant.md) | 回测四个坑、因子衰减、容量 |
| 这个 DeFi 项目能不能放钱 | [07](content/07-web3.md) | 收益四类拆解、尽调六问 |
| 空投要不要点、钱包要不要连 | [07](content/07-web3.md) | 假空投、无限授权、貔貅盘 |
| 怎么持续跟踪，不再靠感觉 | [08](content/08-system.md) | 信息分层、三层笔记、年度七问 |

## 书库

{titles} 本，{files} 个文件，{size}。全部已存进 `books/`，点书名直接下载，不依赖外链。每本标了「读它解决什么问题」，也标了它的局限。

**分类**：{cat_nav}

{book_blocks}

## 术语速查

| 术语 | 一句话 | 章 |
| :--- | :--- | :--- |
| beta | 跟着市场走就能拿到的那部分收益，不用判断力 | [01](content/01-foundation.md) |
| alpha | 超出市场的部分。扣掉费用后长期为正的人极少 | [01](content/01-foundation.md) |
| 自由现金流 | 经营现金流减去维持性资本开支，能自由支配的钱 | [02](content/02-statements.md) |
| 杜邦分解 | ROE = 净利率 × 总资产周转率 × 权益乘数 | [02](content/02-statements.md) |
| 商誉 | 收购溢价。减值时直接冲利润，不经过现金流 | [02](content/02-statements.md) |
| 安全边际 | 价格与估算价值之间的折扣，用来容纳你的错误 | [03](content/03-valuation.md) |
| 能力圈 | 你能判断十年后格局的行业范围，边界比大小重要 | [03](content/03-valuation.md) |
| 再平衡 | 按目标比例卖涨买跌，唯一免费的高抛低吸 | [04](content/04-allocation.md) |
| 前视偏差 | 回测里用了当时根本拿不到的数据 | [06](content/06-quant.md) |
| 因子衰减 | 因子被写进论文后收益逐步消失，容量也在缩小 | [06](content/06-quant.md) |
| 无常损失 | 做市时价格偏离带来的机会成本 | [07](content/07-web3.md) |
| 清算线 | 抵押率跌破后被强制平仓的价格，杠杆的死亡线 | [07](content/07-web3.md) |
| 第二层思维 | 不是「这家公司好不好」，而是「价格里已经包含了什么」 | [05](content/05-psychology.md) |

## 骗局速查

听到这些话，先对照右列。

| 你听到的 | 真实含义 | 出处 |
| :--- | :--- | :--- |
| 「量化搬砖，稳定月化 8%」 | 说不清钱从哪来，属于结构一 | [05](content/05-psychology.md) |
| 「早鸟的收益由后来者支付」 | 庞氏结构，必须不断拉新人 | [05](content/05-psychology.md) |
| 「名额只剩三个，今天最后一天」 | 稀缺加权威，压缩你思考的时间 | [05](content/05-psychology.md) |
| 「提现需要升级会员 / 排队 / 拉人解锁」 | 退出被设计成困难，钱进得去出不来 | [05](content/05-psychology.md) |
| 「老师带单，盈利分成」 | 收益归他，风险归你，亏损不共担 | [05](content/05-psychology.md) |
| 「空投领取，先签名授权一下」 | 授权即交出资产处置权，钱包会被清空 | [07](content/07-web3.md) |
| 「年化 400%，国库补贴」 | 激励补贴或循环抵押，不是收益是风险溢价 | [07](content/07-web3.md) |
| 「团队匿名但代码开源」 | 开源不等于无后门，也不等于有人负责 | [07](content/07-web3.md) |

## 交易所与社群

这一节是仓库的入口信息，与前面八章无关。链接含邀请码，通过它们注册能减免手续费，仓库也会拿到少量返佣；这不会改变正文里的任何判断。

加密资产交易在部分司法辖区受限，请先确认所在地法规。本金可能全部损失，任何平台的「活动」「空投」都不构成收益承诺。

[币圈导航 · 虚拟加密货币资源大全](https://github.com/itgoyo/awesome-crypto) —— 按交易所、空投、钱包、链上数据、NFT、DAO、跨链工具分类的入口清单。

| 平台 | 链接 | 说明 |
| :--- | :--- | :--- |
| 币安 Binance | [binance.com](https://accounts.binance.com/zh-CN/register?ref=FANXIAN) | 邀请码 **FANXIAN**，手续费减免 20%。平台另有 Alpha 积分活动，积分能换什么以当期公告为准，可看[教程检索](https://www.youtube.com/results?search_query=%E5%B8%81%E5%AE%89alpha) |
| 欧易 OKX | [okx.com](https://www.okx.com/zh-hans/join/50253981) | 邀请码 **50253981**，手续费减免 20%；Boost 另有邀请码 **ZHUANMI** |
| ByBit | [bybit.com](https://www.bybit.com/invite?ref=66QLX94) | 邀请码 **66QLX94**，手续费减免 20% |
| Bitget | [bitget.com](https://www.bitget.com/zh-CN/referral/register?clacCode=4BUM7GXX) | 邀请码 **4BUM7GXX**，手续费减免 20% |
| Gate.io | [gate.io](https://www.gatenode.xyz/share/USDTOKOK) | 邀请码 **USDTOKOK**，手续费减免 20% |
| 火币 HTX | [htx.com](https://www.htx.com.am/invite/zh-cn/1f?invite_code=xpi6a223) | 邀请码 **xpi6a223**，手续费减免 20% |
| 抹茶 MEXC | [mexc.co](https://promote.mexc.com/r/wIE7fPvG) | 邀请码 **wIE7fPvG**，手续费减免 20% |
| 电报交流群 | [@jmhbgroup](https://t.me/jmhbgroup) | 交流加密资产相关内容。群里不提供喊单、代操作、保本承诺，遇到这几种说法按[骗局速查](#骗局速查)处理 |

## 声明

内容为学习框架，不构成投资建议。市场有风险，任何框架都不能替代你自己的判断。书库文件版权归原作者与出版方所有，详见 [NOTICE.md](NOTICE.md)。

<div align="center">

[回到顶部](#投资学习手册) · [English](README.en.md) · [在线阅读](index.html)

</div>
"""

EN = """<div align="center">

# An Investing Handbook

**Eight chapters of judgment · {titles} books on the shelf · {size} offline**

Material is not scarce. Filtering is. No roster of repositories here, only standards that were taken apart and rewritten.

[Read online](index.html) · [中文](README.md) · [Library](#library) · [Copyright](NOTICE.md)

![chapters](https://img.shields.io/badge/chapters-8-e0b155?style=flat-square)
![books](https://img.shields.io/badge/books-{titles}-e0b155?style=flat-square)
![files](https://img.shields.io/badge/files-{files}-e0b155?style=flat-square)
![size](https://img.shields.io/badge/size-{size_badge}-e0b155?style=flat-square)

</div>

&nbsp;

# Preface

There is no shortage of open repositories about investing, finance and Web3. What is scarce is the usable part. Strategy code expires, ticker calls have a half-life of weeks, dead links outnumber live ones. What survives is the mechanism: where the money comes from, where the risk sits, how to check the claim.

This handbook takes dozens of sources apart and reorders them into eight chapters along the actual decision path. Each one ends in something you can use: six red flags in financial statements, four valuation rulers, the five-part anatomy of a scam, four holes in a backtest, four sources of DeFi yield, six due-diligence questions. Anything that could not explain where the return comes from stayed out, however professional it looked.

The books were not taken wholesale either. All {titles} entries say what problem the book solves, and where it stops being useful.

**Three rules:**

- Keep the mechanism, drop the conclusion. Conclusions expire.
- Give standards, not tickers. A list makes the decision for you.
- Only what can be verified. What cannot be verified is labelled as such.

# **Navigation:**

[By question](#by-question) | [Library](#library) | [Glossary](#glossary) | [Scam patterns](#scam-patterns) | [Exchanges](#exchanges-and-community) | [Disclaimer](#disclaimer)

## By question

You do not have to read in order. Come in with a question, leave with the section.

| What you want to settle | Chapter | Concepts |
| :--- | :--- | :--- |
| Whose money am I actually earning | [01](content/01-foundation.md) | three sources of return, beta vs alpha |
| Does this company's report have holes | [02](content/02-statements.md) | six red flags, cash flow vs profit |
| Is the high ROE real or just leverage | [02](content/02-statements.md) | the DuPont decomposition |
| Is this price expensive | [03](content/03-valuation.md) | where PE, PB, EV/EBITDA and PS each break |
| Can I trust the DCF "intrinsic value" | [03](content/03-valuation.md) | a range, plus sensitivity, never a point |
| How much should be in equities | [04](content/04-allocation.md) | set the ratio before picking products |
| Does dollar-cost averaging work | [04](content/04-allocation.md) | the actual math, three illusions |
| I want to sell when it drops | [05](content/05-psychology.md) | loss aversion, anchoring, decision log |
| Someone added me to a 30% APY group | [05](content/05-psychology.md) | the five-part scam, phrase translation |
| The backtest shows 80% a year | [06](content/06-quant.md) | four holes, factor decay, capacity |
| Can I put money into this DeFi protocol | [07](content/07-web3.md) | four yield sources, six questions |
| Should I claim this airdrop | [07](content/07-web3.md) | fake drops, unlimited approvals, honeypots |
| How do I keep track without gut feel | [08](content/08-system.md) | information tiers, three-layer notes |

## Library

{titles} titles, {files} files, {size}. Everything sits in `books/`; click a title to download, no external links. Each entry says what problem it solves and where it fails.

**Categories**：{cat_nav}

{book_blocks}

## Glossary

| Term | One line | Ch |
| :--- | :--- | :--- |
| beta | The part of your return that comes from simply holding the market | [01](content/01-foundation.md) |
| alpha | The part beyond the market. Few stay positive after fees | [01](content/01-foundation.md) |
| free cash flow | Operating cash flow minus maintenance capex, the money you can move | [02](content/02-statements.md) |
| DuPont | ROE = net margin × asset turnover × equity multiplier | [02](content/02-statements.md) |
| goodwill | Acquisition premium. Impairment hits profit, not cash | [02](content/02-statements.md) |
| margin of safety | The discount between price and your estimate, sized for your errors | [03](content/03-valuation.md) |
| circle of competence | Industries whose shape you can judge a decade out. The edge matters more than the size | [03](content/03-valuation.md) |
| rebalancing | Selling winners to buy losers by rule, the only free lunch in timing | [04](content/04-allocation.md) |
| look-ahead bias | Using data in a backtest that did not exist at the time | [06](content/06-quant.md) |
| factor decay | A published factor fades, and its capacity shrinks with it | [06](content/06-quant.md) |
| impermanent loss | The opportunity cost of market making when price moves away | [07](content/07-web3.md) |
| liquidation price | Where the collateral ratio breaks and the position is closed for you | [07](content/07-web3.md) |
| second-level thinking | Not "is this a good company" but "what is already in the price" | [05](content/05-psychology.md) |

## Scam patterns

When you hear the left column, read the right one.

| What you hear | What it means | Source |
| :--- | :--- | :--- |
| "Quant arbitrage, steady 8% a month" | No explainable source of return. Pattern one | [05](content/05-psychology.md) |
| "Early birds are paid by later joiners" | A Ponzi structure that needs new money | [05](content/05-psychology.md) |
| "Three spots left, today only" | Scarcity plus authority, to shorten your thinking | [05](content/05-psychology.md) |
| "Withdrawal needs an upgrade / a queue / referrals" | Exit is engineered to be hard | [05](content/05-psychology.md) |
| "Follow my calls, share the profit" | Upside is his, downside is yours | [05](content/05-psychology.md) |
| "To claim the airdrop, just sign this approval" | An approval hands over your assets | [07](content/07-web3.md) |
| "400% APY, subsidised by the treasury" | Emissions or recursive borrowing. Risk premium, not yield | [07](content/07-web3.md) |
| "The team is anonymous but the code is open" | Open source is neither an audit nor an owner | [07](content/07-web3.md) |

## Exchanges and community

This section is access information for the repository and has nothing to do with the eight chapters. The links carry referral codes: registering through them lowers your fees and pays the repository a small rebate. Neither changes a single judgment in the text.

Crypto trading is restricted in some jurisdictions. Check your local rules first. Principal can be lost in full, and no platform campaign or airdrop is a promise of return.

[Crypto navigation · a full directory of virtual-currency resources](https://github.com/itgoyo/awesome-crypto) — entry points grouped by exchange, airdrop, wallet, on-chain data, NFT, DAO and bridges.

| Platform | Link | Notes |
| :--- | :--- | :--- |
| Binance | [binance.com](https://accounts.binance.com/zh-CN/register?ref=FANXIAN) | Code **FANXIAN**, 20% off fees. The platform also runs an Alpha points campaign; what points are worth depends on the current announcement ([search tutorials](https://www.youtube.com/results?search_query=%E5%B8%81%E5%AE%89alpha)) |
| OKX | [okx.com](https://www.okx.com/zh-hans/join/50253981) | Code **50253981**, 20% off fees; Boost uses **ZHUANMI** |
| ByBit | [bybit.com](https://www.bybit.com/invite?ref=66QLX94) | Code **66QLX94**, 20% off fees |
| Bitget | [bitget.com](https://www.bitget.com/zh-CN/referral/register?clacCode=4BUM7GXX) | Code **4BUM7GXX**, 20% off fees |
| Gate.io | [gate.io](https://www.gatenode.xyz/share/USDTOKOK) | Code **USDTOKOK**, 20% off fees |
| HTX | [htx.com](https://www.htx.com.am/invite/zh-cn/1f?invite_code=xpi6a223) | Code **xpi6a223**, 20% off fees |
| MEXC | [mexc.co](https://promote.mexc.com/r/wIE7fPvG) | Code **wIE7fPvG**, 20% off fees |
| Telegram group | [@jmhbgroup](https://t.me/jmhbgroup) | General crypto discussion. No signals, no managed accounts, no guaranteed returns; if you meet those, apply the [scam patterns](#scam-patterns) |

## Disclaimer

This is a learning framework, not investment advice. Markets carry risk, and no framework replaces your own judgment. Book files remain the property of their authors and publishers; see [NOTICE.md](NOTICE.md).

<div align="center">

[Back to top](#an-investing-handbook) · [中文](README.md) · [Read online](index.html)

</div>
"""


def main():
    site = load_site()
    files = [f for b in site["books"] for f in b["files"]]
    stats = {
        "titles": site["stats"]["titles"],
        "files": site["stats"]["files"],
        "size": human_size(sum(f["bytes"] for f in files)),
    }
    stats["size_badge"] = stats["size"].replace(" ", "%20")
    for name, tpl, lang in (("README.md", ZH, "zh"), ("README.en.md", EN, "en")):
        text = render(
            tpl,
            book_blocks=book_blocks(site, lang),
            cat_nav=cat_nav(site, lang),
            **stats,
        )
        paths = [f["path"] for b in site["books"] for f in b["files"]]
        paths += ["content/" + c["id"] + ".md" for c in site["chapters"]]
        text = fix_targets(text, paths)
        # collapse accidental triple blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as fh:
            fh.write(text)
        print("wrote", name, len(text.splitlines()), "lines")


if __name__ == "__main__":
    main()
