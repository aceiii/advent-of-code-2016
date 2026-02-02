#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import string


def main(lines):
    for line in lines:
        marker_mode = 0
        prev = ''
        stack = [list(reversed(line.strip()))]
        expand_params = [0, 0]
        counter = 0
        multipliers = [1]

        while stack:
            line = stack[-1]
            multiplier = multipliers[-1]
            c = line.pop()

            if not line:
                stack.pop()
                multipliers.pop()

            if marker_mode == 0:
                if c == '(':
                    marker_mode = 1
                    prev = ''
                    continue
                counter += multiplier
                continue

            if marker_mode == 1:
                if c in string.digits:
                    prev += c
                    continue
                if c == 'x':
                    marker_mode = 2
                    expand_params[0] = int(prev)
                    prev = ''
                    continue
                raise Exception("Invalid char {}".format(c))

            if marker_mode == 2:
                if c in string.digits:
                    prev += c
                    continue
                if c == ')':
                    marker_mode = 3
                    expand_params[1] = int(prev)
                    prev = ''
                    continue
                raise Exception("Invalid char {}".format(c))

            if marker_mode == 3:
                prev += c
                expand_params[0] -= 1
                if expand_params[0] == 0:
                    marker_mode = 0
                    stack.append(list((reversed(prev))))
                    multipliers.append(multiplier * expand_params[1])
                    prev = ''

        print("Length: {}".format(counter))


if __name__ == "__main__":
    main(sys.stdin.readlines())
