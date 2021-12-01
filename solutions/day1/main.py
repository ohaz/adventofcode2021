import os
from itertools import islice

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
    larger = 0
    previous = lines[0]
    for line in lines:
        if line > previous:
            larger += 1
        previous = line
    return larger

def task2():
    lines = get_input()
    threewise = []
    for i in range(0, len(lines) - 2):
        threewise.append(sum(take(3, lines[i:])))
    larger = 0
    previous = threewise[0]
    for entry in threewise:
        if entry > previous:
            larger += 1
        previous = entry
    return larger