<div align="center">

# 投资学习手册

**八章判断框架 · 21 本本地藏书 · 231.3 MB 离线可读**

资料不缺，缺的是筛选。这里没有仓库名录，只有拆开、重写过的判断标准。

[在线阅读](index.html) · [English](README.en.md) · [书库](#书库) · [版权声明](NOTICE.md)

![chapters](https://img.shields.io/badge/chapters-8-e0b155?style=flat-square)
![books](https://img.shields.io/badge/books-21-e0b155?style=flat-square)
![files](https://img.shields.io/badge/files-29-e0b155?style=flat-square)
![size](https://img.shields.io/badge/size-231.3%20MB-e0b155?style=flat-square)

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

[按问题查](#按问题查) | [书库](#书库) | [术语速查](#术语速查) | [骗局速查](#骗局速查) | [常见问题](#常见问题) | [取舍说明](#取舍说明) | [使用与构建](#使用与构建) | [交易所与社群](#交易所与社群) | [声明](#声明)

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

21 本，29 个文件，231.3 MB。全部已存进 `books/`，点书名直接下载，不依赖外链。每本标了「读它解决什么问题」，也标了它的局限。

**分类**：[定投](#定投) · [价值投资](#价值投资) · [财报分析](#财报分析) · [指数基金](#指数基金) · [资产配置](#资产配置) · [市场史](#市场史) · [投资心理](#投资心理) · [理财入门](#理财入门)

### 定投

> 先把「长期买同一件事」想清楚，再谈买什么。

- [定投改变命运](books/on-regular-investing/OnRegularInvesting-zh.pdf) - 李笑来 · 68.0 MB · 中文 PDF。把定投从操作讲成认知，适合作为第一本，中英双语任选。
  - 其他格式：[中文 EPUB](books/on-regular-investing/OnRegularInvesting-zh.epub) · [中文 MOBI](books/on-regular-investing/OnRegularInvesting-zh.mobi) · [EN PDF](books/on-regular-investing/OnRegularInvesting-en.pdf) · [EN EPUB](books/on-regular-investing/OnRegularInvesting-en.epub) · [EN MOBI](books/on-regular-investing/OnRegularInvesting-en.mobi)
- [定投改变命运（多语言译本）](books/on-regular-investing/translations/OnRegularInvesting-fr.pdf) - 李笑来 · 9.5 MB · FR PDF。同一本书的法、西、俄、日译本，用来对照术语，不必通读。
  - 其他格式：[ES PDF](books/on-regular-investing/translations/OnRegularInvesting-es.pdf) · [RU PDF](books/on-regular-investing/translations/OnRegularInvesting-ru.pdf) · [JA PDF](books/on-regular-investing/translations/OnRegularInvesting-ja.pdf)
- [定投——大佬的自我修养](books/on-regular-investing/DingTou-Dala-Ziwo-Xiuyang.pdf) - 李笑来 · 2.7 MB · 中文 PDF。短讲义，一小时读完，先看它再决定要不要读全书。

### 价值投资

> 安全边际、能力圈、周期。整套框架的地基。

- [聪明的投资者](books/chinese-canon/《聪明的投资者》%28美%29本杰明·格雷厄姆.pdf) - 本杰明·格雷厄姆 · 17.7 MB · PDF。安全边际与市场先生，价值投资的语法书，重点在第八、二十章。
- [证券分析](books/chinese-canon/《证券分析》本杰明•格雷厄姆.pdf) - 本杰明·格雷厄姆 / 戴维·多德 · 2.3 MB · PDF。比《聪明的投资者》更硬，当工具书查阅，不建议通读。
- [穷查理宝典](books/chinese-canon/《穷查理宝典》.pdf) - 彼得·考夫曼 编 · 3.7 MB · PDF。多元思维模型与逆向思考，读演讲部分即可，其余是编排。
- [怎样选择成长股](books/chinese-canon/《怎样选择成长股》.pdf) - 菲利普·费雪 · 5.9 MB · PDF。十五要点是一份可执行的问清单，成长股研究的原始框架。
- [怎样选择成长股（最新全译版）](books/chinese-canon/《怎样选择成长股最新全译版》.pdf) - 菲利普·费雪 · 23.7 MB · PDF。同一本书的全译本，与前一本二选一，译文更完整。
- [投资中最简单的事](books/chinese-canon/《投资中最简单的事》.pdf) - 邱国鹭 · 5.5 MB · PDF。本土案例最多，讲行业格局与定价权，比翻译书更贴近 A 股。
- [投资最重要的事](books/chinese-canon/《投资最重要的事》.pdf) - 霍华德·马克斯 · 18.5 MB · PDF。周期、风险、第二层思维，备忘录体的典范，适合反复翻。

### 财报分析

> 目标只是排除坏公司，不必成为会计。

- [一本书读懂财报](books/chinese-canon/《一本书读懂财报（全新修订版）》.pdf) - 肖星 · 2.5 MB · PDF。中文财报入门最省时间的一本，读完能看懂三张表的关系。

### 指数基金

> 承认选不出个股时的默认答案。

- [指数基金投资指南](books/chinese-canon/《指数基金投资指南》.pdf) - 银行螺丝钉 · 11.6 MB · PDF。指数基金的估值与定投实操，工具性强，注意成书较早。

### 资产配置

> 决定长期结果的大部分，比选股重要。

- [股市长线法宝（第5版）](books/chinese-canon/《股市长线法宝（原书第5版）》.pdf) - 杰里米·西格尔 · 18.1 MB · PDF。用两百年数据看长期收益来源，专治短期焦虑。
- [资产配置的艺术](books/chinese-canon/《资产配置的艺术%28高清%29》.pdf) - 戴维·达斯特 · 25.4 MB · PDF。资产配置的教科书式综述，图表多，适合当手册查。

### 市场史

> 用长周期数据压住短期情绪。

- [人人都该富有（1929）](books/on-regular-investing/EverybodyOughtToBeRich-1929.pdf) - 约翰·拉斯科布 · 846 KB · EN PDF。1929 年的原始短文，定投思想的历史起点，读三页就够。
- [股票作手回忆录](books/chinese-canon/《股票作手回忆录》.pdf) - 埃德温·勒菲弗 · 3.3 MB · PDF。交易者心理的经典叙事，当故事读，别当方法学。

### 投资心理

> 知道偏差存在，比「克服」更现实。

- [乌合之众](books/chinese-canon/《乌合之众》古斯塔夫·勒庞.pdf) - 古斯塔夫·勒庞 · 792 KB · PDF。1895 年的观察随笔，取其直觉，弃其论断，它不是实验研究。

### 理财入门

> 给零基础的人，也给孩子。

- [富爸爸，穷爸爸](books/chinese-canon/《富爸爸,穷爸爸》.pdf) - 罗伯特·清崎 · 728 KB · PDF。现金流思维的入门读物，核心一句值得记，操作建议有过时之处。
- [小狗钱钱](books/chinese-canon/《小狗钱钱》.pdf) - 博多·舍费尔 · 3.8 MB · PDF。给孩子或零基础的人，讲储蓄、目标与延迟满足。
- [纳瓦尔宝典](books/chinese-canon/《纳瓦尔宝典》.pdf) - 埃里克·乔根森 · 3.9 MB · PDF。讲财富与幸福的关系，偏观念，不含可执行方法。
- [纳瓦尔宝典：财富和幸福指南](books/chinese-canon/《纳瓦尔宝典财富和幸福指南》.pdf) - 埃里克·乔根森 · 3.0 MB · PDF。同书的另一版本，内容高度重复，与前一本选一即可。

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

## 常见问题

**为什么没有策略代码？** 代码会过期，且回测好看与实盘赚钱之间隔着交易成本、滑点和容量。第 06 章给的是判断边界，让你看到漂亮曲线时知道该问什么。

**为什么不推荐具体标的？** 标的的信息半衰期以周计，写进来第二天就失效。给框架比给名单有用。

**为什么第 06、07 章没有配套书？** 中文世界缺少写得好的量化与 Web3 入门书，市面上多是策略集合或项目喊单。硬凑一本，不如不凑。

**书能转载或商用吗？** 不能。书库文件版权归原作者与出版方，本仓库只做本地归档。详见 [NOTICE.md](NOTICE.md)。

**为什么删掉了仓库名录？** 表格不产生理解，读者还是要一个个点开。这一版把内容拆开重写，来源只保留在版权声明里。

**会更新吗？** 章节内容相对稳定，书库按需补充。页面与 README 由同一份数据生成，改一处两边同步。

## 取舍说明

**只留机制。** 凡是讲不清收益来源、无法证伪、或者靠「相信我」成立的说法，都没有进正文。留下的部分是能拿去检验的：六个红旗可以对着报表逐条打勾，尽调六问可以对着项目逐条追问。

**具体删了什么。** 策略代码与交易信号全删，会过期。标的推荐全删，半衰期太短。鸡汤段落全删，不产生判断力。畅销书没有照单全收：《乌合之众》是 1895 年的观察随笔而非实验研究，《富爸爸穷爸爸》只留现金流那一句并注明操作建议过时，《纳瓦尔宝典》注明它讲观念、不含方法。

**页面是同一份内容的另一种读法。** `index.html` 带章节侧栏、全文搜索、按格式下载，中英一键切换。README 是它的索引版。

## 使用与构建

把仓库下载到本地，双击 `index.html` 即可：中英切换、搜索、按格式下载都能用，不需要起服务。在 GitHub 网页上点它会显示源码，这是正常的。

重新生成：

```bash
python3 scripts/fetch_books.py    # 校验并补齐书库文件
python3 scripts/build_site.py     # 生成页面数据
python3 scripts/build_readme.py   # 渲染两份 README
```

## 交易所与社群

这一节是仓库的入口信息，与前面八章无关。链接含邀请码，通过它们注册能减免手续费，仓库也会拿到少量返佣；这不会改变正文里的任何判断。

加密资产交易在部分司法辖区受限，请先确认所在地法规。本金可能全部损失，任何平台的「活动」「空投」都不构成收益承诺。

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

**关于「手续费减免 20%」。** 比例与活动规则由平台随时调整，以注册页实际显示为准。邀请码只在注册时生效，注册后再补填无效。

## 声明

内容为学习框架，不构成投资建议。市场有风险，任何框架都不能替代你自己的判断。书库文件版权归原作者与出版方所有，详见 [NOTICE.md](NOTICE.md)。

<div align="center">

[回到顶部](#投资学习手册) · [English](README.en.md) · [在线阅读](index.html)

</div>
