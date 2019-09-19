import cv2
import numpy as np
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
w = a1.shape[1]
h = a1.shape[0]
wU, hU = templateUP.shape[::-1]

res = cv2.matchTemplate(b1,templateUP,cv2.TM_CCOEFF_NORMED)
print ('res',res)
threshold = 0.8
loc = np.where( res >= threshold)
x = 0
y = 0
for pt in zip(*loc[::-1]):
    #cv2.rectangle(a1, pt, (pt[0] + wU, pt[1] + hU), (255,0,255), 2)
    cptX = ((pt[0] + pt[0]+wU)//2)
    cptY = (pt[1]+pt[1] + hU)//2
    cv2.circle (a1, ((pt[0] + pt[0]+wU)//2, (pt[1]+pt[1] + hU)//2), 63, (255,0,255), -1)
    if x != cptX or y != cptY:
        x = cptX
        y = cptY
        up=up+1
    
#    print(pt)
    

cv2.imwrite('res.png',a1)
print (up)


"""
## Detect Left

# Read the images from the file
a2 = cv2.imread('res.png')
b2 = cv2.cvtColor(a2, cv2.COLOR_BGR2GRAY)
template = cv2.imread('left.png',0)

# Get the size of the template. This is the same size as the match.
w, h = template.shape[::-1]

res = cv2.matchTemplate(b2,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    # Draw the rectangle on large_image
    cv2.rectangle(a2, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv2.circle (a2, ((pt[0] + pt[0]+w)//2, (pt[1]+pt[1] + h)//2), 63, (0,0,255), -1)
cv2.imwrite('res.png',a2)

## Detect Right
a3 = cv2.imread('res.png')
b3 = cv2.cvtColor(a3, cv2.COLOR_BGR2GRAY)
template = cv2.imread('right.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(b3,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(a3, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)
    cv2.circle (a3, ((pt[0] + pt[0]+w)//2, (pt[1]+pt[1] + h)//2), 63, (255,0,0), -1)
cv2.imwrite('res.png',a3)

## Detect Down
a4 = cv2.imread('res.png')
b4 = cv2.cvtColor(a4, cv2.COLOR_BGR2GRAY)
template = cv2.imread('down.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(b4,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(a4, pt, (pt[0] + w, pt[1] + h), (255,255,0), 2)
    cv2.circle (a4, ((pt[0] + pt[0]+w)//2, (pt[1]+pt[1] + h)//2), 63, (255,255,0), -1)
cv2.imwrite('res.png',a4)

## Detect pausecircle
a5 = cv2.imread('res.png')
b5 = cv2.cvtColor(a5, cv2.COLOR_BGR2GRAY)
template = cv2.imread('pausecircle.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(b5,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(a5, pt, (pt[0] + w, pt[1] + h), (64,128,255), 2)
    cv2.circle (a5, ((pt[0] + pt[0]+w)//2, (pt[1]+pt[1] + h)//2), 63, (64,128,255), -1)
cv2.imwrite('res.png',a5)

## Detect playcircle
a6 = cv2.imread('res.png')
b6 = cv2.cvtColor(a6, cv2.COLOR_BGR2GRAY)
template = cv2.imread('playcircle.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(b6,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(a6, pt, (pt[0] + w, pt[1] + h), (255,0,128), 2)
    cv2.circle (a6, ((pt[0] + pt[0]+w)//2, (pt[1]+pt[1] + h)//2), 63, (255,0,128), -1)
cv2.imwrite('res.png',a6)

"""
