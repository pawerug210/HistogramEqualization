import matplotlib.pyplot as plt
from Src.Common import convertMatrixTo1dArray


class GraphHelper:

    def __init__(self):
        pass

    def createHistogram(self, matrix, title):
        plt.hist(convertMatrixTo1dArray(matrix), bins=range(0, 255), label=title)

    def drawGraphs(self):
        plt.show()