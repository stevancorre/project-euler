#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   04/12/2021

def solve():
    result = 0
    for n in range(0, 1000):
        if n % 3 == 0 or n % 5 == 0:
            result += n

    return result


if __name__ == "__main__":
    print("ANSWER: %d" % solve())
