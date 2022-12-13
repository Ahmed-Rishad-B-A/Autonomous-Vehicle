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

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    #grab the raw NumPy array representing the image, then initialize the timestamp  # and occupied/unoccupied text
    image = frame.array
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.namedWindow("imagewin2", cv.WINDOW_KEEPRATIO)
    cv.resizeWindow("imagewin2", 1280, 720)
    cv.imshow("imagewin2", image)
    key = cv.waitKey(1) & 0xFF
    print(key)
    if key==ord('q'):
        cv.destroyWindow("imagewin2")
        break
     # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loo

points1= [(0,180),(65,150),(150,150),(150,180)]
pointsdes1 = [(60,240),(60,0),(300,0),(300,240)]

points = np.float32(points1)
pointsdes = np.float32( pointsdes1)

histogramlane=np.zeros(320)
ROIlane=np.array([])

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

result = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
cv.namedWindow("grayed", cv.WINDOW_KEEPRATIO)
cv.resizeWindow("grayed", 640, 480)
cv.imshow("grayed", result)

ret,thresholded = cv.threshold(result,180,255,cv.THRESH_BINARY)
cv.namedWindow("thresholded", cv.WINDOW_KEEPRATIO)
cv.resizeWindow("thresholded", 640, 480)
cv.imshow("thresholded", thresholded)


#edge = cv.Canny(thresholded,100,500,4)
#cv.namedWindow("canny", cv.WINDOW_KEEPRATIO)
#cv.resizeWindow("canny", 640, 480)
#cv.imshow("canny",edge)

thresholded = cv.cvtColor(thresholded, cv.COLOR_GRAY2BGR)
#cv.imshow("thresholded", thresholded)   
  
  
histogramlane.resize(320)
histogramlane[:] = 0
for i in range(320):
    ROIlane=thresholded[140:240,i]
    ROIlane=ROIlane/255
    histogramlane[i]=np.sum(ROIlane)
print(histogramlane)
leftpos=np.argmax(histogramlane[0:130])
print("leftpo=",leftpos)
rightpos=np.argmax(histogramlane[320:170:-1])
print("rightpos=",rightpos)               
cv.line(thresholded,(leftpos,0),(leftpos,240),(0,255,0),2)
cv.line(thresholded,(320-rightpos,0),(320-rightpos,240),(0,255,0),2)


lanecenter=(320-rightpos+leftpos)//2
print("lanecenter",lanecenter)
cv.line(thresholded,(lanecenter,0),(lanecenter,240),(0,0,255),2)
framecenter=160
cv.line(thresholded,(framecenter,0),(framecenter,240),(255,0,0),2)

cv.namedWindow("thresholded1", cv.WINDOW_KEEPRATIO)
cv.resizeWindow("thresholded1", 640, 480)
cv.imshow("thresholded1", thresholded)

result=lanecenter-framecenter
imag= cv.putText(imag,"{}".format(result),(0,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2, cv.LINE_AA)

cv.namedWindow("imag2", cv.WINDOW_KEEPRATIO)
cv.resizeWindow("imag2", 640, 480)
cv.imshow("imag2", imag)


        
cv.waitKey(0)