### Ch.03 OpenCV 영상처리 기능 연습하기
## BGR 채널별 이미지 표현
import cv2 as cv
import numpy as np

# 1. 이미지 불러오기
img = cv.imread('Ch.03/RGB.jpg')     # 이미지 경로 지정
if img is None:
    raise FileNotFoundError("이미지 파일을 찾을 수 없습니다.")

Small_img = cv.resize(img, (700, 500)) 

# 2. 이미지 출력(OpenCV는 BGR 그대로 출력)
cv.imshow('Original Image', Small_img)
cv.imshow('Blue Channel', Small_img[:, :, 0])
cv.imshow('Green Channel', Small_img[:, :, 1])
cv.imshow('Red Channel', Small_img[:, :, 2])

# 3. 키 입력 대기 후 창 닫기
cv.waitKey(0)
cv.destroyAllWindows()