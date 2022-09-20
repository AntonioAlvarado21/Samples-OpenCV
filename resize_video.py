import cv2 as cv

# Read video from file
video = cv.VideoCapture('Videos/personas.mp4')

# Rescale frame
def rescaleFrame(frame, scale=0.75):
    # Works for images, videos and live videos
    width = int(frame.shape[1] * scale) # shape[1] - width
    height = int(frame.shape[0] * scale) # shape[0] - height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



# Loop until the user presses ESC
while True:
    # Read current frame
    isTrue, frame = video.read()

    # Display frame
    cv.imshow('Video', rescaleFrame(frame, scale=0.5)) # scale optional

    # Wait for a key to be pressed (0 = infinite)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# Release video capture object
video.release()

# Destroy all windows
cv.destroyAllWindows()