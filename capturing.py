import cv2

webcam = cv2.VideoCapture(0) #change to 0 or 1 depending on what webcam you have. 0 works for the webcam on my mac.

i = 0

while(i<5): # for loop runs 10 times to take 10 images
    control, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #gray scale image capturing (single channel) -> easier to detect
    cv2.imshow("Frames", gray)
    cv2.waitKey(0)
    cv2.imwrite("count"+str(i)+".jpg", gray) #makes a new file every time enter is hit for up to 10 times.
    i=i+1
    if(cv2.waitKey(10) & 0xFF==ord("q")): #press q to exit the loop early
        break
