import os
from typing import Counter

def get_example_input():
    s = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
    return s.splitlines()

segments = {
    'cf': 1,
    'abcefg': 0,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

def unique_length_segments():
    lengths = [len(x) for x in segments.keys()]
    filtered = {}
    for key, value in segments.items():
        if lengths.count(len(key)) == 1:
            filtered[key] = value
    return filtered

def get_input():
    with open('solutions/day8/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def split(line):
    left, right = [x.strip() for x in line.split('|')]
    patterns = left.split(' ')
    output_values = right.split(' ')
    return patterns, output_values

def task1():
    unique_segments = unique_length_segments()
    unique_lengths = [len(x) for x in unique_segments.keys()]
    counter = 0
    for line in get_input():
        _, output_values = split(line)
        for output in output_values:
            if len(output) in unique_lengths:
                counter += 1
    return counter

def print_known_segments(top=None, middle=None, bottom=None, top_left=None, bottom_left=None, top_right=None, bottom_right=None):
    print(f'Top: {top}, middle: {middle}, bottom: {bottom}, TL: {top_left}, BL: {bottom_left}, TR: {top_right}, BR: {bottom_right}')

def fix_type(s):
    return ''.join(sorted(list(s)))

def build_all(top=None, middle=None, bottom=None, top_left=None, bottom_left=None, top_right=None, bottom_right=None, _print=False):
    if None in [top, middle, bottom, top_left, bottom_left, top_right, bottom_right]:
        raise Exception('Not all are known')
    if _print:
        print_known_segments(top, middle, bottom, top_left, bottom_left, top_right, bottom_right)
    matched_patterns = {
        fix_type(top.union(top_left).union(top_right).union(bottom_left).union(bottom_right).union(bottom)): 0,
        fix_type(top_right.union(bottom_right)): 1,
        fix_type(top.union(top_right).union(middle).union(bottom_left).union(bottom)): 2,
        fix_type(top.union(top_right).union(middle).union(bottom_right).union(bottom)): 3,
        fix_type(top_left.union(top_right).union(middle).union(bottom_right)): 4,
        fix_type(top.union(top_left).union(middle).union(bottom_right).union(bottom)): 5,
        fix_type(top.union(top_left).union(middle).union(bottom_left).union(bottom_right).union(bottom)): 6,
        fix_type(top.union(top_right).union(bottom_right)): 7,
        fix_type(top.union(top_left).union(top_right).union(middle).union(bottom_left).union(bottom_right).union(bottom)): 8,
        fix_type(top.union(top_right).union(top_left).union(middle).union(bottom_right).union(bottom)) : 9,
    }
    return matched_patterns


def task2():
    unique_segments = unique_length_segments()
    unique_lengths = [len(x) for x in unique_segments.keys()]
    counter = 0
    for line in get_input():
        patterns, output_values = split(line)
        matched_patterns = {}
        for output in output_values + patterns:
            match len(output):
                case 2:
                    matched_patterns[1] = set(output)
                case 4:
                    matched_patterns[4] = set(output)
                case 3:
                    matched_patterns[7] = set(output)
                case 7:
                    matched_patterns[8] = set(output)
        patternset = [set(x) for x in patterns]
        outputset = [set(x) for x in output_values]
        topline = matched_patterns[7] - matched_patterns[1]
        almost_nine = matched_patterns[4].union(topline)
        for s in patternset + outputset:
            if len(s - almost_nine) == 1:
                bottom_line = s - almost_nine
                break
        matched_patterns[9] = matched_patterns[4].union(topline).union(bottom_line)
        almost_three = matched_patterns[1].union(bottom_line).union(topline)
        for s in patternset + outputset:
            if len(s - almost_three) == 1:
                middle_line = s - almost_three
                break
        top_left = matched_patterns[9] - matched_patterns[1] - topline - middle_line - bottom_line
        almost_five = topline.union(bottom_line).union(top_left).union(middle_line)
        for s in patternset + outputset:
            if len(s - almost_five) == 1:
                bottom_right = s - almost_five
                break
        matched_patterns[5] = almost_five.union(bottom_right)
        for s in patternset + outputset:
            if len(s - matched_patterns[5]) == 1 and not len(s-matched_patterns[9]) == 0:
                bottom_left = s - matched_patterns[5]
        top_right = set('abcdefg') - topline - middle_line - bottom_line - top_left - bottom_left - bottom_right
        matched_patterns = build_all(topline, middle_line, bottom_line, top_left, bottom_left, top_right, bottom_right)
        result_line = 0
        for value in outputset:
            result_line *= 10
            result_line += matched_patterns[fix_type(value)]
        counter += result_line
    return counter