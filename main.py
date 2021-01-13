import cv2
import os
from datetime import datetime

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.
cap = cv2.VideoCapture(0)
i = 0
while cap.isOpened():
    # Today's date for naming convention of saved pictures
    now = datetime.now()
    dt_string = now.strftime("%m-%d-%y_%H:%M:%S")

    while True:
        # Read the frame
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw the rectangle around each face
        # Check for rectangle inside display
        # Capture image of face and save to file
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            path = '/home/matt/Security_Cam'
            if face_cascade.empty():
                continue
            else:
                os.chdir(path)
                cv2.imwrite(dt_string + '.tiff', img)

        # Display
        cv2.imshow('Security Cam 1', img)
        break

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    i += 1

# Release the VideoCapture object
cap.release()



