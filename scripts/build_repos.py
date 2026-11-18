#!/usr/bin/env python3
"""Merge the curated annotations with the measured GitHub snapshot.

data/upstream.json holds what the GitHub API returned on the check date.
This script adds my own Chinese and English blurbs, categories and tags, then
writes data/repos.json sorted by stars. Star counts are never typed by hand.
"""

from __future__ import annotations

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "upstream.json")
OUT = os.path.join(ROOT, "data", "repos.json")

CATEGORIES = [
    ("books", "开源书与书单", "Open books and booklists"),
    ("cn", "中文学习资料", "Chinese materials"),
    ("quant", "量化与金融机器学习", "Quant and financial ML"),
    ("course", "Web3 课程与路线", "Web3 courses and roadmaps"),
    ("web3", "Web3 资源清单", "Web3 resource lists"),
    ("stock", "股票交易资源", "Stock trading resources"),
]

# full_name: (category, zh, en, tags)
ANNOT = {
    "wilsonfreitas/awesome-quant": (
        "quant",
        "量化金融最大的资源索引，书籍、论文、课程、数据源、回测框架分区清楚。清单以导航为主，代码库只是被列出来。",
        "The largest index in quantitative finance, sectioned into books, papers, courses, data sources and backtesting frameworks. Navigation only, no strategies of its own.",
        ["量化", "论文", "数据源"],
    ),
    "bitcoinbook/bitcoinbook": (
        "books",
        "《精通比特币》第 3 版开源全文，从密码学原理讲到脚本、P2P 网络和共识，读比特币源码之前先读这本。",
        "Mastering Bitcoin, 3rd edition, free full text. Cryptography through scripts, P2P networking and consensus.",
        ["比特币", "开源书", "协议原理"],
    ),
    "ethereumbook/ethereumbook": (
        "books",
        "《精通以太坊》第 2 版，账户模型、EVM、合约开发、共识机制逐章拆解，配大量可运行示例。",
        "Mastering Ethereum, 2nd edition. Accounts, EVM, contract development and consensus, chapter by chapter.",
        ["以太坊", "开源书", "智能合约"],
    ),
    "chaozh/awesome-blockchain-cn": (
        "cn",
        "中文区块链开发资料总汇，Fabric、以太坊、白皮书、视频课程都在里面，条目多到可以当字典查。",
        "A large Chinese-language blockchain library: Fabric, Ethereum, whitepapers and video courses.",
        ["中文", "区块链", "开发资料"],
    ),
    "paperswithbacktest/awesome-systematic-trading": (
        "quant",
        "系统化交易的论文、书籍、博客、教程索引，按策略类型分组，适合当研究入口。",
        "Papers, books, blogs and tutorials for systematic trading, grouped by strategy family.",
        ["系统化交易", "论文", "书单"],
    ),
    "smartcontractkit/full-blockchain-solidity-course-js": (
        "course",
        "Chainlink 官方的全栈 Web3 课程，32 小时大纲覆盖 Solidity、Hardhat、合约交互与部署，仓库里是课程大纲与配套资料。",
        "Chainlink's full-stack Web3 course: Solidity, Hardhat, contract interaction and deployment in a 32-hour outline.",
        ["Web3", "课程", "Solidity"],
    ),
    "OffcierCia/DeFi-Developer-Road-Map": (
        "course",
        "DeFi 开发者路线图与手册，按学习阶段列出该读的文档、该用的工具和该懂的协议。",
        "A DeFi developer roadmap and handbook: what to read, which tools to use, which protocols to understand, stage by stage.",
        ["DeFi", "路线图", "开发者"],
    ),
    "firmai/financial-machine-learning": (
        "quant",
        "金融机器学习资源地图，论文、书籍、课程、行业调研分门别类，偏研究方法而不是产品实现。",
        "A map of financial machine learning: papers, books, courses, industry surveys. Research-oriented.",
        ["机器学习", "论文", "研究方法"],
    ),
    "codeman008/Financial_freedom": (
        "books",
        "中文投资指南仓库，附带 17 本中文投资经典 PDF。本项目 books/chinese-canon/ 下的全部文件都来自这里。",
        "A Chinese investing guide bundled with 17 Chinese-language classics. Source of every file under books/chinese-canon/.",
        ["中文", "书单", "PDF 原书"],
    ),
    "georgezouq/awesome-ai-in-finance": (
        "quant",
        "LLM 与深度学习在金融市场的资料合集，论文、讲座、书单、开源模型分开列。",
        "LLMs and deep learning in markets: papers, talks, reading lists, open models.",
        ["AI", "LLM", "金融"],
    ),
    "xiaolai/regular-investing-in-box": (
        "books",
        "《定投改变命运》开源全书，中英双语 PDF / EPUB / MOBI，另有法、西、俄、日四语译本。本项目 books/on-regular-investing/ 的来源。",
        "The open full text of On Regular Investing: bilingual PDF / EPUB / MOBI plus FR, ES, RU and JA translations.",
        ["定投", "开源书", "多语言"],
    ),
    "DApp-Learning-DAO/DApp-Learning": (
        "course",
        "面向开发者的 DApp 学习计划，按周分任务并配中文讲义，从合约基础走到完整项目。",
        "A weekly DApp learning program with Chinese notes, from contract basics to a full project.",
        ["DApp", "中文讲义", "学习计划"],
    ),
    "thuquant/awesome-quant": (
        "quant",
        "清华量化协会维护的中文量化索引，数据源、交易平台、书籍、求职信息都有覆盖。",
        "A Chinese quant index maintained by the Tsinghua quant association: data, platforms, books, jobs.",
        ["中文", "量化", "求职"],
    ),
    "wangzhe3224/awesome-systematic-trading": (
        "quant",
        "系统化交易清单，中文标注友好，覆盖股票、期货、期权、外汇、加密货币。",
        "A systematic trading list with Chinese annotations, covering equities, futures, options, FX and crypto.",
        ["系统化交易", "中文", "工具"],
    ),
    "grananqvist/Awesome-Quant-Machine-Learning-Trading": (
        "quant",
        "机器学习做量化交易的资源清单，按数据、特征、模型、回测四段组织。",
        "Machine learning for quant trading, organised into data, features, models and backtesting.",
        ["量化", "机器学习", "资源清单"],
    ),
    "Scanate/EthList": (
        "web3",
        "以太坊阅读清单，从白皮书、黄皮书到扩容与治理，给出了必读顺序。",
        "An Ethereum reading list with a reading order, from the whitepaper and yellow paper to scaling and governance.",
        ["以太坊", "阅读清单", "文献"],
    ),
    "FrancescoXX/free-Web3-resources": (
        "web3",
        "免费 Web3 学习资源清单，课程、教程、社区、工具分区收纳。",
        "Free Web3 learning resources: courses, tutorials, communities and tools.",
        ["Web3", "免费资源", "入门"],
    ),
    "yjjnls/awesome-blockchain": (
        "web3",
        "区块链开发与应用资源清单，共识、智能合约、跨链、Layer2 分区整理。",
        "Blockchain development and application resources: consensus, contracts, cross-chain, L2.",
        ["区块链", "开发资料"],
    ),
    "jpantunes/awesome-cryptoeconomics": (
        "web3",
        "加密经济学研究资料，代币机制与激励设计的论文、读物、课程。",
        "Cryptoeconomics research: papers, readings and courses on token mechanics and incentive design.",
        ["加密经济", "论文", "机制设计"],
    ),
    "ong/awesome-decentralized-finance": (
        "web3",
        "DeFi 协议与项目清单，按借贷、DEX、衍生品、稳定币分类。",
        "DeFi protocols and projects sorted into lending, DEX, derivatives and stablecoins.",
        ["DeFi", "协议", "清单"],
    ),
    "fltenwall/web3-awesome": (
        "web3",
        "中文 Web3 百科，概念、赛道、工具按主题整理，适合建立整体地图。",
        "A Chinese Web3 encyclopedia: concepts, sectors and tools organised by theme.",
        ["中文", "Web3", "百科"],
    ),
    "JumpCrypto/crypto-reading-list": (
        "web3",
        "Jump Crypto 维护的加密阅读清单，偏研究与机制设计，收录的多是原始文献。",
        "Jump Crypto's reading list, research-heavy, mostly primary sources on mechanism design.",
        ["阅读清单", "研究", "机制设计"],
    ),
    "0voice/Awesome-QuantDev-Learn": (
        "quant",
        "量化开发的学习路线，从数据获取、因子构建、回测系统到实盘部署的知识地图。",
        "A quant developer learning path: data, factors, backtesting systems and live deployment.",
        ["中文", "学习路线", "量化开发"],
    ),
    "steven2358/awesome-blockchain-ai": (
        "web3",
        "区块链与 AI 结合的项目与论文清单，偏技术方向调研。",
        "Projects and papers at the blockchain and AI intersection.",
        ["区块链", "AI", "论文"],
    ),
    "itgoyo/awesome-crypto": (
        "web3",
        "中文币圈资源导航，交易所、钱包、链上工具、NFT 与学习资料一处集中。",
        "A Chinese crypto navigation hub: exchanges, wallets, on-chain tools, NFT and study material.",
        ["中文", "加密货币", "导航"],
    ),
    "shi-rudo/awesome-stock-trading": (
        "stock",
        "股票交易者资源清单，工具、网站、书籍三类，条目精简。",
        "Resources for stock traders in three groups: tools, websites, books.",
        ["股票", "资源清单", "书单"],
    ),
    "bekatom/awesome-ethereum": (
        "web3",
        "以太坊生态资源清单，开发工具、学习材料、社区入口都有。",
        "Ethereum ecosystem resources: dev tools, learning material, community entry points.",
        ["以太坊", "开发工具", "清单"],
    ),
    "ahmet/awesome-web3": (
        "web3",
        "Web3 资源、库与工具清单，条目按用途分组，入门友好。",
        "Web3 resources, libraries and tools grouped by purpose, beginner friendly.",
        ["Web3", "清单", "入门"],
    ),
    "SoYuCry/awesome-quant-interview": (
        "quant",
        "量化面试八股文，55 个高频考点配详解，覆盖数学统计、编程、因子与机器学习。",
        "Quant interview notes: 55 high-frequency questions with answers across stats, coding, factors and ML.",
        ["中文", "面试", "量化"],
    ),
    "imbaniac/awesome-blockchain": (
        "web3",
        "区块链服务与交易所清单，偏应用层导航，不含协议实现。",
        "Blockchain services and exchanges, application-layer navigation only.",
        ["区块链", "交易所", "清单"],
    ),
}


def main():
    snapshot = json.load(open(SRC, encoding="utf-8"))
    repos = []
    for item in snapshot["repos"]:
        name = item["full_name"]
        if name not in ANNOT:
            raise SystemExit(f"missing annotation for {name}")
        cat, zh, en, tags = ANNOT[name]
        repos.append(
            {
                "id": name.split("/")[-1].lower(),
                "full_name": name,
                "url": f"https://github.com/{name}",
                "stars": item["stars"],
                "pushed_at": item["pushed_at"],
                "archived": item["archived"],
                "license": item["license"],
                "category": cat,
                "zh": zh,
                "en": en,
                "tags": tags,
                "local_books": [],
            }
        )
    repos.sort(key=lambda r: -r["stars"])
    payload = {
        "checked_at": snapshot["checked_at"],
        "total": len(repos),
        "categories": [{"id": c, "zh": z, "en": e} for c, z, e in CATEGORIES],
        "repos": repos,
    }
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False, indent=2)
    print(f"wrote {OUT} with {len(repos)} repos")


if __name__ == "__main__":
    main()
