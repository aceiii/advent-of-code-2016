#!/usr/bin/env python

import sys
import re


def is_valid_triangle(a, b, c):
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True


def solve_possible_triangles(lines):
    tris = []
    for line in lines:
        line = line.strip()
        if line == "":
            break

        tri_parts = map(int, re.split("\s+", line))

        if is_valid_triangle(*tri_parts):
            tris.append(tri_parts)

    return len(tris)


def main():
    print(solve_possible_triangles(sys.stdin.readlines()))


if __name__ == "__main__":
    main()
