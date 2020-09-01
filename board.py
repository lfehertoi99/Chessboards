#%%
import numpy as np
import random
import matplotlib.pyplot as plt
import collections
import copy
#%%
class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def create_graph(self):
        nodes = collections.defaultdict(dict)
        for i in range(self.width):
            for j in range(self.height):
                nodes[i][j] = []

        self.graph = nodes

    def add_edges(self):

        on_board = lambda x, y: ((x >= 0) and (x < self.width)) and ((y >= 0) and (y < self.height))
        legal = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for i in range(self.width):
            for j in range(self.height):
                for r, s in legal:
                    if on_board(i+r, j+s):
                        self.graph[i][j] += [(i+r, j+s)]

    def warnsdorff_graph(self):
        paths = copy.deepcopy(self.graph)
        for i in range(self.width):
            for j in range(self.height):
                paths[i][j] = len(paths[i][j])

        self.warnsdorff = paths

    def traverse(self, start = None):

        if not start:
            i, j = random.randint(0, self.width-1), random.randint(0, self.height-1)
        if start:
            i, j = start
        print("Starting square: %d,%d" % (i, j))
        neighbours = self.graph[i][j]
        path = [(i, j)]
        visited = set()

        while neighbours != []:
            w_index = [*zip(neighbours, [self.warnsdorff[r][s] for r, s in neighbours])] #get w-index of neighbours
            w_index = sorted(w_index, key = lambda x: x[1]) #sort in ascending order of w-index
            next_square = w_index[0][0] #select square with lowest index
            for x,y in neighbours: #reduce w-index of neighbours by 1
                self.warnsdorff[x][y] -= 1
            visited.add((i, j)) #add current square to visited
            i, j = next_square #update square 
            path += [(i, j)] #add current square to path
            neighbours = [x for x in self.graph[i][j] if x not in visited] #update neighbours
        print("Length of path:", len(path))
        return path

# %%
chessboard = Board(5, 3)
chessboard.create_graph()
chessboard.add_edges()
chessboard.warnsdorff_graph()
chessboard.traverse()

# %%
