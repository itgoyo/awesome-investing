# Investing · Finance · Web3 Learning Library

[中文](README.md) | [English](README.en.md)

30 aggregation repositories plus 21 downloadable ebooks, every entry verified against the GitHub API on 2026-11-18, stars read live.

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
| 1 | [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant) | 30.7k | Quant and financial ML | 2026-11 | The largest index in quantitative finance, sectioned into books, papers, courses, data sources and backtesting frameworks. Navigation only, no strategies of its own. |
| 2 | [bitcoinbook/bitcoinbook](https://github.com/bitcoinbook/bitcoinbook) | 25.4k | Open books and booklists | 2024-12 | Mastering Bitcoin, 3rd edition, free full text. Cryptography through scripts, P2P networking and consensus. |
| 3 | [ethereumbook/ethereumbook](https://github.com/ethereumbook/ethereumbook) | 21.5k | Open books and booklists | 2026-10 | Mastering Ethereum, 2nd edition. Accounts, EVM, contract development and consensus, chapter by chapter. |
| 4 | [chaozh/awesome-blockchain-cn](https://github.com/chaozh/awesome-blockchain-cn) | 18.9k | Chinese materials | 2024-02 | A large Chinese-language blockchain library: Fabric, Ethereum, whitepapers and video courses. |
| 5 | [paperswithbacktest/awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading) | 15.4k | Quant and financial ML | 2026-09 | Papers, books, blogs and tutorials for systematic trading, grouped by strategy family. |
| 6 | [smartcontractkit/full-blockchain-solidity-course-js](https://github.com/smartcontractkit/full-blockchain-solidity-course-js) | 14k | Web3 courses and roadmaps | 2024-06 | Chainlink's full-stack Web3 course: Solidity, Hardhat, contract interaction and deployment in a 32-hour outline. |
| 7 | [OffcierCia/DeFi-Developer-Road-Map](https://github.com/OffcierCia/DeFi-Developer-Road-Map) | 10.9k | Web3 courses and roadmaps | 2026-11 | A DeFi developer roadmap and handbook: what to read, which tools to use, which protocols to understand, stage by stage. |
| 8 | [firmai/financial-machine-learning](https://github.com/firmai/financial-machine-learning) | 8.8k | Quant and financial ML | 2025-01 | A map of financial machine learning: papers, books, courses, industry surveys. Research-oriented. |
| 9 | [codeman008/Financial_freedom](https://github.com/codeman008/Financial_freedom) | 8.5k | Open books and booklists | 2026-08 | A Chinese investing guide bundled with 17 Chinese-language classics. Source of every file under books/chinese-canon/. |
| 10 | [georgezouq/awesome-ai-in-finance](https://github.com/georgezouq/awesome-ai-in-finance) | 6.8k | Quant and financial ML | 2026-11 | LLMs and deep learning in markets: papers, talks, reading lists, open models. |
| 11 | [xiaolai/regular-investing-in-box](https://github.com/xiaolai/regular-investing-in-box) | 6.5k | Open books and booklists | 2026-11 | The open full text of On Regular Investing: bilingual PDF / EPUB / MOBI plus FR, ES, RU and JA translations. |
| 12 | [DApp-Learning-DAO/DApp-Learning](https://github.com/DApp-Learning-DAO/DApp-Learning) | 5.8k | Web3 courses and roadmaps | 2026-03 | A weekly DApp learning program with Chinese notes, from contract basics to a full project. |
| 13 | [thuquant/awesome-quant](https://github.com/thuquant/awesome-quant) | 5.7k | Quant and financial ML | 2026-11 | A Chinese quant index maintained by the Tsinghua quant association: data, platforms, books, jobs. |
| 14 | [wangzhe3224/awesome-systematic-trading](https://github.com/wangzhe3224/awesome-systematic-trading) | 5.4k | Quant and financial ML | 2026-11 | A systematic trading list with Chinese annotations, covering equities, futures, options, FX and crypto. |
| 15 | [grananqvist/Awesome-Quant-Machine-Learning-Trading](https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading) | 4.1k | Quant and financial ML | 2025-05 | Machine learning for quant trading, organised into data, features, models and backtesting. |
| 16 | [Scanate/EthList](https://github.com/Scanate/EthList) | 3.9k | Web3 resource lists | 2026-05 | An Ethereum reading list with a reading order, from the whitepaper and yellow paper to scaling and governance. |
| 17 | [FrancescoXX/free-Web3-resources](https://github.com/FrancescoXX/free-Web3-resources) | 3.7k | Web3 resource lists | 2024-10 | Free Web3 learning resources: courses, tutorials, communities and tools. |
| 18 | [yjjnls/awesome-blockchain](https://github.com/yjjnls/awesome-blockchain) | 3.6k | Web3 resource lists | 2026-11 | Blockchain development and application resources: consensus, contracts, cross-chain, L2. |
| 19 | [jpantunes/awesome-cryptoeconomics](https://github.com/jpantunes/awesome-cryptoeconomics) | 1.8k | Web3 resource lists | 2024-06 | Cryptoeconomics research: papers, readings and courses on token mechanics and incentive design. |
| 20 | [ong/awesome-decentralized-finance](https://github.com/ong/awesome-decentralized-finance) | 1.7k | Web3 resource lists | 2026-01 | DeFi protocols and projects sorted into lending, DEX, derivatives and stablecoins. |
| 21 | [fltenwall/web3-awesome](https://github.com/fltenwall/web3-awesome) | 1.4k | Web3 resource lists | 2024-11 | A Chinese Web3 encyclopedia: concepts, sectors and tools organised by theme. |
| 22 | [JumpCrypto/crypto-reading-list](https://github.com/JumpCrypto/crypto-reading-list) | 1.4k | Web3 resource lists | 2024-08 | Jump Crypto's reading list, research-heavy, mostly primary sources on mechanism design. |
| 23 | [0voice/Awesome-QuantDev-Learn](https://github.com/0voice/Awesome-QuantDev-Learn) | 1.2k | Quant and financial ML | 2025-07 | A quant developer learning path: data, factors, backtesting systems and live deployment. |
| 24 | [steven2358/awesome-blockchain-ai](https://github.com/steven2358/awesome-blockchain-ai) | 1.2k | Web3 resource lists | 2026-02 | Projects and papers at the blockchain and AI intersection. |
| 25 | [itgoyo/awesome-crypto](https://github.com/itgoyo/awesome-crypto) | 1.1k | Web3 resource lists | 2026-10 | A Chinese crypto navigation hub: exchanges, wallets, on-chain tools, NFT and study material. |
| 26 | [shi-rudo/awesome-stock-trading](https://github.com/shi-rudo/awesome-stock-trading) | 946 | Stock trading resources | 2026-10 | Resources for stock traders in three groups: tools, websites, books. |
| 27 | [bekatom/awesome-ethereum](https://github.com/bekatom/awesome-ethereum) | 910 | Web3 resource lists | 2026-10 | Ethereum ecosystem resources: dev tools, learning material, community entry points. |
| 28 | [ahmet/awesome-web3](https://github.com/ahmet/awesome-web3) | 909 | Web3 resource lists | 2026-11 | Web3 resources, libraries and tools grouped by purpose, beginner friendly. |
| 29 | [SoYuCry/awesome-quant-interview](https://github.com/SoYuCry/awesome-quant-interview) | 909 | Quant and financial ML | 2026-08 | Quant interview notes: 55 high-frequency questions with answers across stats, coding, factors and ML. |
| 30 | [imbaniac/awesome-blockchain](https://github.com/imbaniac/awesome-blockchain) | 895 | Web3 resource lists | 2024-04 | Blockchain services and exchanges, application-layer navigation only. |

Category spread: 9 quant and financial ML, 10 Web3 resource lists, 4 open books and booklists, 4 Chinese-language collections, 2 Web3 courses and roadmaps, 1 stock trading resource. Chinese material is genuinely scarcer than English on GitHub; that is the platform, not a filter bias.

## Local library

21 titles, 29 files, 231.3 MB. The Chinese classics come from `codeman008/Financial_freedom`; the bilingual *On Regular Investing* plus its four translations come from `xiaolai/regular-investing-in-box`.

| Title | Author | Formats | Size | Source repo |
|-------|--------|---------|------|-------------|
| On Regular Investing | Li Xiaolai | [中文 PDF](books/on-regular-investing/OnRegularInvesting-zh.pdf) · [中文 EPUB](books/on-regular-investing/OnRegularInvesting-zh.epub) · [中文 MOBI](books/on-regular-investing/OnRegularInvesting-zh.mobi) · [EN PDF](books/on-regular-investing/OnRegularInvesting-en.pdf) · [EN EPUB](books/on-regular-investing/OnRegularInvesting-en.epub) · [EN MOBI](books/on-regular-investing/OnRegularInvesting-en.mobi) | 68.0 MB | `xiaolai/regular-investing-in-box` |
| On Regular Investing (translations) | Li Xiaolai | [FR PDF](books/on-regular-investing/translations/OnRegularInvesting-fr.pdf) · [ES PDF](books/on-regular-investing/translations/OnRegularInvesting-es.pdf) · [RU PDF](books/on-regular-investing/translations/OnRegularInvesting-ru.pdf) · [JA PDF](books/on-regular-investing/translations/OnRegularInvesting-ja.pdf) | 9.5 MB | `xiaolai/regular-investing-in-box` |
| Regular Investing: A Veteran's Discipline | Li Xiaolai | [中文 PDF](books/on-regular-investing/DingTou-Dala-Ziwo-Xiuyang.pdf) | 2.7 MB | `xiaolai/regular-investing-in-box` |
| Everybody Ought to Be Rich (1929) | John J. Raskob | [EN PDF](books/on-regular-investing/EverybodyOughtToBeRich-1929.pdf) | 846 KB | `xiaolai/regular-investing-in-box` |
| The Intelligent Investor | Benjamin Graham | [PDF](books/chinese-canon/《聪明的投资者》(美)本杰明·格雷厄姆.pdf) | 17.7 MB | `codeman008/Financial_freedom` |
| Security Analysis | Benjamin Graham & David Dodd | [PDF](books/chinese-canon/《证券分析》本杰明•格雷厄姆.pdf) | 2.3 MB | `codeman008/Financial_freedom` |
| Poor Charlie's Almanack | Peter D. Kaufman (ed.) | [PDF](books/chinese-canon/《穷查理宝典》.pdf) | 3.7 MB | `codeman008/Financial_freedom` |
| Common Stocks and Uncommon Profits | Philip Fisher | [PDF](books/chinese-canon/《怎样选择成长股》.pdf) | 5.9 MB | `codeman008/Financial_freedom` |
| Common Stocks and Uncommon Profits (full translation) | Philip Fisher | [PDF](books/chinese-canon/《怎样选择成长股最新全译版》.pdf) | 23.7 MB | `codeman008/Financial_freedom` |
| The Simplest Thing in Investing | Qiu Guolu | [PDF](books/chinese-canon/《投资中最简单的事》.pdf) | 5.5 MB | `codeman008/Financial_freedom` |
| The Most Important Thing | Howard Marks | [PDF](books/chinese-canon/《投资最重要的事》.pdf) | 18.5 MB | `codeman008/Financial_freedom` |
| Financial Statements in One Book | Xiao Xing | [PDF](books/chinese-canon/《一本书读懂财报（全新修订版）》.pdf) | 2.5 MB | `codeman008/Financial_freedom` |
| The Index Fund Guide | Yinhang Luosiding | [PDF](books/chinese-canon/《指数基金投资指南》.pdf) | 11.6 MB | `codeman008/Financial_freedom` |
| Stocks for the Long Run (5th ed.) | Jeremy Siegel | [PDF](books/chinese-canon/《股市长线法宝（原书第5版）》.pdf) | 18.1 MB | `codeman008/Financial_freedom` |
| The Art of Asset Allocation | David Darst | [PDF](books/chinese-canon/《资产配置的艺术(高清)》.pdf) | 25.4 MB | `codeman008/Financial_freedom` |
| Reminiscences of a Stock Operator | Edwin Lefèvre | [PDF](books/chinese-canon/《股票作手回忆录》.pdf) | 3.3 MB | `codeman008/Financial_freedom` |
| The Crowd: A Study of the Popular Mind | Gustave Le Bon | [PDF](books/chinese-canon/《乌合之众》古斯塔夫·勒庞.pdf) | 792 KB | `codeman008/Financial_freedom` |
| Rich Dad Poor Dad | Robert Kiyosaki | [PDF](books/chinese-canon/《富爸爸,穷爸爸》.pdf) | 728 KB | `codeman008/Financial_freedom` |
| Kira and a Dog Named Money | Bodo Schäfer | [PDF](books/chinese-canon/《小狗钱钱》.pdf) | 3.8 MB | `codeman008/Financial_freedom` |
| The Almanack of Naval Ravikant | Eric Jorgenson | [PDF](books/chinese-canon/《纳瓦尔宝典》.pdf) | 3.9 MB | `codeman008/Financial_freedom` |
| The Almanack of Naval Ravikant (alt. edition) | Eric Jorgenson | [PDF](books/chinese-canon/《纳瓦尔宝典财富和幸福指南》.pdf) | 3.0 MB | `codeman008/Financial_freedom` |

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

1. `GET /repos/{owner}/{repo}` per repo, recording `stargazers_count`, `archived`, `pushed_at`, `license`.
2. `GET /repos/{owner}/{repo}/readme` to confirm the README is reachable.
3. Book downloads resolve each path against the repo tree first; a mismatch fails loudly instead of a silent 404.
4. `data/books.json` records bytes and sha256 measured on disk, never copied from upstream metadata.

## Notes

- An earlier "30 high-star repos" list was checked entry by entry: only 10 existed, 20 returned 404, and most star counts were wrong (one repo claimed 390 stars and has 8). Every repo here was queried fresh.
- The archived `mr-karan/awesome-investing` (2.5k) is a classic but unmaintained, so it fails the not-abandoned rule.
- Four repos last pushed in 2024 still hold up; the table shows the real date.

## Disclaimer

Copyright stays with the original authors and publishers. Local copies are for personal study; buy the books. This repo is an index and an archive, not investment advice.
