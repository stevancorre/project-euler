#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   05/12/2021

def read_source_numbers():
    with open("source.txt", "r") as source_file:
        rows = source_file.readlines()

    return map(int, rows)


def solve():
    result = sum(read_source_numbers())
    return str(result)[0:10]


if __name__ == "__main__":
    print("ANSWER: %s" % solve())
