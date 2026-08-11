import cv2

img = cv2.imread(r"C:\open cv\Input.jpeg")

blur = cv2.GaussianBlur(img,(9,9),10)

sharp = cv2.addWeighted(img,1.5,blur,-0.5,0)

cv2.imshow("Original",img)

cv2.imshow("Unsharp Masking",sharp)

cv2.waitKey(0)

cv2.destroyAllWindows()
