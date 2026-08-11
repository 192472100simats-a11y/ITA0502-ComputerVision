import cv2
import numpy as np

img = cv2.imread(r"C:\open cv\Input.jpeg")

kernel = np.array([[0,-1,0],
                   [-1,4,-1],
                   [0,-1,0]])

lap = cv2.filter2D(img,-1,kernel)

sharp = cv2.add(img,lap)

cv2.imshow("Original",img)

cv2.imshow("Positive Center Laplacian",sharp)

cv2.waitKey(0)

cv2.destroyAllWindows()
