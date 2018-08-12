#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from hashlib import md5


def main(door_id):
    password = [None] * 8
    index = 0

    while password.count(None) > 0:
        hash_check = md5(door_id + str(index)).hexdigest()

        if hash_check[:5] == "00000":
            try:
                pos = int(hash_check[5])
                if pos > 7 or password[pos] is not None:
                    raise Exception()

                password[pos] = hash_check[6]
                print(password)
            except:
                index += 1
                continue

        index += 1

    print("Password: {}".format(''.join(password)))


if __name__ == "__main__":
    TEST_INPUT = "abc"
    REAL_INPUT = "ojvtpuvg"

    main(REAL_INPUT)
