import os
from pprint import pprint

def get_example_input():
    s = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
    return s.splitlines()

def get_input():
    with open('solutions/day11/input.txt') as f:
        return [x.strip() for x in f.readlines()]

class Octopus:
    def __init__(self, starting_value):
        self.value = starting_value
        self.neighbours = set()
        self.has_flashed = False
        self.flash_count = 0
    
    def add_neighbour(self, neighbour):
        self.neighbours.add(neighbour)
        neighbour.neighbours.add(self)
    
    def flash(self):
        if not self.has_flashed:
            self.has_flashed = True
            self.flash_count += 1
            for neighbour in self.neighbours:
                neighbour.step()

    def step(self):
        self.value += 1
        if self.value > 9:
            self.flash()
    
    def reset(self):
        if self.has_flashed:
            self.value = 0
        self.has_flashed = False

    def __str__(self):
        return f'{self.value}'

    def __repr__(self) -> str:
        return str(self)

def get_neighbour_locations(x, y):
    return [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]

def get_neighbour_octopuses(x, y, _octopuses):
    locations = get_neighbour_locations(x, y)
    neighbours = []
    for _x, _y in locations:
        if _x < 0 or _y < 0 or _x >= len(_octopuses[0]) or _y >= len(_octopuses):
            continue
        neighbours.append(_octopuses[_x][_y])
    return neighbours

def task1():
    octopuses = []
    for x, line in enumerate(get_input()):
        octopuses.append([])
        for y, oct_value in enumerate(line):
            new_octopus = Octopus(int(oct_value))
            octopuses[-1].append(new_octopus)
    for x, line in enumerate(octopuses):
        for y, octopus in enumerate(line):
            for neighbour in get_neighbour_octopuses(x, y, octopuses):
                octopus.add_neighbour(neighbour)
    
    for step in range(100):
        for l in octopuses:
            for octopus in l:
                octopus.step()
        for l in octopuses:
            for octopus in l:
                octopus.reset()
    
    flashes = 0
    for l in octopuses:
        for o in l:
            flashes += o.flash_count
    return flashes

def task2():
    octopuses = []
    for x, line in enumerate(get_input()):
        octopuses.append([])
        for y, oct_value in enumerate(line):
            new_octopus = Octopus(int(oct_value))
            octopuses[-1].append(new_octopus)
    for x, line in enumerate(octopuses):
        for y, octopus in enumerate(line):
            for neighbour in get_neighbour_octopuses(x, y, octopuses):
                octopus.add_neighbour(neighbour)
    step = 0
    all_flashed = False
    while not all_flashed:
        for l in octopuses:
            for octopus in l:
                octopus.step()
        all_flashed = True
        for l in octopuses:
            for octopus in l:
                all_flashed &= octopus.has_flashed
        if all_flashed:
            break
        for l in octopuses:
            for octopus in l:
                octopus.reset()
        step += 1
    
    return step + 1