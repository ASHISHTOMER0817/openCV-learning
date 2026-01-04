import cv2 as cv

img = cv.imread("./1/tiger.webp")

if img is None:
      print("sorry! can't find image")
else:
      blurred = cv.GaussianBlur(img, )

cv.imshow("original", img)
cv.imshow("blurred", blurred)
cv.waitKey(0)
cv.destroyAllWindows()
