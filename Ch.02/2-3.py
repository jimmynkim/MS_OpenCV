## 이미지 파일을 변환하기 - resize
import cv2 as cv     
import sys     

img = cv.imread('Ch.02/soccer.jpg')     

if img is None:
    sys.exit('File Not Found') 
    
# 기존 이미지를 축소
Small_image = cv.resize(img, dsize=(0,0), fx=0.3, fy=0.3)     # 가로, 세로를 각각 30%로 축소

cv.imshow('Image Display', Small_image)

cv.waitKey()     

cv.destroyWindow()     