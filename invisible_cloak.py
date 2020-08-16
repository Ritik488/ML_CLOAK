import cv2
import numpy as np

cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
back = cv2.imread('./image.jpg')


while cap.isOpened():

    ret, frame = cap.read()

    if ret:

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv", hsv)

        #how to get the HSV value?
        #lower: -10, 100, 100, higher: h+10, 255, 255
        red = np.uint8([[[0,0,255]]]) #bgr value of red
        hsv_red =cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        #get hsv value of red from bgr
        # print(hsv_red)

        #threshold the hsv value to get only red color
        l_red = np.array([0,100,100])
        r_red = np.array([10,255,255])

        mask = cv2.inRange(hsv, l_red, r_red)
        # cv2.imshow("mask", mask)

        #all things red
        part1 = cv2.bitwise_and(back, back, mask=mask)
        # cv2.imshow("part1", part1)

        mask = cv2.bitwise_not(mask)

        #all things not red 
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("part2", part2)

        cv2.imshow("cloak", part1+part2)

        if cv2.waitKey(5)==ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
