#!/usr/bin/env python

import sys


def add(p, m):
    return (p[0] + m[0], p[1] + m[1])


def code_to_dir(code):
    if code == "U":
        return (0, -1)
    elif code == "D":
        return (0, 1)
    elif code == "L":
        return (-1, 0)
    elif code == "R":
        return (1, 0)


def solve_bathroom_code(lines):
    buttons = {
        (2, 0): '1',
        (1, 1): '2', (2, 1): '3', (3, 1): '4',
        (0, 2): '5', (1, 2): '6', (2, 2): '7', (3, 2): '8', (4, 2): '9',
        (1, 3): 'A', (2, 3): 'B', (3, 3): 'C',
        (2, 4): 'D',
    }

    pos = (1, 1)
    instr = []

    for line in lines:
        line = line.strip()
        if line == "":
            break

        for c in list(line):
            move_dir = code_to_dir(c)
            next_pos = add(pos, move_dir)

            if next_pos in buttons:
                pos = next_pos

        instr.append(buttons[pos])

    return "".join(map(str, instr))


def main():
    print(solve_bathroom_code(sys.stdin.readlines()))


if __name__ == "__main__":
    main()
