import cv2 as cv

# Rescale image
def rescaleFrame(frame, scale=0.75):
    # Works for images, videos and live videos
    width = int(frame.shape[1] * scale) # shape[1] - width
    height = int(frame.shape[0] * scale) # shape[0] - height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Read image
img = cv.imread('Photos/perrito_grande.jpg')

# Display image (with rescale)
cv.imshow('Perrito small', rescaleFrame(img))

# Wait for a key to be pressed (0 = infinite)
cv.waitKey(0)