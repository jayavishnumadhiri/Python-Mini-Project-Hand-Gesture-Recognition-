import cv2
import time
import pyttsx3
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
speech = pyttsx3.init()
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right

        fingers1 = detector.fingersUp(hand1)
        print(fingers1)

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmarks points
            bbox2 = hand2["bbox"]  # Bounding Box info x,y,w,h
            centerPoint2 = hand2["center"]  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type Left or Right

            fingers2 = detector.fingersUp(hand2)
            length, info, img = detector.findDistance(centerPoint1, centerPoint2, img)  # with draw
        if fingers1[0] == 1 and fingers1[1] == 1 and fingers1[2] == 1 and fingers1[3] == 1 and fingers1[4] == 1:
            speech.say("I am Hungry")
            speech.runAndWait()
        elif fingers1[0] == 1 and fingers1[1] == 1 and fingers1[2] == 1:
            speech.say("Need a help")
            speech.runAndWait()
        elif fingers1[0] == 1 and fingers1[1] == 1:
            speech.say("Call to Friend")
            speech.runAndWait()
        elif fingers1[0] == 1 and fingers1[2] == 1 and fingers1[3] == 1 and fingers1[4] == 1:
            speech.say("Where is washroom")
            speech.runAndWait()
        elif fingers1[1] == 1 and fingers1[2] == 1 and fingers1[3] == 1 and fingers1[4] == 1:
            speech.say("What is Your Name")
            speech.runAndWait()
        elif fingers1[2] == 1 and fingers1[3] == 1 and fingers1[4] == 1:
            speech.say("I am feeling Thirsty")
            speech.runAndWait()
        elif fingers1[1] == 1 and fingers1[2] == 1:
            speech.say("Can you switch on AC")
            speech.runAndWait()
        elif fingers1[1] == 1:
            speech.say("I am feeling Tired")
            speech.runAndWait()
        elif fingers1[0] == 1:
            speech.say("Can we go outside and play for a while")
            speech.runAndWait()
        elif fingers1[0] == 1 and fingers1[4] == 1:
            speech.say("can i get your number")
            speech.runAndWait()
        elif fingers1[0] == 1 and fingers1[3] == 1:
            speech.say("I am studying B.Tech")
            speech.runAndWait()
        elif fingers1[0] == 1 and fingers1[2] == 1:
            speech.say("I am feeling sick")
            speech.runAndWait()
        elif fingers1[1] == 1 and fingers1[3] == 1:
            speech.say("I stay at Nellore")
            speech.runAndWait()
        elif fingers1[1] == 1 and fingers1[4] == 1:
            speech.say("Sorry")
            speech.runAndWait()
        elif fingers1[2] == 1 and fingers1[4] == 1:
            speech.say("I am fine")
            speech.runAndWait()
        elif fingers1[3] == 1 and fingers1[4] == 1:
            speech.say("Thank you")
            speech.runAndWait()
        elif fingers1[2] == 1 and fingers1[3] == 1:
            speech.say("Help")
            speech.runAndWait()

    cv2.imshow("Image", img)
    cv2.waitKey(1)

