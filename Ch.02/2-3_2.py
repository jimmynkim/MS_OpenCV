## 이미지 파일을 변환하기2 - resize
import cv2 as cv     
import sys     

img = cv.imread('Ch.02/soccer.jpg')     

if img is None:
    sys.exit('File Not Found') 
    
# 기존 이미지 사이즈 변경
Small_image = cv.resize(img, (400, 600))     # 너비 500, 높이 700

cv.imshow('Image Display', Small_image)

cv.waitKey()     

cv.destroyWindow()     