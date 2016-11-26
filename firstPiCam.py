from picamera.array import PiRGBArray

import picamera
import cv2
import time

camera = picamera.PiCamera()
camera.resolution = (1920, 1088)
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCapture, "bgr")
image = rawCapture.array

cv2.imshow("Image", image)
cv2.waitKey(0)
