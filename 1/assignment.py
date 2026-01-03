# a) load the image
# b) grayscale the image
# c) show it and save it
# challenges -- user input -- ask him if he wants to see it or save it,
# ask him file name and show save successfully.


import cv2 as cv
import os
print(os.getcwd())
img = cv.imread("./1/tiger.webp")
if img is None:
    print("not found")
else:
    print("found it")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# print("save it or see it")
prompt = input("write 'show' to see or 'save' to save it")
if prompt == "show":
      cv.imshow("gray img", gray)
      cv.waitKey(0)
      cv.destroyAllWindows()
elif prompt == "save":
      file_name = input("file name: ")
      cv.imwrite(file_name + ".webp", gray)
      print("saved successfully")
