import cv2
import numpy as np

img = cv2.imread('down.png',0)
imgM = cv2.imread('coding_set.png',0)

newIMG = imgM[200,200]
height, width = imgM.shape[:2]
print (height, width)
newIMG.imshow()
