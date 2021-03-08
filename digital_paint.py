import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

# Hue min, Sat min, Value min, Hue max, Sat, max, Value max
myColors = [
    [104, 126, 43, 143, 201, 125],  # blue marker
    [120, 53, 25, 144, 120, 255],  # purple marker
    [155, 88, 0, 176, 160, 162],  # fuchsia marker
]

myColorValues = [  # BGR
    [134, 86, 17],
    [189, 15, 134],
    [171, 15, 189],
]

myPoints = []  # [x, y, colorId]



def findColor(img, myColors, myColorValues):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv.circle(imgResult, (x, y), 10, myColorValues[count], cv.FILLED)
        if x != 0  and y != 0:
            newPoints.append([x, y, count])
        count += 1
        # cv.imshow(str(color[0]), mask)
    return newPoints

def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
            # cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
    return x + w // 2, y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv.imshow('Result', imgResult)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
