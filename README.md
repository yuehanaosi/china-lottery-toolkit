# 中国彩票全品类工作台 | China Lottery Toolkit

**两大彩票体系，一套选号工作台。** 从一组大乐透号码，到福彩、体彩多玩法的批量选号、注数和预算核算，再到官方开奖资料核验，这个 Codex Skill 把原先分散在不同玩法里的操作放在一个入口。

**Two lottery systems. One toolkit.** Generate picks across China's nationwide number games, keep total cost visible, and trace live draw and rule information back to official sources. Built for Codex, with a standalone offline command line.

- **八大玩法 / Eight game engines:** 超级大乐透、7星彩、排列3、排列5、双色球、福彩3D、七乐彩、快乐8。
- **单式批量 / Batch single entries:** 校验号码范围、位置、号码池、组别和重复注；支持快乐8选一至选十和大乐透追加。
- **预算与规则 / Budget and rules:** 可限制当次生成金额。技能提供复式、胆拖、官方数据与其他玩法的核验路径。

克隆仓库后，把仓库的技能文件放到 `~/.codex/skills/china-lottery-toolkit/`，或直接运行 Python 3 脚本。
Clone the repository and place the skill files in `~/.codex/skills/china-lottery-toolkit/`, or run the Python 3 script directly.

```sh
python3 scripts/pick.py 大乐透 -n 5 --budget 10 --summary
python3 scripts/pick.py kl8 -k 7 -n 3 --summary
python3 scripts/pick.py fc3d --mode group6 -n 4 --summary
```

Codex 示例 / Example prompt:
“用中国彩票全品类工作台按官方规则给我 5 注大乐透，预算 10 元，一注一行。”
“Use China Lottery Toolkit to generate five Double Color Ball entries, one per line, within 10 yuan.”

[技能说明 / Skill instructions](SKILL.md) · [玩法和官方来源 / Games and official sources](references/games.md)

独立项目，与彩票发行机构无隶属关系。历史走势不会提高公平开奖下单注的理论中奖概率。项目不提供购票或支付功能。
Independent project. Historical patterns do not improve per-entry odds in a fair draw. No ticket purchase or payment functionality.
