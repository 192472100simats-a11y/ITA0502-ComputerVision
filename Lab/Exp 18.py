import cv2

img=cv2.imread(r"C:\open cv\Input.jpeg",0)

sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)

cv2.imshow("Original",img)
cv2.imshow("Sobel Y",cv2.convertScaleAbs(sobely))

cv2.waitKey(0)
cv2.destroyAllWindows()
