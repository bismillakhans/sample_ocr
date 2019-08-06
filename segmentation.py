# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:47:12 2019

@author: user
"""

import numpy as np
import cv2
import os
image = cv2.imread('o-1.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',gray)

_,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) # threshold
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(4,4))
dilated = cv2.dilate(thresh,kernel,iterations = 20)

contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


# for each contour found, draw a rectangle around it on original image
for contour in contours:
# get rectangle bounding contour
    [x,y,w,h] = cv2.boundingRect(contour)
# discard areas that are too large
#     if h>600 and w>600:
#         continue

# discard areas that are too small
    if h<40 or w<40:
        continue

# draw rectangle around contour on original image
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)
    cv2.imshow("image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()