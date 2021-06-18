# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 19:10:08 2021

@author: Aahan Birla
"""
import cv2
import numpy as np
import dlib

capture = cv2.videocapture(0)
detect = dlib.get_frontal_face_detector()
while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame,1)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detect(gray)
    i=0
    for face in faces:
        x,y = face.left(),face.top()
        x1,y1 = face.right(),face.bottom()
        cv2.rectangle(frame(x,y),(x1.y1),(0,25,0),2)
        i = i+1
        cv2.putText(frame,'face num'+str(i),(x-10,y-10),
            cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        print(face,i)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    