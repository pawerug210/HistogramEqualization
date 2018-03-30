from Src.GraphHelper import GraphHelper
from Src.PictureHelper import PictureHelper
import numpy as np


class Program:

    def __init__(self):
        self.pictureHelper = PictureHelper()
        self.graphHelper = GraphHelper()

    def run(self, picturePath, blackwhite):
        picture = self.pictureHelper.getPictureGrayScaleArray(
            picturePath) if blackwhite else self.pictureHelper.getColorPicture(picturePath)
        if not blackwhite:
            equalizedPictureArray = self.pictureHelper.equalizeColorPictureHistogram(picture, 256)
        else:
            self.graphHelper.createHistogram(picture, 'before')
            equalizedPictureArray = self.pictureHelper.equalizePictureHistogram(picture, 256)
            self.graphHelper.createHistogram(equalizedPictureArray, 'after')
            self.graphHelper.drawGraphs()
        self.pictureHelper.savePicture(equalizedPictureArray, (picturePath.split('.')[0] + '_equalized.' + picturePath.split('.')[1]))


program = Program()
program.run('test_picture.jpg', True)
# program.run('test_picture_3.jpg', False)
program.run('test_picture.png', False)
