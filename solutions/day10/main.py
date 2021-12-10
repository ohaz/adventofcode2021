import os

def get_example_input():
    s = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
    return s.splitlines()

def get_input():
    with open('solutions/day10/input.txt') as f:
        return [x.strip() for x in f.readlines()]

OPENING = set(['(', '[', '{', '<'])
CLOSING = set([')', ']', '}', '>'])

TRANSLATION = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

TRANSLATION_OPENING_TO_CLOSING = {v: k for k, v in TRANSLATION.items()}

POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

STACK_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def parse(line):
    stack = []
    for char in line:
        if char in OPENING:
            stack.append(char)
        elif char in CLOSING:
            if stack[-1] == TRANSLATION[char]:
                stack.pop()
            else:
                raise SyntaxError(char)
    return stack[::-1]

def task1():
    points = 0
    for line in get_input():
        try:
            parse(line)
        except SyntaxError as e:
            points += POINTS[str(e)]
    return points

def task2():
    points_all = []
    for line in get_input():
        try:
            stack = parse(line)
            points = 0
            for char in stack:
                points *= 5
                points += STACK_POINTS[TRANSLATION_OPENING_TO_CLOSING[char]]
            points_all.append(points)
        except SyntaxError as e:
            pass
    points_all = sorted(points_all)
    return points_all[len(points_all) // 2]