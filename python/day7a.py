#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys


def main(lines):
    total = 0

    for line in map(str.strip, lines):
        is_inside = False
        found = False
        found_inside = False
        for index in range(len(line) - 3):
            char = line[index]
            if is_inside and char == ']':
                is_inside = False
                continue

            if char == '[':
                is_inside = True
                continue

            char2 = line[index + 1]
            char3 = line[index + 2]
            char4 = line[index + 3]

            if char == char4 and char2 == char3 and char != char2:
                if is_inside:
                    found_inside = True
                    break
                else:
                    found = True

        if found and not found_inside:
            total += 1

    print("Total: {}".format(total))


if __name__ == "__main__":
    main(sys.stdin.readlines())
