import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/semaforo-1.jpg')
cv.imshow('Semaforo', img)


# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

# Mask
blank = np.zeros(img.shape[:2], dtype='uint8')
# Intersection area
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 250, 255, -1)
# Image with mask Gray
masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Masked GRAY Image', masked)


# Image with mask RGB
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked RGB Image', masked)

# Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()


# Color histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

cv.waitKey(0)