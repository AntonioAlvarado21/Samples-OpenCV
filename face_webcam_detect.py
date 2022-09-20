import cv2 as cv

# Read video from file
video = cv.VideoCapture(1)

# Loop until the user presses ESC
while True:
    # Read current frame
    isTrue, frame = video.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Cascade classifier
    haar_cascade = cv.CascadeClassifier('haar_cascades/haar_face.xml')

    # Detect faces 
    faces_rect = haar_cascade.detectMultiScale(frame_gray, scaleFactor=1.4, minNeighbors=2)

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
        cv.imshow('Detected Faces', frame)
        #print(f'Number of faces found = {len(faces_rect)}')

    # Display frame
    #cv.imshow('Video', frame)
    
    # Wait for a key to be pressed (0 = infinite)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# Release video capture object
video.release()

# Destroy all windows
cv.destroyAllWindows()