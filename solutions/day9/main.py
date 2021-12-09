import os
from math import prod

def get_example_input():
    s = """2199943210
3987894921
9856789892
8767896789
9899965678"""
    return s.splitlines()

def get_input():
    with open('solutions/day9/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def apply_border(_map):
    _map.insert(0, [10 for _ in range(len(_map[0]))])
    _map.append([10 for _ in range(len(_map[0]))])

    for entry in _map:
        entry.append(10)
        entry.insert(0, 10)
    return _map

def is_low_point(_map, x, y):
    adjacent_and_self = [_map[x][y], _map[x+1][y], _map[x-1][y], _map[x][y+1], _map[x][y-1]]
    value = min(adjacent_and_self)
    return value == _map[x][y] and adjacent_and_self.count(_map[x][y]) == 1

def find_basin(_map, x, y):
    fields_to_look_at = set([(x, y), (x+1, y), (x-1, y), (x, y+1), (x, y-1)])
    fields_been_in = set()
    while len(fields_to_look_at) > 0:
        looking_at = fields_to_look_at.pop()
        _x, _y = looking_at
        if _map[_x][_y] >= 9:
            continue
        if looking_at in fields_been_in:
            continue
        fields_been_in.add(looking_at)
        new_locations = set([(_x+1, _y), (_x-1, _y), (_x, _y+1), (_x, _y-1)])
        fields_to_look_at = fields_to_look_at.union(new_locations)
    return len(fields_been_in)
        

def task1():
    _map = [list(map(int, list(x))) for x in get_input()]
    _map = apply_border(_map)

    low_points = []
    for x, entry in enumerate(_map):
        for y, value in enumerate(entry):
            if value == 10:
                continue
            if is_low_point(_map, x, y):
                low_points.append(value + 1)
    return sum(low_points)

def task2():
    _map = [list(map(int, list(x))) for x in get_input()]
    _map = apply_border(_map)

    low_points = []
    for x, entry in enumerate(_map):
        for y, value in enumerate(entry):
            if value == 10:
                continue
            if is_low_point(_map, x, y):
                low_points.append((x, y))
    basins = []
    for low_point in low_points:
        basins.append(find_basin(_map, low_point[0], low_point[1]))
    return prod(sorted(basins)[:-4:-1])