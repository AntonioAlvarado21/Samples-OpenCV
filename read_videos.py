import cv2 as cv

# Read video (0 = webcam)
#webcam = cv.VideoCapture(2)

# Read video from file
video = cv.VideoCapture('Videos/personas.mp4')

# Loop until the user presses ESC
while True:
    # Read current frame
    # isTrue, frame = webcam.read()
    isTrue, frame = video.read()

    # Display frame
    cv.imshow('Video', frame)

    # Wait for a key to be pressed (0 = infinite)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# Release video capture object
#webcam.release()
video.release()

# Destroy all windows
cv.destroyAllWindows()