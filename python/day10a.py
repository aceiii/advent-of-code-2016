#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import re

from collections import defaultdict


class Bot(object):
    def __init__(self):
        self.values = []
        self.low_to = None
        self.high_to = None

    def __repr__(self):
        return "{0}".format("========= FOUND =======" if len(self.values) == 2 else "")


def main(lines):
    bots = defaultdict(lambda: Bot())
    output = defaultdict(lambda: Bot())

    bins = {"bot": bots, "output": output}

    start_bot = None

    for line in lines:
        line = line.strip()

        match = re.match(r"^value (\d+) goes to bot (\d+)$", line)
        if match is not None:
            val, bot = match.groups()
            bots[bot].values.append(int(val))
            if len(bots[bot].values) == 2:
                start_bot = bot
            continue

        match = re.match(r"^bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)$", line)
        if match is not None:
            bot, low_to, low_val, high_to, high_val = match.groups()
            bots[bot].low_to = (low_to, low_val)
            bots[bot].high_to = (high_to, high_val)
            continue


        raise Exception("Invalid line: '{0}'".format(line))

    next_bot = [start_bot]
    while next_bot:
        current_bot = next_bot.pop()

        bot = bots[current_bot]
        low, high = sorted(bot.values)
        bot.values.pop()
        bot.values.pop()

        low_to_bin, low_to_id = bot.low_to
        bins[low_to_bin][low_to_id].values.append(low)
        if low_to_bin == "bot" and len(bins[low_to_bin][low_to_id].values) == 2:
            next_bot.append(low_to_id)

        high_to_bin, high_to_id = bot.high_to
        bins[high_to_bin][high_to_id].values.append(high)
        if high_to_bin == "bot" and len(bins[high_to_bin][high_to_id].values) == 2:
            next_bot.append(high_to_id)

        if low == 17 and high == 61:
            print("found: {0}".format(current_bot))


if __name__ == "__main__":
    main(sys.stdin.readlines())
