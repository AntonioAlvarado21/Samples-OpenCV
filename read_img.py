import cv2 as cv

# Read image
img = cv.imread('Photos/perrito_grande.jpg')

# Display image
cv.imshow('Perrito',img)

# Wait for a key to be pressed (0 = infinite)
cv.waitKey(0)