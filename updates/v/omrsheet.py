#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 08:36:49 2019

@author: bismi
"""


import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt

img=cv2.imread("result.png",0)

# Create an algorithm to detect left most point
# or let user choose four points and calculate offset
leftY = 80
leftX = 55
offsetX = 915
offsetY = 1256

#crop_img = im[100:200, 100:300].copy()
#cv2.imshow("image",crop_img)
#cv2.waitKey(0)




# pixelFrom to pixelTo
pixelFrom = 1
pixelTo = 4

# up, down, left, right
numberOfCheckedPixel = 4

totalCalculatedPixels = (pixelTo - pixelFrom) * numberOfCheckedPixel

# threshold for correctness since not totally white
# choose better value for more accurate results
threshold = 0.7

choice_list = []

def printPoint(leftX, leftY, choice):
    sum = 0
    for i in range(pixelFrom, pixelTo):
        sum += img[leftY + i, leftX]
        sum += img[leftY - i, leftX]
        sum += img[leftY, leftX + i]
        sum += img[leftY, leftX - i]


    #print(sum)

    if sum / (totalCalculatedPixels * 256) < threshold:
        #print("Black")
        choice_list.append(choice)
        print(choice)
    else:
        #print("White")
        print(end='')




# calculate the first option coordinate against left most answer box
firstOptionX = 95
firstOptionY = 525
lastOptionX = 96
lastOptionY = 1316


# formula: optionOffsetY = (lastOptionY - firstOptionY) / 40
optionOffsetX = 40
optionOffsetY = round((lastOptionY - firstOptionY) / 40)





# Number of horizontal segments
segments = 5
k = 40
segmentOffsetX = 184

for j in range (0, segments):

    print('\n')
    print("=====================")
    print("Segment: " + str(j+1))
    print("=====================")
    print('\n')

    for i in range (0, 40):
        print("Answer " + str(k * j + i + 1))
        choice_list = []
        #print("First POS:" + str(firstOptionX + j * segmentOffsetX) + "," + str(round(firstOptionY + optionOffsetY * i)))
        printPoint(firstOptionX + j * segmentOffsetX, round(firstOptionY + optionOffsetY * i), 1)
        printPoint(firstOptionX + optionOffsetX + j * segmentOffsetX, round(firstOptionY + optionOffsetY * i), 2)
        printPoint(firstOptionX + optionOffsetX * 2 + j * segmentOffsetX, round(firstOptionY + optionOffsetY * i), 3)
        printPoint(firstOptionX + optionOffsetX * 3 + j * segmentOffsetX, round(firstOptionY + optionOffsetY * i), 4)

        if len(choice_list) > 1:
            print('ERROR: Multiple Answers Given.')
        elif len(choice_list) == 0:
            print('No Answers Selected.')

        # Spacing between circles are not accurate
        if(i % 5 == 0):
            optionOffsetY += 0.025

    # reset the increment for the above fix
    optionOffsetY -= 0.2