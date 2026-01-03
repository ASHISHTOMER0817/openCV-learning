resized = cv.resize(img, (300, 300))

cv.imshow("original image", img)
cv.imshow("resized image", resized)
cv.imwrite("resized_output.webp", resized)

cv.waitKey(0)a
cv.destroyAllWindows