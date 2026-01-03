import cv2 as cv

img = cv.imread("./1/tiger.webp")

if img is None:
      print("can't find")
else:
      print("yes found it")

cropped = img[100:200, 50:150]

cv.imshow("original", img)
cv.imshow("cropped", cropped)
cv.waitKey(0)
cv.destroyAllWindows() 