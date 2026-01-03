import cv2 as cv

img = cv.imread("1/tiger.webp")

if img is None:
      print("Image can't found")
else:
      print("found it")

resized = cv.resize(img, (300, 300))
                        ##Width, height

cv.imshow("original image", img)
cv.imshow("resized image", resized)
cv.imwrite("resized_output.webp", resized)

cv.waitKey(0)
cv.destroyAllWindows()