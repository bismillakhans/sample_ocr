import cv2
import matplotlib.pyplot as plt
import imutils
from skimage.measure import label, regionprops
img=cv2.imread("seg1.png",0)
img=cv2.resize(img,(500,100))
ret,img = cv2.threshold(img,127,255,0)
i,cnts,n = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cn = imutils.grab_contours(cnts)
#if len(cn)<0:
#    print(00)
questionCnts = []
img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#img2=cv2.drawContours(img, cnts, -1, (0,255,0), 3)



cv2.imshow("x",img )
cv2.waitKey(0)
