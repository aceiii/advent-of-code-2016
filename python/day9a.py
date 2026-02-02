#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import string

def main(lines):
    for line in lines:
        marker_mode = 0
        prev = ''
        buffer = []
        expand_params = [0, 0]

        for c in line.strip():
            if marker_mode == 0:
                if c == '(':
                    marker_mode = 1
                    prev = ''
                    continue
                buffer.append(c)
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
                    while expand_params[1] > 0:
                        expand_params[1] -= 1
                        buffer.append(prev)
                    prev = ''

        result = ''.join(buffer)
        print(result)
        print("Length: {}".format(len(result)))


if __name__ == "__main__":
    main(sys.stdin.readlines())
