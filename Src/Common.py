import numpy as np


def convertMatrixTo1dArray(matrix):
    return np.asarray(matrix).ravel()


def convert1dArrayToMatrix(array, shape):
    return np.asarray(array).reshape(shape)


def stackArrays(arrays):
    return np.stack(arrays, axis=2)
