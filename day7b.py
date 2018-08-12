#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys


def main(lines):
    total = 0

    for line in map(str.strip, lines):
        is_inside = False
        outside = set()
        inside = set()

        for index in range(len(line) - 2):
            char = line[index]
            if is_inside and char == ']':
                is_inside = False
                continue

            if char == '[':
                is_inside = True
                continue

            char2 = line[index + 1]
            char3 = line[index + 2]

            if char == char3 and char != char2:
                aba = "{0}{1}{0}".format(char, char2)
                if is_inside:
                    inside.add(aba)
                else:
                    outside.add(aba)

        for aba in outside:
            bab = "{0}{1}{0}".format(aba[1], aba[0])
            if bab in inside:
                print(aba, bab, outside, inside)
                total += 1
                break

    print("Total: {}".format(total))


if __name__ == "__main__":
    main(sys.stdin.readlines())
