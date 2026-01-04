import cv2 as cv


img = cv.imread("./cat.jpg")

blurred = cv.medianBlur(img, 11)

cv.imshow("blurred", blurred)
cv.imshow("original", img)

cv.waitKey(0)
cv.destroyAllWindows()