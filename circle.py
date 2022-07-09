import cv2

circle = cv2.imread("black.jpg")

cv2.circle(circle, (250,250), 200, (0,0,225), 5)

cv2.imshow("Circle",circle)

cv2.waitKey(10000)
