import cv2
import numpy as np

img=cv2.imread(r"C:\open cv\Input.jpeg")

rows,cols=img.shape[:2]
M=np.float32([[1,0,100],[0,1,50]])
shifted=cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("Original",img)
cv2.imshow("Translated Image",shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()
