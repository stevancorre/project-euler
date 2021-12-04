#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   04/12/2021

def is_divisible(n):
    for i in range(1, 20):
        if n % i != 0:
            return False

    return True

def solve():
    result = 1

    while not is_divisible(result):
        result += 1

    return result


if __name__ == "__main__":
    print("ANSWER: %d" % solve())