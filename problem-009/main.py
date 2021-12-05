#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   05/12/2021

def is_triplet(a, b, c):
    return pow(a, 2) + pow(b, 2) == pow(c, 2)


def solve():
    result = 0

    for a in range(0, 1000):
        for b in range(a + 1, 1000 - a):
            for c in range(b + 1, 1000 - b):
                if is_triplet(a, b, c) and a + b + c == 1000:
                    result = (a, b, c)

    return result[0] * result[1] * result[2]


if __name__ == "__main__":
    print("ANSWER: %d" % solve())
