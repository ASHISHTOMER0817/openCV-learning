import cv2 as cv

img = cv.imread("./1/tiger.webp")
#width, height

if img is None:
      print("not found")
else:
      (h, w) = img.shape[:2]
      center = (w//2, h//2)
      M = cv.getRotationMatrix2D(center, 135, 0.25)
      print(M)