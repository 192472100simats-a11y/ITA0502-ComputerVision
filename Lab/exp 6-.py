import cv2

# Read the captured video
cap = cv2.VideoCapture("captured_video.mp4")

# Normal speed
while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Normal Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# Slow motion
cap = cv2.VideoCapture("C:\open cv\WIN_20260811_14_56_18_Pro.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Slow Motion", frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# Fast motion
cap = cv2.VideoCapture("captured_video.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Fast Motion", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
