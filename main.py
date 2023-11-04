# import the necessary libraries
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import mediapipe as mp
import camcontrol

# Calling function Picamera
camera = PiCamera()

# Setting resolution of camera
w = 1280
h = 720
camera.resolution = (w, h)

# Setting framerate
camera.framerate = 30

# Change frame to array
rawCapture = PiRGBArray(camera, size=(w, h))

# Calling function drawing utils of Mediapipe.slutions
mp_drawing = mp.solutions.drawing_utils

# Calling function hand of Mediapipe.slutions
mp_hands = mp.solutions.hands

# set font
font = cv2.FONT_HERSHEY_PLAIN

# Calculating tan(60)
tan60 = np.tan(np.pi * 60 / 180)

# create an list variable named LmList
lmList = []

# endless loop for streaming video
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

        # grab the raw NumPy array representing the image
        image = frame.array

        # BRG to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detections
        results = hands.process(image)

        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # deleting all components of lmList
        lmList.clear()

        # Rendering results
        if results.multi_hand_landmarks:
            # Drawing hand palm
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=2, circle_radius=2),
                                          )
            myHand = results.multi_hand_landmarks[0]

            # getting coordinates from fucntion landmark
            for id, lm in enumerate(myHand.landmark):
                # calculating coordinates of key points of the hand
                cx, cy = int(lm.x * w), int(lm.y * h)

                # add id, cx, cy
                lmList.append([id, cx, cy])

        if len(lmList) != 0:
            a = lmList[8][2] - lmList[5][2]

            if a >= 0:
                cv2.putText(image, 'Stop!', (150, 50), font, 2, (0, 0, 255), 2)
                camcontrol.crawlerStop()
            else:
                a = np.abs(lmList[8][2] - lmList[5][2])
                b = np.abs(lmList[8][1] - lmList[5][1])

                # if index finger points straight up
                if b == 0:
                    cv2.putText(image, 'Go ahead!', (50, 50), font, 2, (0, 0, 255), 2)
                    camcontrol.ahead()
                else:
                    # if the index finger in the TURN-LEFT region
                    if (lmList[8][1] > lmList[5][1]) & (tan60 > a / b):
                        cv2.putText(image, 'Turn left', (50, 50), font, 2, (0, 0, 255), 2)
                    camcontrol.turnLeft()

                    # if the index finger in the TURN-RIGHT region
                    elif (lmList[8][1] < lmList[5][1]) & (tan60 > a / b):
                    cv2.putText(image, 'Turn right!', (50, 50), font, 2, (0, 0, 255), 2)
                    camcontrol.turnRight()

                    # if the index finger in the AHEAD region
                    else:
                    cv2.putText(image, 'Go ahead!', (50, 50), font, 2, (0, 0, 255), 2)
                    camcontrol.ahead()

    # Control directions of camera
    horizontal_Position = lmList[0][1]  # get horizontal position of wrist.

    vertical_Position = lmList[0][2]  # get vertical position of wrist.

    # region of wrist l x h 200x150
    if horizontal_Position < (w / 2 - 100):
        camcontrol.cameraRight()

    if horizontal_Position > (w / 2 + 100):
        camcontrol.cameraLeft()

    if vertical_Position < (h / 2 + 100):
        camcontrol.cameraUp()

    if vertical_Position > (h / 2 + 250):
        camcontrol.cameraDown()

        # show the video window
cv2.imshow("Hand gestures", image)

# clear the stream in preparation for the next frame
rawCapture.truncate(0)

# if the `q` key was hit, break from the loop
if cv2.waitKey(1) & 0xFF == ord("q"):
    break

# close the window
cv2.destroyAllWindows()
