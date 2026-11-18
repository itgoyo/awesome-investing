# 投资学习手册

[中文](README.md) | [English](README.en.md)

八章判断框架，21 本本地藏书，一个能搜索的双语页面。这里没有链接清单，只有从几十份开源资料里拆出来、重写过的内容。

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
| [01 投资的收益来源](content/01-foundation.md) | 先弄清钱是谁赚的，再谈方法。收益的三个来源、你能控制的三件事、beta 与 alpha 的分界。 | 2 |
| [02 读财报：排除法](content/02-statements.md) | 三张表的勾稽、经营现金流与自由现金流、杜邦分解看穿高 ROE、六个红旗。 | 1 |
| [03 估值与安全边际](content/03-valuation.md) | 四把尺子各自的适用边界，DCF 为什么只能给区间，安全边际该留多厚。 | 4 |
| [04 资产配置与定投](content/04-allocation.md) | 先定股债比例再挑产品，再平衡的纪律，定投的真实数学与三个幻觉，三个隐性成本。 | 6 |
| [05 心理与骗局](content/05-psychology.md) | 六个反复出现的偏差，骗局的五段式结构，话术翻译表，以及畅销书该信哪一半。 | 5 |
| [06 量化的边界](content/06-quant.md) | 回测的四个坑、因子衰减与容量、机器学习在金融里为什么难，以及为什么这里不收藏策略代码。 | 0 |
| [07 Web3 与加密资产](content/07-web3.md) | 技术层解决了什么，经济层收益从谁来，DeFi 收益的四类拆解，五类骗局与六问尽调。 | 0 |
| [08 建立自己的研究系统](content/08-system.md) | 信息分层、三层笔记、决策日志、复盘节奏、年度七问。 | 2 |

## 本地书库

21 本，29 个文件，231.3 MB。每本都写了「读它解决什么问题」，也写了它的局限。

