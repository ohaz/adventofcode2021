import os
import re

def get_example_input():
    s = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
    return s.splitlines()

def get_input():
    with open('solutions/day13/input.txt') as f:
        return [x.strip() for x in f.readlines()]

FOLD_PATTERN = re.compile(r'fold along (?P<axis>y|x)=(?P<coordinate>\d+)')

def fold_on(coordinates, fold):
    _coords = []
    for coordinate in coordinates:
        _new_coordinate = coordinate
        if fold[0] == 'x':
            if coordinate[0] > fold[1]:
                _new_coordinate = (2*fold[1] - (_new_coordinate[0]), _new_coordinate[1])
        elif fold[0] == 'y':
            if coordinate[1] > fold[1]:
                _new_coordinate = (_new_coordinate[0], 2*fold[1] - (_new_coordinate[1]))
        _coords.append(_new_coordinate)
    return _coords

def draw(coordinates):
    max_x = max([x[0] for x in coordinates])
    max_y = max([x[1] for x in coordinates])
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x,y) in coordinates:
                print('#', end='')
            else:
                print(' ', end='')
        print('')

def run(_folds=1):
    mode = 0
    coordinates = []
    folds = []
    for line in get_input():
        if line.strip() == '':
            mode = 1
            continue
        if mode == 0:
            coordinates.append(tuple([int(x) for x in line.strip().split(',')]))
        elif mode == 1:
            if (m := FOLD_PATTERN.match(line)) is not None:
                folds.append((m.group('axis'), int(m.group('coordinate'))))
    folds_to_do = folds[:_folds] if _folds > 0 else folds
    for fold in folds_to_do:
        coordinates = list(set(fold_on(coordinates, fold)))
    return coordinates

def task1():
    coordinates = run(1)    
    return len(set(coordinates))

def task2():
    coordinates = run(-1) 
    draw(coordinates)
    return len(set(coordinates))