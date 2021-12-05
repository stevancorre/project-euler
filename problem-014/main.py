#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   05/12/2021

def count_collatz_sequence_elements(n):
    count = 0
    while n != 1:
        count += 1
        n = n / 2 if n % 2 == 0 else 3 * n + 1

    return count


def solve():
    result = 0
    largest_chain = 0

    for n in range(1000000, 0, -1):
        chain_length = count_collatz_sequence_elements(n)
        if count_collatz_sequence_elements(n) > largest_chain:
            result = n
            largest_chain = chain_length

    return result


if __name__ == "__main__":
    print("ANSWER: %d" % solve())
