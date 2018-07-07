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
        tris.append(tri_parts)

    x, y, z = zip(*tris)
    tris = x + y + z

    valid_tris = []
    for i in xrange(0, len(tris), 3):
        tri = (tris[i], tris[i + 1], tris[i + 2])
        if is_valid_triangle(*tri):
            valid_tris.append(tri)

    return len(valid_tris)


def main():
    print(solve_possible_triangles(sys.stdin.readlines()))


if __name__ == "__main__":
    main()
