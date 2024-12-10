import cv2
import numpy as np
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=10)  # Increased minNeighbors for better accuracy

    for (x, y, w, h) in faces:
        if w < 50 or h < 50:  # Skip small detections
            continue

        face_roi = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_roi)  # Detect eyes within face
        if len(eyes) >= 2:  # Only proceed if two eyes are detected

            face_img = cv2.equalizeHist(face_roi)  # Normalize lighting
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)


    cv2.imshow('Registering Face', frame)
    if count >= 300 or cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

