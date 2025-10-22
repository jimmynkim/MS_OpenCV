# 이미지 파일 읽고, 표시하고, 저장하기2
import cv2 as cv     
import sys     

img = cv.imread('Ch.02/soccer.jpg', cv.IMREAD_GRAYSCALE)     # 이미지 파일 흑백으로 읽기

if img is None:
    sys.exit('File Not Found')     

cv.imshow('Image Display', img)     

cv.imwrite('Ch.02/soccer2.jpg', img)     

cv.waitKey()     

cv.destroyWindow()     