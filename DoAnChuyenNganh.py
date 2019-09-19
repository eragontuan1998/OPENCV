import cv2
import numpy as np

## Input Big Image
big_image = cv2.imread("data_test_5.png")

## Input Small Image
IMGup = cv2.imread('up.png',0)
IMGleft =cv2.imread('left.png',0)
IMGright = cv2.imread('right.png',0)
IMGdown = cv2.imread('down.png',0)
IMGpause =cv2.imread('pause.png',0)
IMGplay = cv2.imread('play.png',0)

## Create tuples
t = ()
result=()

## Get size image
height = big_image.shape[0]
width = big_image.shape[1]

## Crop big image with two loop(while,for) and save it into tuple
for y in range (0,height,170):
    for x in range (0,width,165):
        crop = big_image[y:y+160,x:x+160]
        t = t + (crop,)
        ##cv2.imshow("new_IMG",crop)
        ##cv2.waitKey(0)
        ##cv2.destroyAllWindows()
        ## x=x+160
    ## y=y+160
        
## Compare matrix with matrix small you have just entered inside
for i in t:
    IMG_GRAY = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    res_IMGup = cv2.matchTemplate(IMG_GRAY,IMGup,cv2.TM_CCOEFF_NORMED)
    res_IMGleft =cv2.matchTemplate(IMG_GRAY,IMGleft,cv2.TM_CCOEFF_NORMED)
    res_IMGright = cv2.matchTemplate(IMG_GRAY,IMGright,cv2.TM_CCOEFF_NORMED)
    res_IMGdown = cv2.matchTemplate(IMG_GRAY,IMGdown,cv2.TM_CCOEFF_NORMED)
    res_IMGpause = cv2.matchTemplate(IMG_GRAY,IMGpause,cv2.TM_CCOEFF_NORMED)
    res_IMGplay = cv2.matchTemplate(IMG_GRAY,IMGplay,cv2.TM_CCOEFF_NORMED)
    #thresUp = 0.6
    #thresLeft = 0.8
    #thresRight = 0.58
    #thresDown = 0.8
    #thressPause = 0.63
    #thressPlay = 0.63
    thresUp = 0.45
    thresLeft = 0.6
    thresRight = 0.5
    thresDown = 0.7
    thressPause = 0.3
    thressPlay = 0.4
    v_up = res_IMGup >= thresUp
    v_left = res_IMGleft >= thresLeft
    v_right = res_IMGright >= thresRight
    v_down = res_IMGdown >= thresDown
    v_pause = res_IMGpause >= thressPause
    v_play = res_IMGplay >= thressPlay
    if v_right.any():
        result = result + ("right",)
    elif v_up.any():
        result = result + ("up",)
    elif v_left.any():
        result = result + ("left",)
    elif v_down.any():
        result = result + ("down",)
    elif v_pause.any():
        result = result + ("pause",)
    elif v_play.any():
        result = result + ("play",)
## Output result with array you have just entered value into
for re in result:
    print (re)
