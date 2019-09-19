import cv2
import numpy as np
import sys
import os.path
import glob
from matplotlib import pyplot as plt

## Create variable count
up = 0
left = 0
right = 0
down = 0
pausecircle = 0
playcircle = 0

## Create SRC Img
IMGup = cv2.imread('up.png')
IMGleft =cv2.imread('left.png')
IMGright = cv2.imread('right.png')
IMGdown = cv2.imread('down.png')
IMGpausecircle =cv2.imread('pausecircle.png')
IMGplaycircle = cv2.imread('playcircle.png')

## Detect Up
a1 = cv2.imread('data_test.png')
b1 = cv2.cvtColor(a1, cv2.COLOR_BGR2GRAY)
templateUP = cv2.imread('up.png',0)
templateDOWN = cv2.imread('down.png',0)
templateLEFT = cv2.imread('left.png',0)
templateRIGHT = cv2.imread('right.png',0)
templatePLAY = cv2.imread('playcircle.png',0)
templatePAUSE = cv2.imread('pausecircle.png',0)

## w, h = templateUP.shape[::-1]
wM = a1.shape[1]
hM = a1.shape[0]
hC = templateUP.shape[0]
wC = templateUP.shape[1]
print (hM,wM)
for i in range (hM):
    for j in range (wM):
        subIMG = a1[i:i+hC,j:j+wC]
        cv2.imshow('cropIMG',subIMG)
        wS = subIMG.shape[1]
        hS = subIMG.shape[0]
        #dif_up=cv2.subtract(subIMG,IMGup)
        #dif_left=cv2.subtract(subIMG,IMGleft)
        #dif_right=cv2.subtract(subIMG,IMGright)
        #dif_down =cv2.subtract(subIMG,IMGdown)
        #dif_pausecircle =cv2.subtract(subIMG,IMGpausecircle)
        #dif_playcircle=cv2.subtract(subIMG,IMGplaycircle)
        #result_up=not np.any(dif_up)
        #result_left=not np.any(dif_left)
        #result_right=not np.any(dif_right)
        #result_down =not np.any(dif_down)
        #result_pausecircle =not np.any(dif_pausecircle)
        #result_playcircle=not np.any(dif_playcircle)
        #if result_up is True :
        #print (wS,hS)
        
        cv2.waitKey(0)

"""
res = cv2.matchTemplate(b1,templateUP,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    if cv2.matchTemplate(b1,templateUP,cv2.TM_CCOEFF_NORMED) is False:
        up = up+1
    cv2.rectangle(a1, pt, (pt[0] + w, pt[1] + h), (255,0,255), 2)
    cv2.circle (a1, ((pt[0] + pt[0]+w)//2, (pt[1]+pt[1] + h)//2), 63, (255,0,255), -1)

cv2.imwrite('res.png',a1)
print (up)
"""
