#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import re


class Screen(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []

        for y in range(height):
            self.pixels.append([0] * width)

    def rect(self, width, height):
        assert width <= self.width and height <= self.height
        for y in range(height):
            for x in range(width):
                self.pixels[y][x] = 1

    def rotate_row(self, y, b):
        row = self.pixels[y][:]

        for x in range(self.width):
            self.pixels[y][x] = row[(x - b) % self.width]

    def rotate_column(self, x, b):
        row = []
        for y in range(self.height):
            row.append(self.pixels[y][x])

        for y in range(self.height):
            self.pixels[y][x] = row[(y - b) % self.height]

    def count(self):
        return sum(map(sum, self.pixels))

    def process(self,lines):
        for line in lines:
            m = re.match(r"rect (\d+)x(\d+)", line.strip())
            if m is not None:
                self.rect(*map(int, m.groups()))
                continue

            m = re.match(r"rotate row y=(\d+) by (\d+)", line.strip())
            if m is not None:
                self.rotate_row(*map(int, m.groups()))
                continue

            m = re.match(r"rotate column x=(\d+) by (\d+)", line.strip())
            if m is not None:
                self.rotate_column(*map(int, m.groups()))
                continue

    def __repr__(self):
        lines = []
        lines.append("=" * (self.width + 2))
        for row in self.pixels:
            lines.append("|{}|".format(''.join(
                map(lambda x: '#' if x == 1 else '.', row))))
        lines.append("=" * (self.width + 2))
        return '\n'.join(lines)


def main(lines):
    screen = Screen(50, 6)
    screen.process(lines)
    print(screen.count())
    print(screen)

if __name__ == "__main__":
    main(sys.stdin.readlines())
