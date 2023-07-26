

import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import math
from time import sleep
from pynput.keyboard import Key,Controller

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)

keys = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
    ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
    ["", "", "Space", "<---"],
]

finalText = ""

#simulating keyboard outside ide
keyboard = Controller()

def draw(img, buttonList):
    overlay = img.copy()
    alpha = 0.5  # Opacity of the overlay

    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv.rectangle(overlay, button.pos, (x + w, y + h), (255, 0, 0), cv.FILLED)
        cv.putText(overlay, button.text, (x + 20, y + 65), cv.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

    img = cv.addWeighted(overlay, alpha, img, 1 - alpha, 0)

    return img

class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.text = text
        self.size = size

buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        if key == "Space":
            buttonList.append(Button([100 * j + 50, 100 * i + 50], key, size=[300, 85]))  # space button
        elif key == "<---":
            buttonList.append(Button([100 * j + 350, 100 * i + 50], key, size=[200, 85]))  # Backspace button
        elif key != "":
            buttonList.append(Button([100 * j + 50, 100 * i + 50], key))  # Normal button

while True:
    success, img = cap.read()
    img = cv.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    img = draw(img, buttonList)
    if hands:
        for hand in hands:
            lmList = hand["lmList"]
            bbox = hand["bbox"]

            if lmList:
                for button in buttonList:
                    x, y = button.pos
                    w, h = button.size

                    if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                        cv.rectangle(img, button.pos, (x + w, y + h), (150, 60, 0), cv.FILLED)
                        cv.putText(img, button.text, (x + 20, y + 65), cv.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)

                        point1 = lmList[8]
                        point2 = lmList[12]
                        length = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
                        if length < 30:
                            cv.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv.FILLED)
                            cv.putText(img, button.text, (x + 20, y + 65), cv.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                            # Decrease opacity of the keys
                            cv.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), -1)

                            if button.text == "Space":
                                finalText += " "
                                keyboard.press(Key.space)
                            elif button.text == "<---":
                                finalText = finalText[:-1]
                                keyboard.press(Key.backspace)
                            else:
                                finalText += button.text
                                keyboard.press(button.text)

                            sleep(0.15)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

    cv.rectangle(img, (50, 450), (700, 550), (255, 255, 255), cv.FILLED)
    cv.putText(img, finalText, (60, 525), cv.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 4)

    cv.imshow("Image", img)
    cv.waitKey(1)

