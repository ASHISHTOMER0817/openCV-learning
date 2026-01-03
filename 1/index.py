import cv2
import numpy as np
import pandas as pd
import os
print(os.getcwd())
img = cv2.imread("./tiger.webp", 0)

if img is None:
      print("can't find img")
else:
      print("found it")

# imshow
# waitkey
# destroyAllWindows

cv2.imshow("window title", img)
cv2.waitKey(0)
cv2.destroyAllWindows()      