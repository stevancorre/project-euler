#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   04/12/2021

def solve():
    sum_of_squares = sum(map(lambda n: pow(n, 2), range(1, 101)))
    square_of_sum = pow(sum(range(1, 101)), 2)

    result = square_of_sum - sum_of_squares
    return result


if __name__ == "__main__":
    print("ANSWER: %d" % solve())
