import cv2
import numpy as np
image_path = "C:\\Users\\saran\\OneDrive\\Desktop\\CV programs\\sample1.jpg"
image = cv2.imread(image_path)
rows, cols, _ = image.shape
transformation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])
affine_image = cv2.warpAffine(image, transformation_matrix, (cols, rows))
cv2.imshow('Original Image', image)
cv2.imshow('Affine Transformed Image', affine_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
