#!/usr/bin/env python

import os
import sys


def add(pos, step):
    return (pos[0] + step[0], pos[1] + step[1])


def turn(cur_dir, left):
    if cur_dir == (0, 1): # up
        if left:
            return (-1, 0)
        else:
            return (1, 0)
    elif cur_dir == (0, -1): # down
        if left:
            return (1, 0)
        else:
            return (-1, 0)
    elif cur_dir == (1, 0): # right
        if left:
            return (0, 1)
        else:
            return (0, -1)
    elif cur_dir == (-1, 0): # left
        if left:
            return (0, -1)
        else:
            return (0, 1)

    raise Exception("wrong turn?")


def solve_hq_steps(steps):
    pos = (0, 0)
    cur_dir = (0, 1)

    for step, count in steps:
        cur_dir = turn(cur_dir, True if step == 'L' else False)
        for _ in xrange(count):
            pos = add(pos, cur_dir)

    return abs(pos[0]) + abs(pos[1])


def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        steps = map(lambda s: (s[0], int(s[1:])), line.split(", "))
        print(solve_hq_steps(steps))


if __name__ == "__main__":
    main()
