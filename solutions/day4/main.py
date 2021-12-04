import os

def get_example_input():
    s = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
    return s.splitlines()

def get_input():
    with open('solutions/day4/input.txt') as f:
        return [x.strip() for x in f.readlines()]

class Entry:
    def __init__(self, number):
        self.number = int(number)
        self.enabled = False
    
    def check_enable(self, bingo_number):
        if bingo_number == self.number:
            self.enabled = True
        return self.enabled
    
    def __str__(self):
        return str(self.number)
    
    def __repr__(self) -> str:
        return str(self)

class Board:
    def __init__(self, idx):
        self.lines = []
        self.idx = idx
        self.turns_ago_victory = -1
    
    def __repr__(self) -> str:
        return f'Board #{self.idx}, Turns since victory: {self.turns_ago_victory}'
    
    def add_line(self, line):
        self.lines.append(line)
    
    def sum_unmarked(self):
        _sum = 0
        for line in self.lines:
            for entry in line:
                if not entry.enabled:
                    _sum += entry.number
        return _sum
    
    def bingo_number_drawn(self, number):
        if self.turns_ago_victory > -1:
            self.turns_ago_victory += 1
        for line in self.lines:
            for entry in line:
                if entry.check_enable(number):
                    if self.check_finished():
                        return True
        return False
    
    def check_line_finished(self, line):
        for entry in line:
            if not entry.enabled:
                return False
        return True

    def set_turns_ago_victory(self):
        if self.turns_ago_victory < 0:
            self.turns_ago_victory = 0

    def check_finished(self):
        for line in self.lines:
            if self.check_line_finished(line):
                self.set_turns_ago_victory()
                return True
        for row in range(len(self.lines)):
            if self.check_line_finished([line[row] for line in self.lines]):
                self.set_turns_ago_victory()
                return True
        """Diagonals not required WTF"""
        """
        # first diagonal
        diagonal_1 = []
        for x in range(len(self.lines)):
            diagonal_1.append(self.lines[x][x])
        if self.check_line_finished(diagonal_1):
            return True
        diagonal_2 = []
        for x in range(len(self.lines)):
            diff = len(self.lines) - x - 1
            diagonal_2.append(self.lines[x][diff])
        if self.check_line_finished(diagonal_2):
            return True
        """
        return False

def create_boards(game_input):
    bingo_numbers = game_input.pop(0).split(',')
    bingo_numbers = [int(x) for x in bingo_numbers]
    boards = []
    idx = 0
    for line in game_input:
        if line == '':
            boards.append(Board(idx))
            idx += 1
        else:
            splits = line.strip().replace('  ', ' ').split(' ')
            boards[-1].add_line([Entry(x) for x in splits])
    return bingo_numbers, boards

def task1():
    game_input = get_input()
    
    bingo_numbers, boards = create_boards(game_input)
    done = None
    for number in bingo_numbers:
        for board in boards:
            if board.bingo_number_drawn(number):
                done = board
                break
        if done is not None:
            break
    return number * board.sum_unmarked()

def task2():
    game_input = get_input()
    
    bingo_numbers, boards = create_boards(game_input)
    cont = True
    for number in bingo_numbers:
        cont = False
        for board in boards:
            if not board.bingo_number_drawn(number):
                cont = True
        if not cont:
            break
    last_winner = sorted(boards, key=lambda x: x.turns_ago_victory)[0]
    
    return number * last_winner.sum_unmarked()