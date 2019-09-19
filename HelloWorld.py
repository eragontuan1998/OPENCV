import cv2
import numpy as np

img1 = cv2.imread("data_test.png")
img2 = cv2.imread("up.png")

#Get size
wM = img1.shape[1]
hM = img1.shape[0]

wC = img2.shape[1]
hC = img2.shape[0]

#Crop IMG
for i in range (hM):
    for j in range (wM):
        subIMG = img1[i:i+hC,j:j+wC]
        if img2.shape==subIMG.shape:
            dif = cv2.subtract(img2,subIMG)
            b,g,r =cv2.split(dif)
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                print("The images are Equal")
                





                    
