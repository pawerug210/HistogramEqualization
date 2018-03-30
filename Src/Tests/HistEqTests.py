import unittest
import numpy as np
from Src.HistEq import HistEq


class CalculationHelperTests(unittest.TestCase):

    def __init__(self, testname):
        super(CalculationHelperTests, self).__init__(testname)
        self.numberMatrix = np.matrix([[1, 2, 3, 4],
                                       [2, 3, 4, 5],
                                       [3, 4, 5, 6],
                                       [4, 5, 6, 7]], dtype=float)
        self.maxRange = 256
        self.helper = HistEq(self.numberMatrix, self.maxRange)

    def test_occurencesNumber(self):
        self.assertEqual(0, self.helper.getOccurencesNumber(0))
        self.assertEqual(1, self.helper.getOccurencesNumber(1))
        self.assertEqual(2, self.helper.getOccurencesNumber(2))
        self.assertEqual(3, self.helper.getOccurencesNumber(3))
        self.assertEqual(4, self.helper.getOccurencesNumber(4))
        self.assertEqual(3, self.helper.getOccurencesNumber(5))
        self.assertEqual(2, self.helper.getOccurencesNumber(6))
        self.assertEqual(1, self.helper.getOccurencesNumber(7))
        self.assertEqual(0, self.helper.getOccurencesNumber(8))

    def test_calculateOccurrenceProbability(self):
        self.assertEqual(4.0 / 16.0, self.helper.calculateOccurrenceProbability(4))
        self.assertEqual(3.0 / 16.0, self.helper.calculateOccurrenceProbability(3))
        self.assertEqual(2.0 / 16.0, self.helper.calculateOccurrenceProbability(2))
        self.assertEqual(1.0 / 16.0, self.helper.calculateOccurrenceProbability(1))
        self.assertEqual(0, self.helper.calculateOccurrenceProbability(0))

    def test_getCount(self):
        self.assertEqual(7, self.helper.getCount(self.numberMatrix))

    def test_normalizeMatrix(self):
        normalizedMatrix = self.helper.normalizeMatrix(self.numberMatrix)
        self.assertEqual(0, self.helper.normalizeMatrix(normalizedMatrix).item((0, 0)))
        self.assertEqual(1, self.helper.normalizeMatrix(normalizedMatrix).item((3, 3)))
        self.assertEqual(0.5, self.helper.normalizeMatrix(normalizedMatrix).item((1, 2)))
        self.assertEqual(1.0 / 3.0, self.helper.normalizeMatrix(normalizedMatrix).item((1, 1)))

    def test_cumulativeDistributionFunction(self):
        self.assertEqual(1.0 / 16.0, self.helper.cumulativeDistributionFunction(1))
        self.assertEqual(3.0 / 16.0, self.helper.cumulativeDistributionFunction(2))
        self.assertEqual(10.0 / 16.0, self.helper.cumulativeDistributionFunction(4))
        self.assertEqual(1.0, self.helper.cumulativeDistributionFunction(7))

    def test_equalizationFormula(self):
        self.assertEqual(15, self.helper.equalizationFormula(1))
        self.assertEqual(255, self.helper.equalizationFormula(7))
        # self.assertEqual(0, self.helper.equalizationFormula(1, self.numberMatrix))
        # self.assertEqual(0, self.helper.equalizationFormula(1, self.numberMatrix))


if __name__ == '__main__':
    unittest.main()
