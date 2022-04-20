import cv2
import numpy as nu

def change(x):
    pass

video=cv2.VideoCapture('bolt_test_pothole.mp4')#allocating the video to a variable
"""
cv2.namedWindow('pothole_detection')  #creating a window

#creating and allocating channel values

cv2.createTrackbar('lowest value of h','pothole_detection',0,280,change)
cv2.createTrackbar('lowest value of s','pothole_detection',0,280,change)
cv2.createTrackbar('lowest value of v','pothole_detection',0,280,change)

cv2.createTrackbar('highest value of h','pothole_detection',200,200,change)
cv2.createTrackbar('highest value of s','pothole_detection',200,200,change)
cv2.createTrackbar('highest value of v','pothole_detection',200,200,change)
"""
#if the video is succesfully opened we enter while loop

while(video.isOpened()):
    rev,frame =video.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #converting the video into hsv mode
    """
    lower_bound_h =cv2.getTrackbarPos('lowest value of h', 'pothole_detection')
    lower_bound_s =cv2.getTrackbarPos('lowest value of s','pothole_detection')
    lower_bound_v =cv2.getTrackbarPos('lowest value of v','pothole_detection')

    higher_bound_h=cv2.getTrackbarPos('highest value of h','pothole_detection')
    higher_bound_s =cv2.getTrackbarPos('highest value of s','pothole_detection')
    higher_bound_v =cv2.getTrackbarPos('highest value of v','pothole_detection')
    
    #steps used for checking the appropriate value
    
    lowest = nu.array([lower_bound_h, lower_bound_s, lower_bound_v])
    highest = nu.array([higher_bound_h, higher_bound_s, higher_bound_v])
    pothole = cv2.inRange(hsv_frame, lowest, highest)
    final = cv2.bitwise_and(frame, frame, mask=pothole)

    """
    low=nu.array([0,0,142])   # obtained these values for pothole detection by using the above steps
    hig=nu.array([200,200,200])
    pothole=cv2.inRange(hsv_frame,low,hig)
    final=cv2.bitwise_and(frame,frame,mask=pothole)

    #Printing the results
    cv2.imshow('Original_video',frame)
    cv2.imshow('Resulting_Video',final)
    cv2.imshow('Pothole_Detection_HSV',pothole)

    #for exiting from the projected screen in between press "Escape key"
    key=cv2.waitKey(1) & 0xff
    if (key==27):
        break
#releaseing and destroying all windows
video.release()
cv2.destroyAllWindows()