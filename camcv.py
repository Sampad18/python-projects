import cv2
import sys
import numpy as np
c = cv2.VideoCapture(0)
if not c.isOpened():
    print("cannot open camera!")
    exit()

while True:
    ret,frame = c.read()
    if not ret:
        print('error')
        break
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow("webcam",hsv)
    if cv2.waitKey(1)==ord(" "):
        break
c.release()
cv2.destroyAllWindows()
