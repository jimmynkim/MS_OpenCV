## 이미지 파일을 변환하기 - cvtColor
import cv2 as cv     
import sys     

img = cv.imread('Ch.02/soccer.jpg')     

if img is None:
    sys.exit('File Not Found') 

# 기존 이미지를 Gray 이미지로 변환    
Gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)     

cv.imshow('Image Display', Gray_image)     

cv.waitKey()     

cv.destroyWindow()     