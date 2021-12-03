import os
import operator

def get_example_input():
    s = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    return s.splitlines()

def get_input():
    with open('solutions/day3/input.txt') as f:
        return [x.strip() for x in f.readlines()]


def task1():
    inp = get_input()

    sums = [0 for _ in range(len(inp[0]))]
    for line in inp:
        for index, value in enumerate(line):
            if value == "1":
                sums[index] += 1
    gamma = []
    epsilon = []
    for value in sums:
        gamma.append(value > (len(inp) // 2))
        epsilon.append(not gamma[-1])

    gamma = int("".join(str(int(i)) for i in gamma), 2)
    epsilon = int("".join(str(int(i)) for i in epsilon), 2)

    return gamma * epsilon

def search_on_index(index, current_elements, best="1", op=operator.ge):
    bests = [x[index] for x in current_elements].count(best)
    filter_for = ""
    if op(bests, len(current_elements) - bests):
        filter_for = best
    else:
        filter_for = "0" if best == "1" else "1"
    newlist = [x for x in current_elements if x[index] == filter_for]
    return newlist


def task2():
    inp = get_input()

    oxygen_list = inp[:]
    for index, _ in enumerate(inp[0]):
        oxygen_list = search_on_index(index, oxygen_list)
        if len(oxygen_list) == 1:
            break
    oxygen = int(oxygen_list[0], 2)

    co2_list = inp[:]
    for index, _ in enumerate(inp[0]):
        co2_list = search_on_index(index, co2_list, "0", op=operator.le)
        if len(co2_list) == 1:
            break
    co2 = int(co2_list[0], 2)

    return oxygen * co2
