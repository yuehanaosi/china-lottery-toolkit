---
name: china-lottery-toolkit
description: 中国体彩与福彩选号、历期开奖核验、号码走势统计、玩法辨别和预算核算；适用于大乐透、双色球、7星彩、排列3/5、福彩3D、快乐8、七乐彩。 Generate and validate China Sports and Welfare Lottery picks, verify official draws, analyze historical number trends, and calculate ticket costs.
---

# 中国彩票研究与选号工具箱：体彩、福彩、历期开奖、号码走势与预算核算

## China Lottery Research & Pick Toolkit for Sports and Welfare Lottery Draws, Number Trends and Budget Checks

**技能 SKU / Skill SKU** · `CLT-CN-001`

一套技能，覆盖全国联销的体彩与福彩乐透、数字和基诺选号，并为地方彩、赛事竞猜和即开票提供核验入口。
One toolkit for nationwide Sports and Welfare Lottery picks, with verification workflows for regional games, sports pools and scratch tickets.

1. **认准玩法 / Resolve the game.** Read [game catalog](references/games.md). “五星” can mean 体彩排列5 informally or a five-position bet in another game. If context does not resolve it, ask which official game and province; never substitute silently. For 快乐8, state the requested pick size or say that the default is 选十. In PL3 and FC3D, default to 直选 and label group selections explicitly.
2. **生成可用号码 / Generate valid picks.** Run `python3 scripts/pick.py <game> -n <count> --summary` from this skill's directory. Use `--budget` for an explicit cap, `--add-on` only for 大乐透, `-k` for 快乐8 and `--mode group3|group6` for the relevant three-digit games. When no count or budget is specified, use five single entries and report the total. Do not silently trim requests exceeding the budget; state the largest affordable count. The script is offline and creates no transactions.
3. **核对数据 / Verify live facts.** For latest draws, historical analysis, availability, deadlines or checking tickets, use the official source for that draw or policy. State the issue number, draw date and source URL; if inaccessible, disclose that and avoid inventing values. For statistics, record the covered issues, sample size and missing periods. Frequency, omission, consecutive numbers and balance may describe past draws or filter candidate picks; they do not improve the per-entry odds of a fair draw.
4. **按要求交付 / Deliver in the requested format.** One entry per line, no tables or parallel columns for picks. Pad lottery ball numbers to two digits, keep positional digits in order with leading zeroes, and use `+` between separate zones. Keep the amount, issue context and brief risk statement outside the pick list. Use the user's language.
5. **复式、胆拖及其他彩种 / Expanded bets and other games.** Follow the [calculation and routing notes](references/games.md). Verify current official rules before claiming a ticket can be purchased, checking prizes, or quoting official odds. Do not generate arbitrary fixture identifiers, match markets or scratch ticket serial numbers. Do not buy or place bets.

每组同类合法单式组合在公平开奖中的理论概率相同。只在事先设定的娱乐预算内考虑参与，不追损。
In a fair draw, like-for-like valid entries have equal theoretical odds. Set a fixed entertainment budget and avoid chasing losses.
