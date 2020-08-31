#%%
import numpy as np
import matplotlib.pyplot as plt
import collections
#%%
class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def create_graph(self):
        nodes = collections.defaultdict(dict)
        for i in range(self.height):
            for j in range(self.width):
                nodes[i][j] = []

        self.graph = nodes

    def add_edges(self):

        on_board = lambda x, y: (x >= 0 & x <= self.width) & (y >= 0 & y <= self.height)
        legal = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for i in range(self.height):
            for j in range(self.width):
                for r, s in legal:
                    if on_board(i+r, j+s):
                        self.graph[i][j] += [(i+r, j+s)]

    def warnsdorff_graph(self):
        paths = self.graph.copy()
        for i in range(self.height):
            for j in range(self.width):
                paths[i][j] = len(self.graph[i][j])

        self.warnsdorff = paths





# %%
chessboard = Board(5, 3)
print(chessboard.width, chessboard.height)
# %%
chessboard.create_graph()
# %%
chessboard.graph
# %%
chessboard.add_edges()
# %%
chessboard.graph
# %%
chessboard.warnsdorff_graph()
# %%
chessboard.warnsdorff
# %%
