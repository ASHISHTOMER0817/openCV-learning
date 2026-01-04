import cv2 as cv

img = cv.imread("./contours & shape detection/yellow.jpg")

if img is None:
      print('what is this')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh1 = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
_, thresh2 = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
cv.imshow("contours", gray)
cv.imshow("thresh", thresh1 )
cv.imshow("thresh", thresh2 )
cv.waitKey(0)
cv.destroyAllWindows()
