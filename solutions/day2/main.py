import os
import re

def get_example_input():
    s = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    return s.splitlines()

def get_input():
    with open('solutions/day2/input.txt') as f:
        return [x for x in f.readlines()]

COMMAND_REGEX = re.compile(r'(?P<direction>forward|down|up)\s(?P<amount>\d+)')

def run_command_1(command):
    if (m:=COMMAND_REGEX.match(command)) is not None:
        direction = m.group('direction')
        amount = int(m.group('amount'))

        if direction == 'forward':
            return amount, 0
        elif direction == 'up':
            return 0, -amount
        elif direction == 'down':
            return 0, amount

def run_command_2(command, aim):
    if (m:=COMMAND_REGEX.match(command)) is not None:
        direction = m.group('direction')
        amount = int(m.group('amount'))

        if direction == 'forward':
            return amount, aim * amount, aim
        elif direction == 'up':
            return 0, 0, aim - amount
        elif direction == 'down':
            return 0, 0, aim + amount

def task1():
    x, y = 0, 0
    for command in get_input():
        diff_x, diff_y = run_command_1(command)
        x += diff_x
        y += diff_y
    return x*y

def task2():
    x, y, aim = 0, 0, 0
    for command in get_input():
        diff_x, diff_y, aim = run_command_2(command, aim)
        x += diff_x
        y += diff_y
    return x*y