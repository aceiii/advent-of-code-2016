#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from hashlib import md5


def main(door_id):
    password = []
    index = 0

    while len(password) < 8:
        hash_check = md5(door_id + str(index)).hexdigest()

        if hash_check[:5] == "00000":
            password.append(hash_check[5])
            print(''.join(password))

        index += 1

    print("Password: {}".format(''.join(password)))


if __name__ == "__main__":
    TEST_INPUT = "abc"
    REAL_INPUT = "ojvtpuvg"

    main(REAL_INPUT)
