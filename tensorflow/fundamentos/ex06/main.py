import numpy as np

def sigmod(z):
    return 1 / (1 + np.exp(-z))

entradas = np.array([
    [1,0],
    [0,1],
    [0,0],
    [1,1]
])