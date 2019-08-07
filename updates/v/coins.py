# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:14:31 2019

@author: user
"""
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb

image=cv2.imread("seg.png",0)
image=cv2.resize(image,(500,100))

# apply threshold
thresh = threshold_otsu(image)
bw = closing(image > thresh, square(30))

# remove artifacts connected to image border
#cleared = clear_border(bw)

# label image regions
label_image = label(bw)
image_label_overlay = label2rgb(label_image, image=image)

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(image_label_overlay)

for region in regionprops(label_image):
    # take regions with large enough areas
    if region.area >= 1500:
#        print(region.label)
        if 300 < region.coords[0][1] < region.coords[-1][1] < 400: #consider area is betwwen 300 and 400 is option 3
            print("three")
    
#        print(region, region[region])
        # draw rectangle around segmented object
        minr, minc, maxr, maxc = region.bbox
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)

#ax.set_axis_off()
plt.tight_layout()
plt.show()