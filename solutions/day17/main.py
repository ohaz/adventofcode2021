import os
import re
import sys
try:
    from tqdm import tqdm
except ImportError:
    tqdm = lambda x:x

def get_example_input():
    s = """target area: x=20..30, y=-10..-5"""
    return s.splitlines()

def get_input():
    with open('solutions/day17/input.txt') as f:
        return [x.strip() for x in f.readlines()]

REGEX = re.compile(r'target area: x=(?P<x1>[-+]?\d+)\.\.(?P<x2>[-+]?\d+), y=(?P<y1>[-+]?\d+)\.\.(?P<y2>[-+]?\d+)')
def parse_input(line):
    points = []
    if (m:=REGEX.match(line)) is not None:
        x1, x2 = int(m.group('x1')), int(m.group('x2'))
        y1, y2 = int(m.group('y1')), int(m.group('y2'))
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                points.append((x, y))
    return points

def sign(x): 
  return 1-(x<=0) 

def test_starting_position(pos, velocity, targets):
    pos_x, pos_y = pos
    vel_x, vel_y = velocity
    lowest_y = min([_pos[1] for _pos in targets])
    y_max = pos_y
    while lowest_y <= pos_y:
        pos_x += vel_x
        pos_y += vel_y
        vel_x += (-1 * sign(vel_x)) if vel_x != 0 else 0
        vel_y -= 1
        y_max = max(y_max, pos_y)
        if (pos_x, pos_y) in targets:
            return y_max
    return None

def task1():
    points = parse_input(get_input()[0])
    x_max = max([p[0] for p in points])
    y_max = -1
    for x in tqdm(range(x_max + 1)):
        for y in range(500):
            if (result := test_starting_position((0, 0), (x, y), points)) is not None:
                y_max = max(y_max, result)
    return y_max

def task2():
    points = parse_input(get_input()[0])
    x_max = max([p[0] for p in points])
    valids = 0
    for x in tqdm(range(x_max + 1)):
        for y in range(-100, 500):
            if (result := test_starting_position((0, 0), (x, y), points)) is not None:
                valids += 1
    return valids