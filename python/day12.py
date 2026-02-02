#!/usr/bin/env python3

import sys


def try_parse_int(a):
    try:
        return int(a, 10)
    except:
        return a


def parse(lines):
    instrs = []
    for line in lines:
        parts = [try_parse_int(a) for a in line.strip().split(' ')]
        instrs.append(tuple(parts))
    return instrs


def reg_or_val(regs, a):
    if type(a) == int:
        return a
    return regs[a]


def run_instr(regs, instr):
    op, *rest = instr
    if op == 'cpy':
        a, b = rest
        regs[b] = reg_or_val(regs, a)
    elif op == 'inc':
        regs[rest[0]] += 1
    elif op == 'dec':
        regs[rest[0]] -= 1
    elif op == 'jnz':
        a, b = rest
        if reg_or_val(regs, a) != 0:
            return b
    return 1


def run(regs, ip, instrs):
    n = len(instrs)
    while ip >= 0 and ip < n:
        instr = instrs[ip]
        ip += run_instr(regs, instr)


def part1(lines):
    instrs = parse(lines)
    regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    ip = 0
    run(regs, ip, instrs)
    return regs['a']


def part2(lines):
    instrs = parse(lines)
    regs = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    ip = 0
    run(regs, ip, instrs)
    return regs['a']


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

