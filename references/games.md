# 玩法与来源 · Game catalog and sources

| 发行方 / Operator | 玩法 / Game | CLI | 单式号码 / Single entry |
|---|---|---|---|
| 体彩 / Sports | 超级大乐透 / Super Lotto | dlt | 前区 01–35 选 5，后区 01–12 选 2；区内不重复 / Distinct within each pool |
| 体彩 / Sports | 7星彩 / 7-Star | qxc | 前六位各为 0–9，末位为 00–14；按位置 / Six ordered digits and one terminal value |
| 体彩 / Sports | 排列3 / Pick 3 | pl3 | 三位各为 0–9；支持直选、组选三、组选六 / Direct and two group modes |
| 体彩 / Sports | 排列5 / Pick 5 | pl5 | 五位各为 0–9，按位置 / Five ordered digits |
| 福彩 / Welfare | 双色球 / Double Color Ball | ssq | 红球 01–33 选 6，蓝球 01–16 选 1；区内不重复 / Distinct within each pool |
| 福彩 / Welfare | 福彩3D / Welfare 3D | fc3d | 三位各为 0–9；支持直选、组选三、组选六 / Direct and two group modes |
| 福彩 / Welfare | 七乐彩 / Seven Lotto | qlc | 01–30 选 7；特别号码是开奖字段，投注时不用另选 / Pick seven; no separate bonus pick |
| 福彩 / Welfare | 快乐8 / Happy 8 | kl8 | 从 01–80 不重复选 1 至 10；明确具体玩法 / Choose 1–10 distinct balls |

- 体彩：[玩法目录](https://m.lottery.gov.cn/zs/wfjs/) · [大乐透规则](https://m.lottery.gov.cn/ksjz/m/yxgz_dlt/) · [历史号码](https://m.lottery.gov.cn/zst/tbsj/)。
- 福彩：[中国福彩网](https://www.cwl.gov.cn/) · [官方玩法说明](https://www.cwl.gov.cn/upload/resources/file/2021/07/26/806575.pdf) · [规则变更公告入口](https://www.cwl.gov.cn/gzdt/gsld/)。早期报告用于理解玩法结构；按目标期最新公告核对规则。
- 选号脚本按每注基础 2 元估算，大乐透追加按每注共 3 元。它不内置派奖、奖级或销售截止时间。 / The script estimates 2 CNY per base entry or 3 CNY per Super Lotto add-on entry; it does not encode promotions, prize tiers or closing times.
- 直选定位；组三恰有两位同号，组六三位互异。组选号码按升序显示，不能按直选票核奖。 / Direct bets are ordered; Group 3 has exactly one repeated pair; Group 6 has all distinct digits. Group output is sorted.
- 复式：独立号码池分别计算二项式系数 C(备选数, 每注所需数)，再相乘；位置型复式按各位置的候选数相乘。胆拖：对使用胆拖的池计算 C(拖码数, 每注所需数−胆码数)，并与其他池注数相乘。核对各区胆码与拖码无交集，并查该玩法是否允许所用格式及注数限制。 / For pools, multiply the combination counts. With bankers, subtract the fixed banker count from the required picks before choosing from the remaining pool. For positional bets, multiply candidate counts per position. Verify exact game constraints before calculating a ticket.
- 传统足彩、竞彩、北京单场及其他地方彩：确认发行机构、省份、期号或赛事日期；核对官方销售状态、在售场次及可选结果。给定有效选项后才可整理方案，不凭空补齐。 / For sports pools and regional games, confirm issuer, region and active slate before listing selections.
- 即开票（如顶呱刮、刮刮乐）：只查询官方票种、面额和公开规则，无可由本脚本生成的投注号码。 / Scratch games are informational only; there is no number entry to generate.
