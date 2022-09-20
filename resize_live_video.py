import cv2 as cv

# Function for rescale frame
def changeRes(width, height):
    # Works for Live videos
    webcam.set(3, width)
    webcam.set(4, height)
    webcam.set(10, 150)

# Read video from file
webcam = cv.VideoCapture(1)

# Rescale properties of live video before displaying
changeRes(480, 280)

# Loop until the user presses ESC
while True:
    # Read current frame
    isTrue, frame = webcam.read()

    # Display frame
    cv.imshow('Webcam', frame) 

    # Wait for a key to be pressed (0 = infinite)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# Release video capture object
webcam.release()

# Destroy all windows
cv.destroyAllWindows()