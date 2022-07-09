import cv2

rect = cv2.imread("black.jpg")

cv2.rectangle(rect, (100,100), (400,400), (200,0,200), 3 )

cv2.imshow("Rectangle",rect)

cv2.waitKey(10000)
