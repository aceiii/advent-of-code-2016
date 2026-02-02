#!/usr/bin/env python3

import sys


def parse(lines):
    discs = []
    for line in lines:
        parts = line = line.strip().split(' ')
        n = int(parts[3], 10)
        pos = int(parts[-1][:-1], 10)
        discs.append((n, pos))
    return discs


def sim(discs, n):
    for idx, (steps, pos) in enumerate(discs):
        if (n + pos + idx + 1) % steps != 0:
            return False
    return True


def part1(lines):
    discs = parse(lines)
    n = 0
    while True:
        if sim(discs, n):
            return n
        n += 1


def part2(lines):
    discs = parse(lines)
    discs.append((11, 0))
    n = 0
    while True:
        if sim(discs, n):
            return n
        n += 1


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

