from scipy import misc
from Src.HistEq import HistEq
from Src.Common import convert1dArrayToMatrix
from Src.Common import stackArrays
import numpy as np

class PictureHelper:

    def __init__(self):
        pass

    def getPictureGrayScaleArray(self, picturePath):
        return misc.imread(picturePath, flatten=True, mode='L')

    def getColorPicture(self, picturePath):
        return misc.imread(picturePath, mode='RGB')

    def equalizeColorPictureHistogram(self, picture, scaleRange):
        r, g, b = picture[:, :, 0], picture[:, :, 1], picture[:, :, 2]
        rEqualized = self.equalizePictureHistogram(np.asmatrix(r), scaleRange)
        gEqualized = self.equalizePictureHistogram(np.asmatrix(g), scaleRange)
        bEqualized = self.equalizePictureHistogram(np.asmatrix(b), scaleRange)
        equalizedPicture = stackArrays((rEqualized, gEqualized, bEqualized))
        return equalizedPicture


    def equalizePictureHistogram(self, pictureArray, scaleRange):
        histEq = HistEq(pictureArray, scaleRange)
        equalizedPicture = []
        for x in range(0, pictureArray.size):
            equalizedPicture.append(histEq.equalizationFormula(pictureArray.item(x)))
        return convert1dArrayToMatrix(equalizedPicture, pictureArray.shape)

    def savePicture(self, pictureArray, picturePath):
        misc.imsave(picturePath, pictureArray)
