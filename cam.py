import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    cv2.imshow("webcam",img)
    k=cv2.waitKey(0)
    if cv2.waitKey(10):
        break
cap.release()
cv2.destroyAllWindows()
