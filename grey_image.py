import cv2

img=cv2.imread("image.png") #assigns image to read to img variable

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #color function to chang ecolor and asign it to a variable

cv2.imshow("Original Image", img) #shows original image
cv2.imshow("Gray Image", gray)  #shows gray image

cv2.waitKey(10000) #displays image for alloted time
