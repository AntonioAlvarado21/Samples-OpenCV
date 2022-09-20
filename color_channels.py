import cv2 as cv
import numpy as np

img = cv.imread('Photos/semaforo-1.jpg')
#cv.imshow('Semaforo', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# Splitting the image into its color channels
b, g, r = cv.split(img)
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merging the color channels
merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

cv.waitKey(0)