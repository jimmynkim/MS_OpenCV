## 이미지 전처리(OpenCV)가 잘 작동되는지 실습 환경 구축
import cv2 as cv
import sys

img = cv.imread('Ch.02/soccer.jpg')

if img is None:
    sys.exit('File Not Found')

cv.imshow('Image Display', img)

cv.waitKey()
cv.destroyWindow()