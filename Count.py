import cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX
## Detect up with color red
a10 =cv2.imread("coding_set.png")
a1 = cv2.imread("subimg.png")
print(a1.type())
inputImage = cv2.imread("data_test.png")
##Crop input Image
## Save in array[ cropImage[]
print (a1)
b1 = cv2.cvtColor(a1,cv2.COLOR_BGR2GRAY)

IMGup = cv2.imread('up.png' )
IMGleft =cv2.imread('left.png' )
IMGright = cv2.imread('right.png' )
IMGdown = cv2.imread('down.png' )
IMGpause =cv2.imread('pause.png' )
IMGplay = cv2.imread('play.png' )

###
"""
cv2.imshow('IMG3',img3)
cv2.waitKey(1000)
cv2.destroyAllWindows()
"""
###
template = cv2.imread('up.png',0)
wU, hU = template.shape[::-1]

##
res = cv2.matchTemplate(b1,template,cv2.TM_CCOEFF_NORMED)

threshold = 0.8

loc = np.where(res>=threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(a1, pt, (pt[0] + wU, pt[1] + hU), (0,0,255), -1)
    cv2.putText(a1,"UP",(pt[0], (pt[1]+pt[1] + hU)//2),font,1,(255, 255, 255))
cv2.imwrite("newres.png",a1)
"""
## Detect down with color green
a4 = cv2.imread('res.png')
b4 = cv2.cvtColor(a4, cv2.COLOR_BGR2GRAY)
template = cv2.imread('down.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(b4,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
a = 0;
for pt in zip(*loc[::-1]):
    cv2.rectangle(a4, pt, (pt[0] + w, pt[1] + h), (0,255,0), -1)
    cv2.putText(a4,"DOWN",(pt[0], (pt[1]+pt[1] + h)//2),font,1,(255, 255, 255))
    ##cv2.circle (a5, ((pt[0] + pt[0]+w)//2, (pt[1]+pt[1] + h)//2), 63, (64,128,255), -1)
cv2.imwrite('res.png',a4)


##
## Detect Left with color blue
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
    cv2.rectangle(a2, pt, (pt[0] + w, pt[1] + h), (255,0,0), -1)
    cv2.putText(a2,"LEFT",(pt[0], (pt[1]+pt[1] + h)//2),font,1,(255, 255, 255))
    ##cv2.circle (a2, ((pt[0] + pt[0]+w)//2, (pt[1]+pt[1] + h)//2), 63, (0,0,255), -1)
cv2.imwrite('res.png',a2)

## Detect Right with color brown
a3 = cv2.imread('res.png')
b3 = cv2.cvtColor(a3, cv2.COLOR_BGR2GRAY)
template = cv2.imread('right.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(b3,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(a3, pt, (pt[0] + w, pt[1] + h), (42,42,165), -1)
    cv2.putText(a3,"RIGHT",(pt[0], (pt[1]+pt[1] + h)//2),font,1,(255, 255, 255))
    ##cv2.circle (a3, ((pt[0] + pt[0]+w)//2, (pt[1]+pt[1] + h)//2), 63, (255,0,0), -1)
cv2.imwrite('res.png',a3)


## Detect pause with color white
a5 = cv2.imread('res.png')
b5 = cv2.cvtColor(a5, cv2.COLOR_BGR2GRAY)
template = cv2.imread('pause.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(b5,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(a5, pt, (pt[0] + w, pt[1] + h), (147,20,255), -1)
    cv2.putText(a5,"PAUSE",(pt[0], (pt[1]+pt[1] + h)//2),font,1,(255, 255, 255))
    ##cv2.circle (a5, ((pt[0] + pt[0]+w)//2, (pt[1]+pt[1] + h)//2), 63, (64,128,255), -1)
cv2.imwrite('res.png',a5)

## Detect play with color black
a6 = cv2.imread('res.png')
b6 = cv2.cvtColor(a6, cv2.COLOR_BGR2GRAY)
template = cv2.imread('play.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(b6,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(a6, pt, (pt[0] + w, pt[1] + h), (0,0,0), -1)
    cv2.putText(a6,"PLAY",(pt[0], (pt[1]+pt[1] + h)//2),font,1,(255, 255, 255))
    ##cv2.circle (a6, ((pt[0] + pt[0]+w)//2, (pt[1]+pt[1] + h)//2), 63, (255,0,128), -1)
cv2.imwrite('res.png',a6)


cv2.waitKey(1000)
cv2.destroyAllWindows()
"""
"""
## DETECT COLOR
image = cv2.imread("res.png");
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("Color Detect",image)
cv2.imshow("Color  ",hsv)
lower_red = np.array([133,21,199])
upper_red = np.array([255,0,255])

mask =cv2.inRange(hsv,lower_red,upper_red)

#cv2.imshow("Color Detect",image)

#cv2.imshow("Color Detect",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

