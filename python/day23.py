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


def reg_val(regs, a):
    if type(a) == int:
        return a
    return regs[a]


def toggle_instr(instrs, x):
    if x < 0 or x >= len(instrs):
        return
    op, *rest = instrs[x]
    if len(rest) == 1:
        instrs[x] = ('dec' if op == 'inc' else 'inc', *rest)
    else:
        instrs[x] = ('cpy' if op == 'jnz' else 'jnz', *rest)


def run_instr(regs, instrs, ip):
    try:
        op, *rest = instrs[ip]
        if op == 'cpy':
            a, b = rest
            if type(b) == str:
                regs[b] = reg_val(regs, a)
        elif op == 'inc':
            regs[rest[0]] += 1
        elif op == 'dec':
            regs[rest[0]] -= 1
        elif op == 'jnz':
            a, b = rest
            if reg_val(regs, a) != 0:
                return reg_val(regs, b)
        elif op == 'tgl':
            toggle_instr(instrs, ip + reg_val(regs, rest[0]))
        else:
            raise NotImplementedError(op)
        return 1
    except Exception as e:
        print("ERROR", e)
        return 1


def run(regs, ip, instrs):
    n = len(instrs)
    i = 0
    while ip >= 0 and ip < n:
        ip += run_instr(regs, instrs, ip)
        i += 1


def part1(lines):
    instrs = parse(lines)
    regs = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    ip = 0
    run(regs, ip, instrs)
    return regs['a']


def part2(lines):
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

