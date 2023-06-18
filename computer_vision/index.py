# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2
import numpy as np

# capture frames from a video
cap = cv2.VideoCapture('video1.mp4')

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')
def on_click(event, x, y, p1, p2):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray, 1.465, 1)
    # To draw a rectangle in each cars


    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
    # # Coordinates that you want to Perspective Transform
    # pts1 = np.float32([[3,372],[551,598],[615,157],[886,199]])
    # # Size of the Transformed Image
    # pts2 = np.float32([[0,0],[500,0],[0,400],[500,400]])
    # for val in pts1:
    #     cv2.circle(frames,(val[0],val[1]),5,(0,255,0),-1)
    # M = cv2.getPerspectiveTransform(pts1,pts2)
    # frames = cv2.warpPerspective(frames,M,(500,400)) 
    cv2.imshow('video2',cv2.resize(frames,(500,400))) 
    cv2.setMouseCallback('video2', on_click)
	
	# Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break

# De-allocate any associated memory usage
cv2.destroyAllWindows()