| 书名 | 作者 | 一句话 | 格式 | 大小 |
|------|------|--------|------|------|
| 定投改变命运 | 李笑来 | 把定投从操作讲成认知，适合作为第一本，中英双语任选。 | [ZH PDF](books/on-regular-investing/OnRegularInvesting-zh.pdf) · [ZH EPUB](books/on-regular-investing/OnRegularInvesting-zh.epub) · [ZH MOBI](books/on-regular-investing/OnRegularInvesting-zh.mobi) · [EN PDF](books/on-regular-investing/OnRegularInvesting-en.pdf) · [EN EPUB](books/on-regular-investing/OnRegularInvesting-en.epub) · [EN MOBI](books/on-regular-investing/OnRegularInvesting-en.mobi) | 68.0 MB |
| 定投改变命运（多语言译本） | 李笑来 | 同一本书的法、西、俄、日译本，用来对照术语，不必通读。 | [FR PDF](books/on-regular-investing/translations/OnRegularInvesting-fr.pdf) · [ES PDF](books/on-regular-investing/translations/OnRegularInvesting-es.pdf) · [RU PDF](books/on-regular-investing/translations/OnRegularInvesting-ru.pdf) · [JA PDF](books/on-regular-investing/translations/OnRegularInvesting-ja.pdf) | 9.5 MB |
| 定投——大佬的自我修养 | 李笑来 | 短讲义，一小时读完，先看它再决定要不要读全书。 | [ZH PDF](books/on-regular-investing/DingTou-Dala-Ziwo-Xiuyang.pdf) | 2.7 MB |
| 人人都该富有（1929） | 约翰·拉斯科布 | 1929 年的原始短文，定投思想的历史起点，读三页就够。 | [EN PDF](books/on-regular-investing/EverybodyOughtToBeRich-1929.pdf) | 846 KB |
| 聪明的投资者 | 本杰明·格雷厄姆 | 安全边际与市场先生，价值投资的语法书，重点在第八、二十章。 | [PDF](books/chinese-canon/《聪明的投资者》(美)本杰明·格雷厄姆.pdf) | 17.7 MB |
| 证券分析 | 本杰明·格雷厄姆 / 戴维·多德 | 比《聪明的投资者》更硬，当工具书查阅，不建议通读。 | [PDF](books/chinese-canon/《证券分析》本杰明•格雷厄姆.pdf) | 2.3 MB |
| 穷查理宝典 | 彼得·考夫曼 编 | 多元思维模型与逆向思考，读演讲部分即可，其余是编排。 | [PDF](books/chinese-canon/《穷查理宝典》.pdf) | 3.7 MB |
| 怎样选择成长股 | 菲利普·费雪 | 十五要点是一份可执行的问清单，成长股研究的原始框架。 | [PDF](books/chinese-canon/《怎样选择成长股》.pdf) | 5.9 MB |
| 怎样选择成长股（最新全译版） | 菲利普·费雪 | 同一本书的全译本，与前一本二选一，译文更完整。 | [PDF](books/chinese-canon/《怎样选择成长股最新全译版》.pdf) | 23.7 MB |
| 投资中最简单的事 | 邱国鹭 | 本土案例最多，讲行业格局与定价权，比翻译书更贴近 A 股。 | [PDF](books/chinese-canon/《投资中最简单的事》.pdf) | 5.5 MB |
| 投资最重要的事 | 霍华德·马克斯 | 周期、风险、第二层思维，备忘录体的典范，适合反复翻。 | [PDF](books/chinese-canon/《投资最重要的事》.pdf) | 18.5 MB |
| 一本书读懂财报 | 肖星 | 中文财报入门最省时间的一本，读完能看懂三张表的关系。 | [PDF](books/chinese-canon/《一本书读懂财报（全新修订版）》.pdf) | 2.5 MB |
| 指数基金投资指南 | 银行螺丝钉 | 指数基金的估值与定投实操，工具性强，注意成书较早。 | [PDF](books/chinese-canon/《指数基金投资指南》.pdf) | 11.6 MB |
| 股市长线法宝（第5版） | 杰里米·西格尔 | 用两百年数据看长期收益来源，专治短期焦虑。 | [PDF](books/chinese-canon/《股市长线法宝（原书第5版）》.pdf) | 18.1 MB |
| 资产配置的艺术 | 戴维·达斯特 | 资产配置的教科书式综述，图表多，适合当手册查。 | [PDF](books/chinese-canon/《资产配置的艺术(高清)》.pdf) | 25.4 MB |
| 股票作手回忆录 | 埃德温·勒菲弗 | 交易者心理的经典叙事，当故事读，别当方法学。 | [PDF](books/chinese-canon/《股票作手回忆录》.pdf) | 3.3 MB |
| 乌合之众 | 古斯塔夫·勒庞 | 1895 年的观察随笔，取其直觉，弃其论断，它不是实验研究。 | [PDF](books/chinese-canon/《乌合之众》古斯塔夫·勒庞.pdf) | 792 KB |
| 富爸爸，穷爸爸 | 罗伯特·清崎 | 现金流思维的入门读物，核心一句值得记，操作建议有过时之处。 | [PDF](books/chinese-canon/《富爸爸,穷爸爸》.pdf) | 728 KB |
| 小狗钱钱 | 博多·舍费尔 | 给孩子或零基础的人，讲储蓄、目标与延迟满足。 | [PDF](books/chinese-canon/《小狗钱钱》.pdf) | 3.8 MB |
| 纳瓦尔宝典 | 埃里克·乔根森 | 讲财富与幸福的关系，偏观念，不含可执行方法。 | [PDF](books/chinese-canon/《纳瓦尔宝典》.pdf) | 3.9 MB |
| 纳瓦尔宝典：财富和幸福指南 | 埃里克·乔根森 | 同书的另一版本，内容高度重复，与前一本选一即可。 | [PDF](books/chinese-canon/《纳瓦尔宝典财富和幸福指南》.pdf) | 3.0 MB |

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
