import cv2 as cv
image_path = "C:\\Users\\saran\\OneDrive\\Desktop\\CV programs\\sample1.jpg"
image = cv.imread(image_path)
grayimage = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('Original Image',image)
cv.imshow('Gray Scale Image',grayimage)
cv.waitKey(0)
cv.destroyAllWindows()
