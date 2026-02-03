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


def noop_out(s):
    pass


def run_instr(regs, instrs, ip, out=noop_out):
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
        elif op == 'out':
            out(reg_val(regs, rest[0]))
        else:
            raise NotImplementedError(op)
        return 1
    except ExpectedResult as e:
        raise e
    except UnexpectedResult as e:
        raise e
    except Exception as e:
        print('Instr Error', e)
        return 1


def print_instrs(instrs):
    for instr in instrs:
        print(' '.join(str(s) for s in instr))


def print_debug(i, ip, instrs, regs, debug):
    if not debug:
        return
    print(i, "=================")
    print(ip, instrs[ip], regs)
    print_instrs(instrs)
    print()


def try_run_replacement(regs, instrs, ip, repls):
    for (repl_instrs, func) in repls:
        n = len(repl_instrs)
        if repl_instrs == instrs[ip:ip+n]:
            return func(regs, instrs, ip)
    return None


def run(regs, ip, instrs, replacements=[], debug=False, out=noop_out):
    n = len(instrs)
    i = 0

    repl_map = {}
    for repl in replacements:
        repl_instrs, func = repl
        instr = repl_instrs[0]
        if instr in repl_map:
            repl_map[instr].append(repl)
        else:
            repl_map[instr] = [repl]

    while ip >= 0 and ip < n:
        print_debug(i, ip, instrs, regs, debug)
        instr = instrs[ip]
        res = None
        if instr in repl_map:
            res = try_run_replacement(regs, instrs, ip, repl_map[instr])
        if res is None:
            ip += run_instr(regs, instrs, ip, out)
        else:
            ip += res
        i += 1


def mult_instr(regs, instrs, ip):
    d = regs['d']
    b = regs['b']
    regs['a'] = d * b
    regs['c'] = 0
    regs['d'] = 0
    return 6


class ExpectedResult(Exception):
    pass


class UnexpectedResult(Exception):
    pass


def try_run(lines, initial_a):
    instrs = parse(lines)
    regs = {'a': initial_a, 'b': 0, 'c': 0, 'd': 0}
    ip = 0
    replacements = [
        ([('cpy','b','c'),('inc','a'),('dec','c'),('jnz','c',-2),('dec','d'),('jnz','d',-5)], mult_instr),
    ]

    expect = [0, 1]
    expect_idx = 0
    target_n = 10000

    def out(n):
        nonlocal expect
        nonlocal expect_idx
        nonlocal target_n
        expected = expect[expect_idx  % 2]
        if expected != n:
            raise UnexpectedResult()
        expect_idx += 1
        if target_n  == expect_idx:
            raise ExpectedResult()
    try:
        run(regs, ip, instrs, replacements, debug=False, out=out)
    except UnexpectedResult:
        return False
    except ExpectedResult:
        return True
    except Exception as e:
        print('Error', e)
    return False


def part1(lines):
    i = 0
    while True:
        if try_run(lines, i):
            return i
        i += 1


def part2(lines):
    pass


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

