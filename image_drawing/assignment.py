## ask user to provide file location.
## Ask user to choose one of the options, options are - line, circle, rectangle, text
## Now ask him the coordinates.
## Ask him if he wants to save the file or not.


import cv2 as cv
import questionary as ques
def img_cr(image_loc, shape, pt1, pt2, text, save):

      img = cv.imread(image_loc)
      if img is None:
            print("failed to load")
            return
      
      thickness = 4
      color = (255, 0, 0)
      if shape == "line":
            cv.line(img, pt1, pt2, color, thickness)
      elif shape == "circle":
            cv.circle(img, pt1, 20, color, thickness = 4)
      elif shape == "rectangle":
            cv.rectangle(img, pt1, pt2, color, thickness)
      else:
            cv.putText(img, text, pt1, 4, 1, color = color)

      if save == "y":
            cv.imwrite("copy_cat.webp", img)

      cv.imshow("image" + shape, img)
      cv.waitKey(0)
      cv.destroyAllWindows()


print("hello user")

file_path = ques.path("Select a file:").ask()

shape = ques.select("Choose one shape/text:", choices = ["circle", "rectangle", "line", "text"]).ask()

print('first point coordinates')
# print('second point coordinates')
pt1_x = int(input("x-axis: "))
pt1_y = int(input("y-axis: "))
pt2_x = 0
pt2_y = 0
txt = ""
if shape == "rectangle" or shape == "line":
      print("second point coordinates")
      pt2_x = int(input("x-axis: "))
      pt2_y = int(input("y-axis: "))
if shape == "text":
      txt = input("write the text: ")

save = input("Write 'y' to save 'n' for no : ")

img_cr(file_path, shape, (pt1_x, pt1_y), (pt2_x, pt2_y), txt, save)



