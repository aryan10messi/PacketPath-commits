import cv2

img=cv2.imread("image.png") # sets image to the variable

resized = cv2.resize(img, (400,500)) # gives the image you want to resize and the measurement you want to resize it to

cv2.imshow("Original", img)   # shows original image with title original
cv2.imshow("Resized", resized)  #shows resized image with title original

cv2.waitKey(10000) #keeps images up for 10 seconds
