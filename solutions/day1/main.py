import os
from itertools import islice, pairwise

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def get_example_input():
    return [int(x) for x in '199 200 208 210 200 207 240 269 260 263'.split(' ')]

def get_input():
    with open('solutions/day1/input.txt') as f:
        return [int(x) for x in f.readlines()]

def task1():
    lines = get_input()
    increasing = [b > a for (a,b) in pairwise(lines)].count(True)
    return increasing

def task2():
    lines = get_input()
    threewise = []
    for i in range(0, len(lines) - 2):
        threewise.append(sum(take(3, lines[i:])))
    increasing = [b > a for (a,b) in pairwise(threewise)].count(True)
    return increasing