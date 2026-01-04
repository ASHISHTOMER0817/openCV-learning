import cv2 as cv


camera = cv.VideoCapture(0)

# print(camera.read()[1])   ## frames include 3D array, each array includes H, w, 3, corresponds to pixel.

frame_width = int(camera.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))

codec = cv.VideoWriter.fourcc('X', 'V', 'I', 'D')
recorder = cv.VideoWriter("recording.avi", codec, 20, (frame_width, frame_height))

while True:
      ret, frame = camera.read()

      if not ret:
            break
      recorder.write(frame)
      cv.imshow("video playback", frame)

      if cv.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
recorder.release()
cv.destroyAllWindows()


