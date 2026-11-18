# 投资 · 金融 · Web3 学习资料库

[中文](README.md) | [English](README.en.md)

30 个资料汇总型仓库 + 21 本可下载电子书，全部按 GitHub API 核验，星数实时取值，核验日期 2026-11-18。

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
| 1 | [wilsonfreitas/awesome-quant](https://github.com/wilsonfreitas/awesome-quant) | 30.7k | 量化与金融机器学习 | 2026-11 | 量化金融最大的资源索引，书籍、论文、课程、数据源、回测框架分区清楚。清单以导航为主，代码库只是被列出来。 |
| 2 | [bitcoinbook/bitcoinbook](https://github.com/bitcoinbook/bitcoinbook) | 25.4k | 开源书与书单 | 2024-12 | 《精通比特币》第 3 版开源全文，从密码学原理讲到脚本、P2P 网络和共识，读比特币源码之前先读这本。 |
| 3 | [ethereumbook/ethereumbook](https://github.com/ethereumbook/ethereumbook) | 21.5k | 开源书与书单 | 2026-10 | 《精通以太坊》第 2 版，账户模型、EVM、合约开发、共识机制逐章拆解，配大量可运行示例。 |
| 4 | [chaozh/awesome-blockchain-cn](https://github.com/chaozh/awesome-blockchain-cn) | 18.9k | 中文学习资料 | 2024-02 | 中文区块链开发资料总汇，Fabric、以太坊、白皮书、视频课程都在里面，条目多到可以当字典查。 |
| 5 | [paperswithbacktest/awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading) | 15.4k | 量化与金融机器学习 | 2026-09 | 系统化交易的论文、书籍、博客、教程索引，按策略类型分组，适合当研究入口。 |
| 6 | [smartcontractkit/full-blockchain-solidity-course-js](https://github.com/smartcontractkit/full-blockchain-solidity-course-js) | 14k | Web3 课程与路线 | 2024-06 | Chainlink 官方的全栈 Web3 课程，32 小时大纲覆盖 Solidity、Hardhat、合约交互与部署，仓库里是课程大纲与配套资料。 |
| 7 | [OffcierCia/DeFi-Developer-Road-Map](https://github.com/OffcierCia/DeFi-Developer-Road-Map) | 10.9k | Web3 课程与路线 | 2026-11 | DeFi 开发者路线图与手册，按学习阶段列出该读的文档、该用的工具和该懂的协议。 |
| 8 | [firmai/financial-machine-learning](https://github.com/firmai/financial-machine-learning) | 8.8k | 量化与金融机器学习 | 2025-01 | 金融机器学习资源地图，论文、书籍、课程、行业调研分门别类，偏研究方法而不是产品实现。 |
| 9 | [codeman008/Financial_freedom](https://github.com/codeman008/Financial_freedom) | 8.5k | 开源书与书单 | 2026-08 | 中文投资指南仓库，附带 17 本中文投资经典 PDF。本项目 books/chinese-canon/ 下的全部文件都来自这里。 |
| 10 | [georgezouq/awesome-ai-in-finance](https://github.com/georgezouq/awesome-ai-in-finance) | 6.8k | 量化与金融机器学习 | 2026-11 | LLM 与深度学习在金融市场的资料合集，论文、讲座、书单、开源模型分开列。 |
| 11 | [xiaolai/regular-investing-in-box](https://github.com/xiaolai/regular-investing-in-box) | 6.5k | 开源书与书单 | 2026-11 | 《定投改变命运》开源全书，中英双语 PDF / EPUB / MOBI，另有法、西、俄、日四语译本。本项目 books/on-regular-investing/ 的来源。 |
| 12 | [DApp-Learning-DAO/DApp-Learning](https://github.com/DApp-Learning-DAO/DApp-Learning) | 5.8k | Web3 课程与路线 | 2026-03 | 面向开发者的 DApp 学习计划，按周分任务并配中文讲义，从合约基础走到完整项目。 |
| 13 | [thuquant/awesome-quant](https://github.com/thuquant/awesome-quant) | 5.7k | 量化与金融机器学习 | 2026-11 | 清华量化协会维护的中文量化索引，数据源、交易平台、书籍、求职信息都有覆盖。 |
| 14 | [wangzhe3224/awesome-systematic-trading](https://github.com/wangzhe3224/awesome-systematic-trading) | 5.4k | 量化与金融机器学习 | 2026-11 | 系统化交易清单，中文标注友好，覆盖股票、期货、期权、外汇、加密货币。 |
| 15 | [grananqvist/Awesome-Quant-Machine-Learning-Trading](https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading) | 4.1k | 量化与金融机器学习 | 2025-05 | 机器学习做量化交易的资源清单，按数据、特征、模型、回测四段组织。 |
| 16 | [Scanate/EthList](https://github.com/Scanate/EthList) | 3.9k | Web3 资源清单 | 2026-05 | 以太坊阅读清单，从白皮书、黄皮书到扩容与治理，给出了必读顺序。 |
| 17 | [FrancescoXX/free-Web3-resources](https://github.com/FrancescoXX/free-Web3-resources) | 3.7k | Web3 资源清单 | 2024-10 | 免费 Web3 学习资源清单，课程、教程、社区、工具分区收纳。 |
| 18 | [yjjnls/awesome-blockchain](https://github.com/yjjnls/awesome-blockchain) | 3.6k | Web3 资源清单 | 2026-11 | 区块链开发与应用资源清单，共识、智能合约、跨链、Layer2 分区整理。 |
| 19 | [jpantunes/awesome-cryptoeconomics](https://github.com/jpantunes/awesome-cryptoeconomics) | 1.8k | Web3 资源清单 | 2024-06 | 加密经济学研究资料，代币机制与激励设计的论文、读物、课程。 |
| 20 | [ong/awesome-decentralized-finance](https://github.com/ong/awesome-decentralized-finance) | 1.7k | Web3 资源清单 | 2026-01 | DeFi 协议与项目清单，按借贷、DEX、衍生品、稳定币分类。 |
| 21 | [fltenwall/web3-awesome](https://github.com/fltenwall/web3-awesome) | 1.4k | Web3 资源清单 | 2024-11 | 中文 Web3 百科，概念、赛道、工具按主题整理，适合建立整体地图。 |
| 22 | [JumpCrypto/crypto-reading-list](https://github.com/JumpCrypto/crypto-reading-list) | 1.4k | Web3 资源清单 | 2024-08 | Jump Crypto 维护的加密阅读清单，偏研究与机制设计，收录的多是原始文献。 |
| 23 | [0voice/Awesome-QuantDev-Learn](https://github.com/0voice/Awesome-QuantDev-Learn) | 1.2k | 量化与金融机器学习 | 2025-07 | 量化开发的学习路线，从数据获取、因子构建、回测系统到实盘部署的知识地图。 |
| 24 | [steven2358/awesome-blockchain-ai](https://github.com/steven2358/awesome-blockchain-ai) | 1.2k | Web3 资源清单 | 2026-02 | 区块链与 AI 结合的项目与论文清单，偏技术方向调研。 |
| 25 | [itgoyo/awesome-crypto](https://github.com/itgoyo/awesome-crypto) | 1.1k | Web3 资源清单 | 2026-10 | 中文币圈资源导航，交易所、钱包、链上工具、NFT 与学习资料一处集中。 |
| 26 | [shi-rudo/awesome-stock-trading](https://github.com/shi-rudo/awesome-stock-trading) | 946 | 股票交易资源 | 2026-10 | 股票交易者资源清单，工具、网站、书籍三类，条目精简。 |
| 27 | [bekatom/awesome-ethereum](https://github.com/bekatom/awesome-ethereum) | 910 | Web3 资源清单 | 2026-10 | 以太坊生态资源清单，开发工具、学习材料、社区入口都有。 |
| 28 | [ahmet/awesome-web3](https://github.com/ahmet/awesome-web3) | 909 | Web3 资源清单 | 2026-11 | Web3 资源、库与工具清单，条目按用途分组，入门友好。 |
| 29 | [SoYuCry/awesome-quant-interview](https://github.com/SoYuCry/awesome-quant-interview) | 909 | 量化与金融机器学习 | 2026-08 | 量化面试八股文，55 个高频考点配详解，覆盖数学统计、编程、因子与机器学习。 |
| 30 | [imbaniac/awesome-blockchain](https://github.com/imbaniac/awesome-blockchain) | 895 | Web3 资源清单 | 2024-04 | 区块链服务与交易所清单，偏应用层导航，不含协议实现。 |

分类分布：量化与金融机器学习 9 个，Web3 资源清单 10 个，开源书与书单 4 个，中文学习资料 4 个，Web3 课程与路线 2 个，股票交易资源 1 个。中文资料的绝对数量比英文少，这是 GitHub 的现状，不是筛选偏向。

## 本地书库

共 21 本、29 个文件、231.3 MB。中文经典来自 `codeman008/Financial_freedom`，《定投改变命运》中英双语加四语译本来自 `xiaolai/regular-investing-in-box`。

| 书名 | 作者 | 格式 | 大小 | 来源仓库 |
|------|------|------|------|----------|
| 定投改变命运 | 李笑来 | [中文 PDF](books/on-regular-investing/OnRegularInvesting-zh.pdf) · [中文 EPUB](books/on-regular-investing/OnRegularInvesting-zh.epub) · [中文 MOBI](books/on-regular-investing/OnRegularInvesting-zh.mobi) · [EN PDF](books/on-regular-investing/OnRegularInvesting-en.pdf) · [EN EPUB](books/on-regular-investing/OnRegularInvesting-en.epub) · [EN MOBI](books/on-regular-investing/OnRegularInvesting-en.mobi) | 68.0 MB | `xiaolai/regular-investing-in-box` |
| 定投改变命运（多语言译本） | 李笑来 | [FR PDF](books/on-regular-investing/translations/OnRegularInvesting-fr.pdf) · [ES PDF](books/on-regular-investing/translations/OnRegularInvesting-es.pdf) · [RU PDF](books/on-regular-investing/translations/OnRegularInvesting-ru.pdf) · [JA PDF](books/on-regular-investing/translations/OnRegularInvesting-ja.pdf) | 9.5 MB | `xiaolai/regular-investing-in-box` |
| 定投——大佬的自我修养 | 李笑来 | [中文 PDF](books/on-regular-investing/DingTou-Dala-Ziwo-Xiuyang.pdf) | 2.7 MB | `xiaolai/regular-investing-in-box` |
| 人人都该富有（1929） | 约翰·拉斯科布 | [EN PDF](books/on-regular-investing/EverybodyOughtToBeRich-1929.pdf) | 846 KB | `xiaolai/regular-investing-in-box` |
| 聪明的投资者 | 本杰明·格雷厄姆 | [PDF](books/chinese-canon/《聪明的投资者》(美)本杰明·格雷厄姆.pdf) | 17.7 MB | `codeman008/Financial_freedom` |
| 证券分析 | 本杰明·格雷厄姆 / 戴维·多德 | [PDF](books/chinese-canon/《证券分析》本杰明•格雷厄姆.pdf) | 2.3 MB | `codeman008/Financial_freedom` |
| 穷查理宝典 | 彼得·考夫曼 编 | [PDF](books/chinese-canon/《穷查理宝典》.pdf) | 3.7 MB | `codeman008/Financial_freedom` |
| 怎样选择成长股 | 菲利普·费雪 | [PDF](books/chinese-canon/《怎样选择成长股》.pdf) | 5.9 MB | `codeman008/Financial_freedom` |
| 怎样选择成长股（最新全译版） | 菲利普·费雪 | [PDF](books/chinese-canon/《怎样选择成长股最新全译版》.pdf) | 23.7 MB | `codeman008/Financial_freedom` |
| 投资中最简单的事 | 邱国鹭 | [PDF](books/chinese-canon/《投资中最简单的事》.pdf) | 5.5 MB | `codeman008/Financial_freedom` |
| 投资最重要的事 | 霍华德·马克斯 | [PDF](books/chinese-canon/《投资最重要的事》.pdf) | 18.5 MB | `codeman008/Financial_freedom` |
| 一本书读懂财报 | 肖星 | [PDF](books/chinese-canon/《一本书读懂财报（全新修订版）》.pdf) | 2.5 MB | `codeman008/Financial_freedom` |
| 指数基金投资指南 | 银行螺丝钉 | [PDF](books/chinese-canon/《指数基金投资指南》.pdf) | 11.6 MB | `codeman008/Financial_freedom` |
| 股市长线法宝（第5版） | 杰里米·西格尔 | [PDF](books/chinese-canon/《股市长线法宝（原书第5版）》.pdf) | 18.1 MB | `codeman008/Financial_freedom` |
| 资产配置的艺术 | 戴维·达斯特 | [PDF](books/chinese-canon/《资产配置的艺术(高清)》.pdf) | 25.4 MB | `codeman008/Financial_freedom` |
| 股票作手回忆录 | 埃德温·勒菲弗 | [PDF](books/chinese-canon/《股票作手回忆录》.pdf) | 3.3 MB | `codeman008/Financial_freedom` |
| 乌合之众 | 古斯塔夫·勒庞 | [PDF](books/chinese-canon/《乌合之众》古斯塔夫·勒庞.pdf) | 792 KB | `codeman008/Financial_freedom` |
| 富爸爸，穷爸爸 | 罗伯特·清崎 | [PDF](books/chinese-canon/《富爸爸,穷爸爸》.pdf) | 728 KB | `codeman008/Financial_freedom` |
| 小狗钱钱 | 博多·舍费尔 | [PDF](books/chinese-canon/《小狗钱钱》.pdf) | 3.8 MB | `codeman008/Financial_freedom` |
| 纳瓦尔宝典 | 埃里克·乔根森 | [PDF](books/chinese-canon/《纳瓦尔宝典》.pdf) | 3.9 MB | `codeman008/Financial_freedom` |
| 纳瓦尔宝典：财富和幸福指南 | 埃里克·乔根森 | [PDF](books/chinese-canon/《纳瓦尔宝典财富和幸福指南》.pdf) | 3.0 MB | `codeman008/Financial_freedom` |

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

1. 逐个调用 `GET /repos/{owner}/{repo}`，记录 `stargazers_count`、`archived`、`pushed_at`、`license`。
2. 调用 `GET /repos/{owner}/{repo}/readme`，确认 README 可访问。
3. 下载书籍时先比对仓库文件树，路径对不上就报错，不会静默 404。
4. 下载完成后按磁盘上的真实字节数与 sha256 写入 `data/books.json`，不抄上游元数据。

## 说明

- 上一版有人给过一份「30 个高星仓库」清单，逐条核验后只有 10 个真实存在，其余 20 个返回 404，星数也普遍对不上（例如某仓库标 390 星，实际 8 星）。这份 README 里每一个仓库都是现查的。
- 已归档的 `mr-karan/awesome-investing`（2.5k）经典但停更，按「不废弃」标准没有收录。
- 有 4 个仓库最后更新停在 2024 年，内容仍有效，表中照实标注日期。

## 免责声明

资料版权归各仓库原作者与出版方所有，本地副本仅供个人学习，请支持正版。仓库只做索引与归档，不构成任何投资建议。
