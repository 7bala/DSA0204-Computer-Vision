import cv2
import numpy as np 
img = r'C:\\Movies\\Farzi_(2023)_S01_EP_(01-08)_HQ_HDRip_-_x264_-_[Tel_+_Tam]_ESub.mkv.mp4'
c=cv2.VideoCapture(img)
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[100,50],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
while True:
    a,r = c.read()
    dst = cv2.warpPerspective(r,M,(700, 700))
    cv2.imshow('Transformed Image', dst)
    cv2.waitKey(1)
