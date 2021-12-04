#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   04/12/2021

def solve():
    result = 0

    a = 1
    b = 2
    c = 0

    while a < 4000000:
        c = a + b
        a = b
        b = c

        if a % 2 == 0:
            result += a

    return result


if __name__ == "__main__":
    print("ANSWER: %d" % solve())
