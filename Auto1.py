from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv
import numpy as np

camera = PiCamera(resolution = (320,240))
camera.framerate = 32
rawCapture = PiRGBArray(camera,size=(320,240))
# allow the camera to warmup
time.sleep(0.1)
# grab an image from the camera
imag=cv.imread("road.jpg")
imag=cv.resize(imag,(320,240) , interpolation = cv.INTER_AREA)

# for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#     # grab the raw NumPy array representing the image, then initialize the timestamp
#     # and occupied/unoccupied text
#     image = frame.array
#     image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     cv.namedWindow("imagewin", cv.WINDOW_KEEPRATIO)
#     cv.resizeWindow("imagewin", 1280, 720)
#     cv.imshow("imagewin", image)
#     key = cv.waitKey(1) & 0xFF
#     # clear the stream in preparation for the next frame
#     rawCapture.truncate(0)
#      # if the `q` key was pressed, break from the loo
points = np.float32([(0,180),(60,150),(230,150),(280,180)])
pointsdes =np.float32( [(60,240),(60,0),(300,0),(300,240)])

points1= [(0,180),(60,150),(230,150),(280,180)]
pointsdes1 = [(60,240),(60,0),(300,0),(300,240)]

cv.line(imag,points1[0],points1[1],(0,0,255),1)
cv.line(imag,points1[1],points1[2],(0,0,255),1)
cv.line(imag,points1[2],points1[3],(0,0,255),1)
cv.line(imag,points1[3],points1[0],(0,0,255),1)

# cv.line(imag,pointsdes[0],pointsdes[1],(0,255,0),2)
# cv.line(imag,pointsdes[1],pointsdes[2],(0,0,255),2)
# cv.line(imag,pointsdes[2],pointsdes[3],(0,0,255),2)
# cv.line(imag,pointsdes[3],pointsdes[0],(0,0,255),2)

matrix = cv.getPerspectiveTransform(points,pointsdes)
result = cv.warpPerspective(imag, matrix, (320,240))
cv.namedWindow("imagewin", cv.WINDOW_KEEPRATIO)
cv.resizeWindow("imagewin", 640, 480)
cv.imshow("imagewin", imag)
#

cv.namedWindow("perspective", cv.WINDOW_KEEPRATIO)
cv.resizeWindow("perspective", 640, 480)
cv.imshow("perspective", result)
cv.waitKey(0)
