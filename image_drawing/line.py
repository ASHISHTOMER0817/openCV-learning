import cv2 as cv

img = cv.imread("./1/tiger.webp")

print(img.shape)
if img is None:
      print("not found")
else:
      print("image loaded successfully")
      pt1 = (150, 150)
      pt2 = (250, 250)
      color = (0, 0, 255)
      thickness = 4

      cv.line(img, pt1, pt2, color, thickness)
      cv.rectangle(img, pt1, pt2, color, thickness)
      cv.imshow("line drawing",img)
      cv.waitKey(0)
      cv.destroyAllWindows()

