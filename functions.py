import cv2 as cv

img = cv.imread('photos/perrito2.jpg')
cv.imshow('Perrito', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

# Blur (reduce noise)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

# Edge Cascade (If we pass blur the edges are more visible)
canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=2)
#cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
#cv.imshow('Eroded', eroded)

# Resize (Ignores aspect ratio) It can be INTER_AREA, INTER_LINEAR, INTER_CUBIC
resized = cv.resize(img, (700,700), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

# Cropping 
cropped = resized[100:200, 200:450]
cv.imshow('Cropped', cropped)

cv.waitKey(0)