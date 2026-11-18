<!-- zh -->

## 一句话

量化不是印钞机，是把纪律写成代码。它的价值在执行与风控，不在预测。

## 回测的四个坑

一份漂亮的回测曲线，九成问题出在这四处：

- **前视偏差**。用了当时拿不到的数据，比如用修正后的财报数据回测当年的选股。
- **幸存者偏差**。只回测今天还活着的公司，退市和暴雷的样本被悄悄剔除。
- **过拟合**。参数调到与历史完美吻合，样本外立刻失效。参数越多，越容易自欺。
- **成本忽略**。不算滑点、手续费、冲击成本，尤其在小市值和高换手策略里，成本能吃掉全部超额。

判断一份回测是否可信，先问：样本外表现如何？交易成本按多少算？参数只有几个？换一个时间段还成立吗？

## 因子会衰减

任何公开的因子，在被发表之后超额收益都会下降。原因是资金涌入，套利空间被抹平。所以"找到能长期稳定的因子"这件事本身反直觉，更现实的目标是理解因子为什么有效，以及它在什么环境下失效。

容量也是硬约束。一个策略管理一千万能赚，管理一百亿就赚不到，因为交易本身会改变价格。

## 机器学习在金融里为什么难

金融数据的信噪比极低。图像识别里信号占主导，金融里噪声占主导。样本量还特别少：一年只有两百五十个交易日，十年也只有两千五百个观测，而特征可以有几万个。

结果就是模型很容易记住噪声。样本内 AUC 零点九，样本外接近随机，是常态而不是意外。

机器学习在金融里真正靠谱的用法有三个：处理非结构化数据（文本、卫星图、票据）、做风险建模、做执行优化。用来直接预测涨跌，成功率极低。

## 为什么不收策略代码

我们看过大量高星项目，代码写得很漂亮，但共同问题是：策略与特定市场环境绑定、维护停更、没有真实资金曲线。

代码会过期，方法论不会。这份手册只保留判断标准：回测要看样本外、成本要算全、参数要少、逻辑要能一句话说清。

## 自检

如果一个策略的收益无法用一句话解释来源，它更可能是数据挖掘的产物，而不是发现。

<!-- en -->
---

## In one sentence

Quant is not a printing press. It is discipline expressed as code. Its value sits in execution and risk control, not prediction.

## Four holes in every backtest

A beautiful equity curve usually leaks in one of four places:

- **Look-ahead.** Using data that did not exist at the time, such as restated financials to pick stocks in the original year.
- **Survivorship.** Testing only companies alive today, quietly dropping the delisted and the blown-up.
- **Overfitting.** Parameters tuned until history fits perfectly, then failing immediately out of sample. More parameters, more self-deception.
- **Ignored costs.** No slippage, commission or market impact. In small caps and high-turnover strategies, costs can consume the entire excess return.

Before trusting a backtest, ask four questions. What does it do out of sample? What cost assumption? How many parameters? Does it survive a different period?

## Factors decay

Any published factor loses excess return after publication, because capital arrives and closes the gap. Finding a permanently stable factor is therefore counter-intuitive. The realistic goal is understanding why a factor works and when it stops.

Capacity binds too. A strategy that works with ten million may not work with ten billion, because the trading itself moves the price.

## Why machine learning struggles here

Financial data has an extremely low signal-to-noise ratio. In image recognition the signal dominates. Here noise does. Sample size is also tiny: two hundred fifty trading days a year, twenty-five hundred observations in a decade, against tens of thousands of features.

Models memorise noise. An in-sample AUC of 0.9 with near-random out-of-sample performance is the norm, not an accident.

Three uses of ML that do hold up: processing unstructured data such as text, satellite imagery and receipts; risk modelling; execution optimisation. Direct price prediction has a very low hit rate.

## Why this library carries no strategy code

We read a large number of popular projects. Many are elegantly written, and they share the same problems: strategies bound to one market regime, maintenance that stopped, no real capital curve.

Code expires. Method does not. What survives here is the standard: judge out of sample, count all costs, keep parameters few, and demand a one-sentence explanation of where the return comes from.

## Self-check

If the source of a strategy's return cannot be stated in one sentence, it is more likely data mining than discovery.
