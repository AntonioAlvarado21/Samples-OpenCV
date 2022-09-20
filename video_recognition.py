import cv2 as cv

# Read video from file
video = cv.VideoCapture('Videos/selena.mp4')
# Cascade classifier
haar_cascade = cv.CascadeClassifier('haar_cascades/haar_face.xml')
people = ['selena_gomez', 'harry_styles', 'kate_beckinsale', 'henry_cavill']

# Loop until the user presses ESC
while True:
    # Read current frame
    isTrue, frame = video.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces 
    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read('trained/face_trained.yml')

    # Detect the face in the image
    faces_rect = haar_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=1)

    for (x, y, w, h) in faces_rect:
        faces_roi = frame_gray[y:y+h, x:x+w]
        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with a confidence of {confidence}')
        cv.putText(frame, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    
    cv.imshow('Detected Face', frame)

    # Wait for a key to be pressed (0 = infinite)
    if cv.waitKey(1) & 0xFF==ord('d'):
        break

# Release video capture object
video.release()

# Destroy all windows
cv.destroyAllWindows()