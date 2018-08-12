#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
from operator import itemgetter


def main(lines):
    N = len(lines[0].strip())

    repititions = []
    for _ in range(N):
        repititions.append({})

    for line in lines:
        for index in range(N):
            char = line[index]
            if char in repititions[index]:
                repititions[index][char] += 1
            else:
                repititions[index][char] = 1

    message = [None] * N
    for index in range(N):
        chars = sorted(repititions[index].items(),
                       key=itemgetter(1),
                       reverse=False)

        print(chars)
        message[index] = chars[0][0]

    print("Message: {}".format(''.join(message)))


if __name__ == "__main__":
    main(sys.stdin.readlines())
