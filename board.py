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
        
        neighbours = self.graph[i][j]
        path = []
        visited = set()

        while neighbours != []:
            path += [(i, j)]
            w_index = [*zip(neighbours, [self.warnsdorff[r][s] for r, s in neighbours])]
            w_index = sorted(w_index, key = lambda x: x[1])
            next_square = w_index[0][0]
            visited.add((i, j))
        
            i, j = next_square
            neighbours = [x for x in self.graph[i][j] if x not in visited]

        return path

# %%
chessboard = Board(5, 3)
chessboard.create_graph()
chessboard.add_edges()
chessboard.warnsdorff_graph()
chessboard.traverse()
