import cv2

img=cv2.imread(r"C:\open cv\Input.jpeg",0)

sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)

cv2.imshow("Original",img)
cv2.imshow("Sobel X",cv2.convertScaleAbs(sobelx))

cv2.waitKey(0)
cv2.destroyAllWindows()
