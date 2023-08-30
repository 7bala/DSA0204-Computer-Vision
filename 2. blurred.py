import cv2 as cv
image_path = "C:\\Users\\saran\\OneDrive\\Desktop\\CV programs\\sample1.jpg"
image = cv.imread(image_path)
blur = cv.GaussianBlur(image,(5,5),0)
cv.imshow('Original image ',image)
cv.imshow('Blurred image ',blur)
cv.waitKey(0)
cv.destroyAllWindows()
