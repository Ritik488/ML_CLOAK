import cv2
#This is my webcam
cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)


while cap.isOpened():
    ret, back =  cap.read() #Here I'm simply reading the frame
    if ret: 
        cv2.imshow("image", back)
        #back is what the camera is reading 
        if cv2.waitKey(5)==ord('q'):
            #Save the image
            cv2.imwrite('image.jpg', back)
            break
cap.release()
cv2.destroyAllWindows()
