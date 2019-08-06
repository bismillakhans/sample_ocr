# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 16:07:45 2019

@author: user
"""
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import numpy as np
import cv2
import os
image = cv2.imread('o-1.png')
#image=cv2.resize(image,(1700,1200))
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)
#cv2.imshow('gray',~gray)
#cv2.imshow('gray',edged)
#e=edged.copy()
#_, contours, hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)
#cv2.imshow('canny edges after contouring', edged)

print(len(cnts))
cnts = cnts, key=cv2.contourArea, reverse=True
i=1
for c in cnts:
		# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
		if len(approx) == 4:
		        docCnt=approx
		        break
paper = four_point_transform(image, docCnt.reshape(4, 2))
cv2.imshow("image",paper)
            
            



cv2.waitKey(0)
cv2.destroyAllWindows()