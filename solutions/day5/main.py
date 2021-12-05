import os
import re
from collections import defaultdict

def get_example_input():
    s = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
    return s.splitlines()

def get_input():
    with open('solutions/day5/input.txt') as f:
        return [x.strip() for x in f.readlines()]

PARSER = re.compile(r'(?P<x1>\d+),(?P<y1>\d+)\s->\s(?P<x2>\d+),(?P<y2>\d+)')

def generate_line(x1, y1, x2, y2, ignore_diagonal=True):
    if ignore_diagonal and not ((x1 == x2) or (y1 == y2)):
        return []
    elif not ignore_diagonal and not ((x1 == x2) or (y1 == y2)):
        y_diff = y1
        x_diffs = []
        y_diffs = []
        for x_diff in range(min(x1, x2), max(x1, x2) + 1):
            if x1 < x2:
                x_diffs.append(x_diff)
            else:
                x_diffs.insert(0, x_diff)
        for y_diff in range(min(y1, y2), max(y1, y2) + 1):
            if y1 < y2:
                y_diffs.append(y_diff)
            else:
                y_diffs.insert(0, y_diff)
        results = list(zip(x_diffs, y_diffs))
        return results

    x1, x2 = tuple(sorted([x1, x2]))
    y1, y2 = tuple(sorted([y1, y2]))
    if x1 == x2:
        return [(x1, y) for y in range(y1, y2 + 1)]
    else:
        return [(x, y1) for x in range(x1, x2 + 1)]

def calculate(with_diagonals):
    pipes = [PARSER.match(x) for x in get_input()]
    points = defaultdict(int)
    for pipe in pipes:
        x1,y1 = int(pipe.group('x1')), int(pipe.group('y1'))
        x2,y2 = int(pipe.group('x2')), int(pipe.group('y2'))
        line = generate_line(x1, y1, x2, y2, not with_diagonals)
        for entry in line:
            points[entry] += 1
    return sum(i >= 2 for i in points.values())

def task1():
    return calculate(False)

def task2():
    return calculate(True)