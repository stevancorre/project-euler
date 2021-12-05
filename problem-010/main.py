#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   05/12/2021

from math import sqrt
def xis_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))


def is_prime(n):
    if n == 1:
        return False

    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False

    return True

def solve():
    result = 0

    for n in range(1, 2000001):
        if is_prime(n):
            result += n

    return result


if __name__ == "__main__":
    print("ANSWER: %d" % solve())
