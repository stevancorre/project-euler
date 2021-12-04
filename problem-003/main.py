#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   04/12/2021

from math import sqrt


def is_prime(n):
    if n == 2:
        return True

    for d in range(2, n):
        if n % d == 0:
            return False

    return True


def solve():
    result = 0
    N = 600851475143

    for d in range(1, int(sqrt(N))):
        if N % d == 0 and is_prime(d):
            result = d

    return result


if __name__ == "__main__":
    print("ANSWER: %d" % solve())
