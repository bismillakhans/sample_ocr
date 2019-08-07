# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2


img=cv2.imread("full_fill.png")
img_matrix=np.asarray(img)
width,height,c=img.shape
n=4
a=int(width/n)
b=int(height/n)
resize=cv2.resize(img,(a,b))

crop=resize[310:a,50:b+50]




cv2.imshow("image",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()