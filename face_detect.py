import cv2 as cv


img = cv.imread('Photos/personas2.jpg')
#cv.imshow('Persona', img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

# Cascade classifier
haar_cascade = cv.CascadeClassifier('haar_cascades/haar_face.xml')

# Detect faces (Incresing the scale factor will increase the accuracy but will decrease the speed 
# and minNeighbors will increase the speed but decrease the accuracy) 
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=6)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow('Detected Faces', img)

cv.waitKey(0)