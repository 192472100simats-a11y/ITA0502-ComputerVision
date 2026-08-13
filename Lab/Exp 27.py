import cv2

img1 = cv2.imread(r"C:\open cv\Input.jpeg")
img2 = cv2.imread(r"C:\open cv\AOT.jpeg")

crop = img1[20:200, 20:200]

crop = cv2.resize(crop, (150, 150))

img2[20:170, 20:170] = crop

cv2.imshow("Original Image 1", img1)
cv2.imshow("Output - Pasted Image", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
