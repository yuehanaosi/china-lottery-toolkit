#!/usr/bin/env python3
"""Offline single-entry generator for nationally pooled China lottery games."""
import argparse
from itertools import combinations_with_replacement
from math import comb
from random import SystemRandom

POOLS = {'ssq': ((33, 6), (16, 1)), 'dlt': ((35, 5), (12, 2)),
         'qlc': ((30, 7),), 'kl8': ((80, 10),)}
DIGITS = {'qxc': (10,) * 6 + (15,), 'pl3': (10,) * 3,
          'pl5': (10,) * 5, 'fc3d': (10,) * 3}
ALIASES = {'双色球':'ssq','大乐透':'dlt','超级大乐透':'dlt','七乐彩':'qlc',
           '快乐8':'kl8','快乐八':'kl8','七星彩':'qxc','7星彩':'qxc',
           '排列3':'pl3','排列三':'pl3','排列5':'pl5','排列五':'pl5',
           '福彩3D':'fc3d','福彩3d':'fc3d','3D':'fc3d','3d':'fc3d'}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('game', help='ssq dlt qlc kl8 qxc pl3 pl5 fc3d or Chinese name')
    p.add_argument('-n', '--count', type=int, default=5)
    p.add_argument('-k', '--pick', type=int, help='Happy 8: 1–10 numbers per entry (default 10)')
    p.add_argument('--mode', choices=('direct', 'group3', 'group6'), default='direct')
    p.add_argument('--budget', type=int, help='Maximum batch cost in whole yuan')
    p.add_argument('--add-on', action='store_true', help='Super Lotto only')
    p.add_argument('--summary', action='store_true', help='Print cost to stderr')
    a = p.parse_args()
    game = ALIASES.get(a.game, a.game.lower())
    if game not in POOLS and game not in DIGITS:
        p.error('Unknown or ambiguous game; use an explicit supported game name.')
    if a.pick is not None and (game != 'kl8' or not 1 <= a.pick <= 10):
        p.error('--pick is only for Happy 8, from 1 through 10.')
    if a.mode != 'direct' and game not in ('pl3', 'fc3d'):
        p.error('Group modes only apply to PL3 and FC3D.')
    if a.add_on and game != 'dlt':
        p.error('--add-on only applies to Super Lotto.')
    cost = a.count * (3 if a.add_on else 2)
    if not 1 <= a.count <= 1000:
        p.error('--count must be 1 through 1000.')
    if a.budget is not None and cost > a.budget:
        p.error(f'{a.count} entries cost {cost} CNY, above budget.')
    rng = SystemRandom()
    if game in POOLS:
        pools = ((80, a.pick or 10),) if game == 'kl8' else POOLS[game]
        total = 1
        for upper, k in pools:
            total *= comb(upper, k)

        def draw():
            return tuple(tuple(sorted(rng.sample(range(1, upper + 1), k))) for upper, k in pools)

        if game == 'kl8' and a.pick == 1:
            lines = [((x,),) for x in range(1, 81)]
        else:
            lines = None

        def render(row):
            return ' + '.join(' '.join(f'{x:02}' for x in zone) for zone in row)
    else:
        total = 1
        for upper in DIGITS[game]:
            total *= upper

        def draw():
            return tuple(rng.randrange(upper) for upper in DIGITS[game])

        lines = None
        if a.mode != 'direct':
            lines = [row for row in combinations_with_replacement(range(10), 3)
                     if len(set(row)) == (2 if a.mode == 'group3' else 3)]
            total = len(lines)
        elif total <= 1000:
            lines = [tuple(map(int, f'{x:03}')) for x in range(total)]

        def render(row):
            if game == 'qxc':
                return ' '.join(map(str, row[:6])) + f' + {row[-1]:02}'
            return ' '.join(map(str, row))

    if a.count > total:
        p.error(f'Only {total} distinct entries exist in this mode.')
    if lines is not None:
        rows = rng.sample(lines, a.count)
    else:
        rows, seen = [], set()
        while len(rows) < a.count:
            row = draw()
            if row not in seen:
                seen.add(row)
                rows.append(row)
    for row in rows:
        print(render(row))
    if a.summary:
        import sys
        print(f'{a.count} entries | {cost} CNY', file=sys.stderr)


if __name__ == '__main__':
    main()
