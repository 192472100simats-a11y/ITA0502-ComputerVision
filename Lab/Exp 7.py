import cv2
import time

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if not ret:
        break

    cv2.imshow("Video",frame)

    k=cv2.waitKey(1)&0xFF

    if k==ord('s'):
        time.sleep(0.1)

    if k==ord('f'):
        time.sleep(0.01)

    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
