#!/usr/bin/env python

import sys
import operator
import string
from collections import defaultdict


def is_valid_checksum(name, checksum):
    counts = defaultdict(lambda: 0)

    for c in name:
        counts[c] += 1

    chars = sorted(counts.items(), key=operator.itemgetter(0), reverse=False)
    chars = sorted(chars, key=operator.itemgetter(1), reverse=True)

    test_checksum = "".join(map(operator.itemgetter(0), chars))[:5]

    return test_checksum == checksum


def decrypt_name(encrypted_name, rot):
    letters = string.ascii_lowercase
    indexes = {c: letters.find(c) for c in letters}

    dec = []

    for c in encrypted_name:
        if c == "-":
            dec.append(" ")
            continue
        i = indexes[c]
        dc = letters[(i + rot) % len(letters)]
        dec.append(dc)

    return "".join(dec)

def solve_decrypted_rooms(lines):
    valid_ids = []

    for line in lines:
        line = line.strip()
        if line == "":
            break

        parts = line.split("[", 1)
        id_parts = parts[0].split("-")

        checksum = parts[1][:-1]
        name = "".join(id_parts[:-1])
        full_name = "-".join(id_parts[:-1])
        sector_id = int(id_parts[-1])

        if is_valid_checksum(name, checksum):
            valid_ids.append((full_name, sector_id))

    answer = None

    for encrypted_name, sector_id in valid_ids:
        name = decrypt_name(encrypted_name, sector_id)
        print name
        if "northpole" in name:
            answer = sector_id

    return "answer: %s" % (answer,)

def main():
    print(solve_decrypted_rooms(sys.stdin.readlines()))


if __name__ == "__main__":
    main()
