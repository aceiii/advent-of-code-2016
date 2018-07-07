#!/usr/bin/env python

import sys
import operator
from collections import defaultdict


def is_valid_checksum(name, checksum):
    counts = defaultdict(lambda: 0)

    for c in name:
        counts[c] += 1

    chars = sorted(counts.items(), key=operator.itemgetter(0), reverse=False)
    chars = sorted(chars, key=operator.itemgetter(1), reverse=True)

    test_checksum = "".join(map(operator.itemgetter(0), chars))[:5]

    return test_checksum == checksum


def solve_valid_room_checksums(lines):
    valid_ids = []

    for line in lines:
        line = line.strip()
        if line == "":
            break

        parts = line.split("[", 1)
        id_parts = parts[0].split("-")

        checksum = parts[1][:-1]
        name = "".join(id_parts[:-1])
        sector_id = int(id_parts[-1])

        if is_valid_checksum(name, checksum):
            valid_ids.append(sector_id)

    return sum(valid_ids)

def main():
    print(solve_valid_room_checksums(sys.stdin.readlines()))


if __name__ == "__main__":
    main()
