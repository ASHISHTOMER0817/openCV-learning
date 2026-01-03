import cv2 as cv

img = cv.imread("./tiger.webp")

## TO CHECK IF IT EXISTS AND HAS BEEN CONVERTED TO NUMPY ARRAY
if img is None:
      print("why")
else:
      print("good")

## TO SHOW IMAGE
# cv.imshow("title", img)
# cv.waitKey(0)
# cv.destroyAllWindows()


## TO SAVE IMAGE
# success = cv.imwrite("tiger_copy.webp", img)
# if success:
#       print('successfully saved')
# else:
#       print("failed to save")


## image dimension -- (WIDTH, HEIGHT, CHANNEL{bgr if black and white - nothing})
print(img.shape)   ## it returns tupple


## GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray_img", gray)
cv.waitKey(0)
cv.destroyAllWindows()




