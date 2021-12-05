#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   05/12/2021

from math import sqrt


def count_factors_of(n):
    return sum(2 for d in range(1, int(sqrt(n) + 1)) if n % d == 0)


def solve():
    result = 0

    nth = 1
    while True:
        result += nth
        nth += 1

        if count_factors_of(result) > 499:
            return result


if __name__ == "__main__":
    print("ANSWER: %d" % solve())
