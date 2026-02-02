#!/usr/bin/env python3

import sys
from hashlib import md5
from functools import cache


def contains_three_in_row(s):
    for i in range(0, len(s)-2):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            return s[i]
    return None


def contains_five_in_row(s):
    for i in range(0, len(s)-4):
        if s[i] == s[i+1] and s[i] == s[i+2] and s[i] == s[i+3] and s[i] == s[i+4]:
            return s[i]
    return None


def is_key(prefix, n):
    key = prefix + str(n)
    h = md5(key.encode('ascii')).hexdigest()
    c = contains_three_in_row(h);
    if c is None:
        return False
    for i in range(n+1, n+1001):
        key2 = prefix + str(i)
        h2 = md5(key2.encode('ascii')).hexdigest()
        if contains_five_in_row(h2) == c:
            return True
    return False


def part1(lines):
    prefix = lines[0]
    found = 0
    target = 64
    idx = 0
    while True:
        if is_key(prefix, idx):
            found += 1
            if found == target:
                return idx
        idx += 1

@cache
def stretched_hash(key):
    h = md5(key.encode('ascii')).hexdigest()
    for i in range(2016):
        h = md5(h.encode('ascii')).hexdigest()
    return h


def is_key2(prefix, n):
    key = prefix + str(n)
    h = stretched_hash(key)
    c = contains_three_in_row(h);
    if c is None:
        return False
    for i in range(n+1, n+1001):
        key2 = prefix + str(i)
        h2 = stretched_hash(key2)
        if contains_five_in_row(h2) == c:
            return True
    return False


def part2(lines):
    prefix = lines[0]
    found = 0
    target = 64
    idx = 0
    while True:
        if is_key2(prefix, idx):
            found += 1
            if found == target:
                return idx
        idx += 1


def main():
    lines = sys.stdin.read().strip().split("\n")
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

