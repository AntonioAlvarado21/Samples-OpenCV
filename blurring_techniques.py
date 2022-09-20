import cv2 as cv

img = cv.imread('Photos/perrito_grande.jpg')
cv.imshow('Perrito', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur (better for salt and pepper noise)
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur (better for preserving edges)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)