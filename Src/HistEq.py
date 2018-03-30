import numpy as np
import math as math
from Src.Common import convertMatrixTo1dArray


class HistEq:

    def __init__(self, matrix, range):
        self.array = convertMatrixTo1dArray(matrix)
        self.arraySize = self.array.size
        self.range = range
        unique, counts = np.unique(self.array, return_counts=True)
        self.occurrenceDict = dict(zip(unique, counts))
        self.probabilityDict = dict(zip(unique, (self.calculateOccurrenceProbability(float(x)) for x in unique)))
        self.cumulativeDict = self.createCumulativeDict()

    def createCumulativeDict(self):
        dict = {}
        for x in range(0, int(self.range)):
            dict[x] = self.cumulativeDistributionFunction(x)
        return dict

    def calculateOccurrenceProbability(self, value):
        return self.getOccurencesNumber(value) / self.arraySize

    def getOccurencesNumber(self, value):
        return self.occurrenceDict[value] if value in self.occurrenceDict else 0

    def getCount(self, matrix):
        return len(np.unique(np.asarray(matrix)))

    # CDF
    def cumulativeDistributionFunction(self, value):
        cdf = 0.0
        for i in (x for x in self.probabilityDict.keys() if x <= int(value)):
            cdf += self.probabilityDict[i]
        return cdf

    # normalize with values [0, 1]
    def normalizeMatrix(self, matrix):
        minValue = matrix.min()
        subtraction = matrix.max() - minValue
        for index in range(0, matrix.size):
            matrix.itemset(index, (matrix.item(index) - minValue) / subtraction)
        return matrix

    def equalizationFormula(self, value):
        return math.floor(self.cumulativeDict[value] * self.range - 1)
