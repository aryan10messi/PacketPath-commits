import cv2

black =cv2.imread("black.jpg")

cv2.line(black, (55,50), (200,100), (255, 0, 0), 2)
cv2.imshow("Lines", black)

cv2.waitKey(10000)
