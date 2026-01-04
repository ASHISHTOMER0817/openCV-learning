import cv2 as cv

img = cv.imread("./contours & shape detection/yellow.jpg")

if img is None:
      print('what is this')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh1 = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
_, thresh2 = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
cv.imshow("contours", gray)
cv.imshow("thresh1", thresh1 )
cv.imshow("thresh2", thresh2 )
cv.waitKey(0)
cv.destroyAllWindows()

#FIND CONTOURS
# contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# cv.drawContours(img, contours, -1, (0, 255, 0), 2)


# cv.imshow("contours", img)
# cv.waitKey(0)
# cv.destroyAllWindows()