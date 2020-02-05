import os
import numpy as np
from cv2 import *
import glob

class preprocessing:
    def __init__(self):
        self.startrun()

    def startrun(self):
        path = os.environ
        path = path['IMGDIR']
        if not os.path.exists("output"):
            os.mkdir("output")
        images = glob.glob(path + "\*.tif")
        for imagename in images:
            img = imread(imagename, 1)

            #  green band processing
            height, width = img.shape[:2]
            for j in range(0, height, 1):
                for k in range(0, width, 1):
                    img.itemset((j, k, 0), 0)
                    img.itemset((j, k, 2), 0)

            #  grayscale conversion
            img_gray = cvtColor(img, COLOR_BGR2GRAY)

            #  Vessel central light reflex removal
            kernel = getStructuringElement(MORPH_ELLIPSE, (7, 7))
            erosion = erode(img_gray, kernel, iterations=1)

            #  Adaptive Histogram Equalisation
            clahe = createCLAHE(clipLimit=45.0, tileGridSize=(8, 8))
            claheimage = clahe.apply(erosion)

            # Gaussian Blurring
            blur = GaussianBlur(claheimage, (5, 5), 0)

            # Top Hat transformation
            kernel = getStructuringElement(MORPH_ELLIPSE, (203, 203))
            img_tophat = morphologyEx(blur, MORPH_TOPHAT, kernel)
            filename = imagename.replace("Images", "Output")
            imwrite(filename.replace(".tif", ".bmp"), img_tophat)

