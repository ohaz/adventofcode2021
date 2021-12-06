import os
from collections import deque

def get_example_input():
    s = """3,4,3,1,2"""
    return s.splitlines()

def get_input():
    with open('solutions/day6/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def task1():
    fishes = [int(x) for x in get_input()[0].split(',')]
    for _ in range(80):
        for index, f in enumerate(fishes[:]):
            f -= 1
            if f >= 0:
                fishes[index] = f
            else:
                fishes[index] = 6
                fishes.append(8)
    return len(fishes)

def task2():
    fishes = [int(x) for x in get_input()[0].split(',')]
    fish_groups = deque([fishes.count(x) for x in range(9)])
    for _ in range(256):
        fish_groups.rotate(-1)
        fish_groups[6] += fish_groups[8]
    return sum(list(fish_groups))