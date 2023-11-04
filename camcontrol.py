"""
This class obtains all methods that control the movements of the camera such as UP, DOWN, TURN LEFT, RIGHT and methods that control Crawler turn LEFT, RIGHT, AHEAD
"""

import RPi.GPIO as GPIO
import time

# setting up output mode using BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# declare varialbes
c1 = 17  # GPIO 17
c2 = 27  # GPIO 27
c3 = 22  # GPIO 22
c4 = 10  # GPIO 10

m1 = 23  # GPIO 23
m2 = 24  # GPIO 24
m3 = 25  # GPIO 25
m4 = 9  # GPIO 9

# declare pinouts for controlling the Camera
GPIO.setup(c1, GPIO.OUT)
GPIO.setup(c2, GPIO.OUT)
GPIO.setup(c3, GPIO.OUT)
GPIO.setup(c4, GPIO.OUT)

# declare pin inputs for controlling Crawler
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)
GPIO.setup(m3, GPIO.OUT)
GPIO.setup(m4, GPIO.OUT)


# method stopping the movement of the camera by setting output pins GPIO 17, 27, 22, 10 at LOW-level
def cameraStop():
    GPIO.output(c1, GPIO.LOW)
    GPIO.output(c2, GPIO.LOW)
    GPIO.output(c3, GPIO.LOW)
    GPIO.output(c4, GPIO.LOW)


# method stopping the movement of Crawler by setting output pins GPIO 23, 24, 25, 9 at LOW-level
def crawlerStop():
    GPIO.output(m1, GPIO.LOW)
    GPIO.output(m2, GPIO.LOW)
    GPIO.output(m3, GPIO.LOW)
    GPIO.output(m4, GPIO.LOW)


# method controlling camera moving UP by setting output pins GPIO 10 at a HIGH level and GPIO 22 at LOW-level
def cameraUp():
    GPIO.output(c3, GPIO.LOW)
    GPIO.output(c4, GPIO.HIGH)
    time.sleep(0.01)  # time for movement is 1 millisecond
    cameraStop()


# method controlling camera moving DOWN by setting output pins GPIO 22 at HIGH level and GPIO 10 at LOW-level
def cameraDown():
    GPIO.output(c3, GPIO.HIGH)
    GPIO.output(c4, GPIO.LOW)
    time.sleep(0.01)  # time for movement is 1 millisecond
    cameraStop()


# method controlling camera moving RIGHT by setting output pins GPIO 27 at HIGH level and GPIO 17 at LOW-level
def cameraRight():
    GPIO.output(c1, GPIO.LOW)
    GPIO.output(c2, GPIO.HIGH)
    time.sleep(0.01)  # time for movement is 1 millisecond
    cameraStop()


# method controlling camera moving LEFT by setting output pins GPIO 27 at HIGH level and GPIO 17 at LOW-level
def cameraLeft():
    GPIO.output(c1, GPIO.HIGH)
    GPIO.output(c2, GPIO.LOW)
    time.sleep(0.01)  # time for movement is 1 millisecond
    cameraStop()


# method controlling crawler AHEAD by setting output pins GPIO 23, GPIO 25 at HIGH level and GPIO 24, GPIO 9 at LOW-level
def ahead():
    GPIO.output(m1, GPIO.HIGH)
    GPIO.output(m2, GPIO.LOW)
    GPIO.output(m3, GPIO.HIGH)
    GPIO.output(m4, GPIO.LOW)


# method controlling crawler turnRIGHT by setting output pins GPIO 23 at HIGH level and GPIO 24, GPIO 25, and GPIO 9 at LOW-level
def turnRight():
    GPIO.output(m1, GPIO.HIGH)
    GPIO.output(m2, GPIO.LOW)
    GPIO.output(m3, GPIO.LOW)
    GPIO.output(m4, GPIO.LOW)


# method controlling crawler turnLEFT by setting output pins GPIO 25 at HIGH level and GPIO 23, GPIO 24, and GPIO 9 at LOW-level
def turnLeft():
    GPIO.output(m1, GPIO.LOW)
    GPIO.output(m2, GPIO.LOW)
    GPIO.output(m3, GPIO.HIGH)
    GPIO.output(m4, GPIO.LOW)
