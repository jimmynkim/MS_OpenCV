### Ch.04 OpenCV 엣지와 영역 검출
## Sobel 연산자를 활용한 엣지 검출
import cv2 as cv
import numpy as np

# 이미지 불러오기(그레이스케일)
img = cv.imread('Ch.04/soccer.jpg', cv.IMREAD_GRAYSCALE)
Small_img = cv.resize(img, (400, 600)) 

# Sobel 연산자 적용 (64F로 계산 후 절댓값, uint8 변환)
sobel_x = cv.Sobel(Small_img, cv.CV_64F, 1, 0, ksize=3)     # 수평 방향의 경계(수직 엣지)를 강조 
sobel_y = cv.Sobel(Small_img, cv.CV_64F, 0, 1, ksize=3)     # 수직 방향의 경계(수평 엣지)를 강조

# 엣지 강도 계산: sqrt(sobel_x^2 + sobel_y^2)
magnitide = np.sqrt(sobel_x**2 + sobel_y**2)     # x와 y 방향의 소벨 연산 결과를 가중합하여 엣지 강도 계산

# 정수형으로 변환
abs_sobel_x = cv.convertScaleAbs(sobel_x)
abs_sobel_y = cv.convertScaleAbs(sobel_y)
edge_strength = cv.convertScaleAbs(magnitide)

# 출력
cv.imshow('Original', Small_img)
cv.imshow('Sobel X', abs_sobel_x)
cv.imshow('Sobel Y', abs_sobel_y)
cv.imshow('Edge Strength (Magnitude)', edge_strength)

cv.waitKey(0)
cv.destroyAllWindows()