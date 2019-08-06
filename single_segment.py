# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:55:45 2019

@author: user
"""

import cv2
import os
image = cv2.imread('o-1.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) # threshold
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(1,1))
dilated = cv2.dilate(thresh,kernel,iterations = 20)
# cv2.imwrite("new2.jpg",dilated)
contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

# #Saving each contours as a jpg file
contour=contours[2]
[x,y,w,h] = cv2.boundingRect(contour)
# if h<40 or w<40:
#     continue
cv2.rectangle(image,(x,y),(x+w,y+h),(125,0,255),5)
new_image = image[y:y+h, x:x+w]
cv2.imwrite("new22.jpg",new_image)

# Performing in all contours value

for contour in contours:
    [x,y,w,h] = cv2.boundingRect(contour)    
#     if h<40 or w<40:
#         continue
    z=cv2.rectangle(image,(x,y),(x+w,y+h),(125,0,255),4) 
    cv2.imwrite("new2.jpg",z)
    
cv2.waitKey(0)
cv2.destroyAllWindows()