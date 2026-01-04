import cv2 as cv


cap = cv.VideoCapture(0)

while True:
      ret, frame = cap.read()  #ret = True/ False frame = image

      if not ret:
            print("could not read frame")
            break

      cv.imshow("webcam Feed", frame)

      if cv.waitKey(1) & 0xFF == ord('q'):  ## 113 == 113 True
            print("Quitting...")
            break

cap.release()      ## to close the recording and deallocates the memory.
cv.destroyAllWindows()