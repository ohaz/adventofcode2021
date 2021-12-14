import os
from itertools import pairwise
from collections import defaultdict, Counter
from copy import deepcopy

def get_example_input():
    s = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
    return s.splitlines()

def get_input():
    with open('solutions/day14/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def parse_input(_inp):
    template = _inp.pop(0)
    _inp.pop(0)
    insertion_rules = defaultdict(lambda: '')
    for line in _inp:
        source, added = line.split(' -> ')
        insertion_rules[source] = added
    return template, insertion_rules

def task1():
    current_polymer, translation = parse_input(get_input())
    for _ in range(10):
        new_polymer = ''
        for a,b in pairwise(current_polymer):
            new_polymer += f'{a}{translation[a+b]}'
        new_polymer += f'{b}'
        current_polymer = new_polymer
    counted = Counter(current_polymer)
    return current_polymer.count(max(counted, key=counted.get)) - current_polymer.count(min(counted, key=counted.get))

def task2():
    current_polymer, translation = parse_input(get_input())
    pairs = defaultdict(int)
    counter = defaultdict(int)
    for a,b in pairwise(current_polymer):
        pairs[(a,b)] += 1
    for char in current_polymer:
        counter[char] += 1
    for _ in range(40):
        _copy = deepcopy(pairs)
        for key, value in pairs.items():
            a, b = key

            new_element = translation[a+b]
            _copy[(a, new_element)] += value
            _copy[(new_element, b)] += value
            _copy[key] -= value
            counter[new_element] += value
        pairs = _copy
    return max(counter.values()) - min(counter.values())
