import cv2

face_detection = cv2.CascadeClassifier("face.xml")

count = 0
face = cv2.imread("face3.jpg") #change the .jpg file you want to use to check for faces.
gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
faceResult = face_detection.detectMultiScale(gray, 1.1,4)

for (x,y,w,h) in faceResult:
    print("I found a face!")
    count+=1
    cv2.rectangle(face, (x,y), (x+w, y+h), (255,0,0), 3)

if(count == 0):
    print("No face was found!")

cv2.imshow("Detection", face)
cv2.waitKey(0)
