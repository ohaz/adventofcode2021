import os
from queue import PriorityQueue
import sys
import copy
import networkx


def get_example_input():
    s = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
    return s.splitlines()

def get_input():
    with open('solutions/day15/input.txt') as f:
        return [x.strip() for x in f.readlines()]

def get_neighbour_locations(x, y):
    return [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]

def is_valid_neighbour(world, x, y):
    return x >= 0 and y >= 0 and x < len(world[0]) and y < len(world)

class Graph:
    def __init__(self, amount_vertices):
        self.amount_vertices = amount_vertices
        self.edges = [[-1 for i in range(amount_vertices)] for j in range(amount_vertices)]
        self.visited = set()

    def add_edge(self, u, v, u_v_weight, v_u_weight):
        self.edges[u][v] = u_v_weight
        self.edges[v][u] = v_u_weight
 
    def dijkstra(self, src):
        D = {v:sys.maxsize for v in range(self.amount_vertices)}
        D[src] = 0

        queue = PriorityQueue()
        queue.put((0, src))

        while not queue.empty():
            (distance, current) = queue.get()
            self.visited.add(current)

            for neighbour in range(self.amount_vertices):
                if self.edges[current][neighbour] != -1:
                    distance = self.edges[current][neighbour]
                    if neighbour not in self.visited:
                        old_cost = D[neighbour]
                        new_cost = D[current] + distance

                        if new_cost < old_cost:
                            queue.put((new_cost, neighbour))
                            D[neighbour] = new_cost
        return D


def task1():
    world = []
    for line in get_input():
        world.append([])
        for entry in line:
            world[-1].append(int(entry))
    
    graph = Graph(len(world) * len(world[0]))

    for y in range(len(world)):
        for x in range(len(world[0])):
            neighbours = get_neighbour_locations(x, y)
            for neighbour in neighbours:
                _x, _y = neighbour
                if is_valid_neighbour(world, _x, _y):
                    graph.add_edge(y * len(world[0]) + x, _y * len(world[0]) + _x,  world[_y][_x], world[y][x])

    distances = graph.dijkstra(0)
    target_location = len(world) * len(world[0]) - 1
    return distances[target_location]

def task2():
    world = []
    for line in get_input():
        world.append([])
        for entry in line:
            world[-1].append(int(entry))
        _world = copy.copy(world[-1])
        for _ in range(4):
            _world = [(x % 9) + 1 for x in _world]
            world[-1].extend(_world)

    _world = copy.copy(world)
    for i in range(1,5):
        for line in _world:
            world.append([x+i if x+i < 10 else (x+i) -9 for x in line])
   
    graph = networkx.DiGraph()

    for y in range(len(world)):
        for x in range(len(world[0])):
            neighbours = get_neighbour_locations(x, y)
            for neighbour in neighbours:
                _x, _y = neighbour
                if is_valid_neighbour(world, _x, _y):
                    graph.add_edge((x, y), (_x, _y), weight=world[_x][_y])
                    graph.add_edge((_x, _y), (x, y), weight=world[x][y])
        
    return networkx.shortest_path_length(graph, source=(0,0), target=(len(world[0]) -1, len(world) - 1), weight='weight')