#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Stévan Corre <stevancorre@protonmail.com>
# Date:   05/12/2021

import math

GRID_WIDTH = 20
GRID_HEIGHT = 20


def read_source_grid():
    with open("source.txt", "r") as source_file:
        rows = source_file.readlines()

    return [map(int, row.split()) for row in rows]


def product_of(ns):
    result = 1
    for n in ns:
        result *= n

    return result


def solve():
    result = 0
    grid = read_source_grid()

    # horizontally
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH - 4):
            result = max(result, product_of(grid[y][x:x + 4]))

    # vertically
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT - 4):
            ns = [grid[y + offset][x] for offset in range(4)]
            result = max(result, product_of(ns))

    # diagonally \
    for x in range(GRID_WIDTH - 4):
        for y in range(GRID_HEIGHT - 4):
            ns = [grid[y + offset][x + offset] for offset in range(4)]
            result = max(result, product_of(ns))

    # diagonally /
    for x in range(GRID_WIDTH - 4):
        for y in range(4, GRID_HEIGHT):
            ns = [grid[y - offset][x + offset] for offset in range(4)]
            result = max(result, product_of(ns))

    return result


if __name__ == "__main__":
    print("ANSWER: %d" % solve())
