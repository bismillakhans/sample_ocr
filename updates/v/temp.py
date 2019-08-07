import cv2
import numpy as np

img = np.array([
    [1, 0, 1, 1, 2],
    [1, 0, 1, 1, 2],
    [1, 0, 1, 1, 2],
    [1, 0, 1, 1, 2],
    [1, 0, 1, 1, 2]], dtype=np.uint8)

new_img = np.zeros_like(img)                                        # step 1
for val in np.unique(img)[1:]:                                      # step 2
    mask = np.uint8(img == val)                                     # step 3
    labels, stats = cv2.connectedComponentsWithStats(mask, 4)[1:3]  # step 4
    largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])      # step 5
    new_img[labels == largest_label] = val                          # step 6

print(new_img)