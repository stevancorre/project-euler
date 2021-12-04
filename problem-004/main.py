#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   04/12/2021

def is_palidrome(n):
    str_n = str(n)
    return str_n[::-1] == str_n


def solve():
    result = 0

    for a in range(100, 999):
        for b in range(a, 999):
            c = a * b

            if is_palidrome(c) and c > result:
                result = c

    return result


if __name__ == "__main__":
    print("ANSWER: %d" % solve())
