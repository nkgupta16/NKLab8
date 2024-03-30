# Variant 1: Conversion to halftone	

import cv2
import numpy as np

image = cv2.imread('variant-1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
halftone = np.zeros_like(gray, dtype=np.uint8)

for i in range(gray.shape[0]):
    for j in range(gray.shape[1]):
        pixel_value = gray[i, j]
        threshold = np.random.uniform(0, 255)
        if pixel_value > threshold:
            halftone[i, j] = 255
        else:
            halftone[i, j] = 0

scale_factor = 5
halftone = cv2.resize(halftone, (0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_NEAREST)

window_name = 'Halftone Image'
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 1061, 706)  # Change the window size to 800 x 600 pixels

cv2.imshow(window_name, halftone)
cv2.waitKey(0)
cv2.destroyAllWindows()
