import sys

import numpy as np

edges = np.array([[0,1],[0,3],[1,2],[1,4],[2,5],[3,4],[3,5],[4,5]])

matrix = np.zeros((edges.max()+1, edges.max()+1))
matrix[edges[:,0], edges[:,1]] = 1
matrix[edges[:,1], edges[:,0]] = 1

np.set_printoptions(threshold=sys.maxsize)
print(matrix)