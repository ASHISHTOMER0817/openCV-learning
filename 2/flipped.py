import cv2 as cv

img = cv.imread("./1/tiger.webp")

if img is None:
      print("can find the image")
else:
      print("here is your image")
      flipped_horizontal = cv.flip(img, 1)
      flipped_vertical = cv.flip(img, 0)
      flipped_both = cv.flip(img, -1)

      cv.imshow("original", img)
      cv.imshow("horizontal", flipped_horizontal)
      cv.imshow("vertical", flipped_vertical)
      cv.imshow("flipped both", flipped_both)

      cv.waitKey(0)
      cv.destroyAllWindows()
