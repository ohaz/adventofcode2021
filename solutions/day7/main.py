import os
import sys

def get_example_input():
    s = """16,1,2,0,4,2,7,1,2,14"""
    return s.splitlines()

def get_input():
    with open('solutions/day7/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def task1():
    crabs = [int(x) for x in get_input()[0].split(',')]
    best_fuel_cost = sys.maxsize
    for pos in range(min(crabs), max(crabs) + 1):
        fuel_cost = 0
        for crab in crabs:
            fuel_cost += abs(crab - pos)
        best_fuel_cost = min(best_fuel_cost, fuel_cost)
    return best_fuel_cost
        

def task2():
    crabs = [int(x) for x in get_input()[0].split(',')]
    best_fuel_cost = sys.maxsize
    for pos in range(min(crabs), max(crabs) + 1):
        fuel_cost = 0
        for crab in crabs:
            fuel_cost += int(abs(crab - pos) * (abs(crab - pos) + 1) / 2)
        best_fuel_cost = min(best_fuel_cost, fuel_cost)
    return best_fuel_cost