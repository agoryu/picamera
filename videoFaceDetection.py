from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time

# initialisation de la camera
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(320, 240))

# initialisation fenetre d'affichage
display_window = cv2.namedWindow("Faces detection")
# initialisation du detecteur
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
time.sleep(1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	
	# recuperation de l'image courante
	image = frame.array

	# detection du visage
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)

	print(faces)

	# creation de la roi autour du visage
	for (x,y,w,h) in faces:
		cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

	# affichage de l'image
	cv2.imshow("Faces detection", image)
	key = cv2.waitKey(1)

	rawCapture.truncate(0)

	if key == 33:
		camera.close()
		cv2.destroyAllWindows()
		break
