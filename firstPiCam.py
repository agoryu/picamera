from picamera.array import PiRGBArray

import picamera
import cv2
import time
import io

# retourne une image provenant de la picamera
def getImage():
	camera = picamera.PiCamera()
	camera.resolution = (320, 240)
	rawCapture = PiRGBArray(camera)

	time.sleep(0.1)

	camera.capture(rawCapture, "bgr")
	image = rawCapture.array
	return image

# affiche l'image en parametre de la fonction
def displayImage(image):
	cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
	cv2.imshow("Image", image)
	cv2.resizeWindow("Image", 500, 500)
	cv2.waitKey(0)

# detection d'un visage dans une image
def facesDetection(image):
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	return faces

image = getImage()
faces = facesDetection(image)
for(x, y, w, h) in faces:
	cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

displayImage(image)
