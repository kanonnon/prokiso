import cv2
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
p = GPIO.PWM(4, 50)
p.start(0.0)

faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

def add_doraemon(img, rect):
    filename = "./doraemon.jpg"
    doraemon = cv2.imread(filename)
    
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1

    resized_doraeon = cv2.resize(doraemon, (w, h))

    added_doraemon = img.copy()
    added_doraemon[y1:y2, x1:x2] = resized_doraeon
    p.ChangeDutyCycle(4)
    
    return added_doraemon

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
    )
    
    for (x, y, w, h) in faces:
        img = add_doraemon(img, (x+10, y+10, x+w+10, y+h+10))
        
    cv2.imshow("video", img)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.detroyAllWindows()