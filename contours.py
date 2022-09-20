import cv2 as cv
import numpy as np

img = cv.imread('Photos/perrito_grande.jpg')
#cv.imshow('Perrito', img)

blank = np.zeros(img.shape, dtype='uint8')
#cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

countours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(countours)} countours found!')

cv.drawContours(blank, countours, -1, (0,255,0), 1) # -1 --> All countours
cv.imshow('Countours Drawn', blank)

cv.waitKey(0)