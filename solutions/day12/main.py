import os

def get_example_input():
    s = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""
    s = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""
    s = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""" 
    return s.splitlines()

def get_input():
    with open('solutions/day12/input.txt') as f:
        return [x.strip() for x in f.readlines()]

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = set()
    
    def is_big_cave(self):
        return self.name[0].isupper()
    
    def is_start(self):
        return 'start' == self.name
    
    def is_end(self):
        return 'end' == self.name
    
    def __repr__(self):
        return str(self)
    
    def __str__(self) -> str:
        return f'{self.name}'

def find_paths(current_path, visited):
    if current_path[-1].is_end():
        return [current_path]
    paths = []
    for neighbour in current_path[-1].neighbours:
        if neighbour not in visited:
            _visited = visited if neighbour.is_big_cave() else visited + [neighbour]
            paths.extend(find_paths(current_path + [neighbour], _visited))
    return paths

def task1():
    nodes = {}
    start = None
    for line in get_input():
        _nodes = line.strip().split('-')
        for node in _nodes:
            if node not in nodes.keys():
                nodes[node] = Node(node)
                if node == 'start':
                    start = nodes[node]
        nodes[_nodes[0]].neighbours.add(nodes[_nodes[1]])
        nodes[_nodes[1]].neighbours.add(nodes[_nodes[0]])
    paths = find_paths([start], [start])
    return len(paths)

def find_paths_twice(current_path, visited, has_twice=False):
    if current_path[-1].is_end():
        return [current_path]
    paths = []
    for neighbour in current_path[-1].neighbours:
        if neighbour.is_start():
            continue
        if neighbour not in visited:
            _visited = visited if neighbour.is_big_cave() else visited + [neighbour]
            paths.extend(find_paths_twice(current_path + [neighbour], _visited, has_twice))
        elif (neighbour in visited) and (not has_twice) and (not neighbour == 'start'):
            _visited = visited if neighbour.is_big_cave() else visited + [neighbour]
            paths.extend(find_paths_twice(current_path + [neighbour], visited, True))           
    return paths

def task2():
    nodes = {}
    start = None
    for line in get_input():
        _nodes = line.strip().split('-')
        for node in _nodes:
            if node not in nodes.keys():
                nodes[node] = Node(node)
                if node == 'start':
                    start = nodes[node]
        nodes[_nodes[0]].neighbours.add(nodes[_nodes[1]])
        nodes[_nodes[1]].neighbours.add(nodes[_nodes[0]])
    paths = find_paths_twice([start], [start])
    return len(paths)