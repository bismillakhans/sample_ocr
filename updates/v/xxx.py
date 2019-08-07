import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import imutils
result=cv2.imread("aligned_org.png",0)
orginal=cv2.imread("aligned_res.png",0)

result= cv2.resize(result,(500,500))
orginal=  cv2.resize(orginal,(500,500))

binary=result-orginal
binary = cv2.GaussianBlur(binary, (5, 5), 0)
binary = cv2.threshold(binary, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
binary=~binary
#x=orginal[6:15, 0:95]
#y=result[6:15, 0:95]
#

count =0
for y in range(0, binary.shape[0],100):
   column = binary[4:binary.shape[1], y: y + 95]    
   cv2.imshow("image",column)
   cv2.waitKey(1)
   
   for x in range(0, column.shape[0],16):
        row = column[x:x+10,:]
        
        cv2.imshow("x", cv2.resize(row,(500,100)))
        cv2.waitKey(1)
        
        count=count+1
        
        cnts = cv2.findContours(row.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        questionCnts = []
        
        
        


