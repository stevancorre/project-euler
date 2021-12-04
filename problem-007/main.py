#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   04/12/2021

from math import sqrt


def is_prime(n):
    if n == 2:
        return True

    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False

    return True


def solve():
    result = 0
    count = 0

    while count <= 10001:
        result += 1

        if is_prime(result):
            count += 1

    return result


if __name__ == "__main__":
    print("ANSWER: %d" % solve())
