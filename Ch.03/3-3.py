## 모폴로지 
## 정의: 디지털 이미지에서는 픽셀 집합의 형태적 특징을 처리하는 기법
import cv2 as cv
import numpy as np

# 1. 빈 흰 캔버스 생성
canvas = np.ones((200, 600), dtype=np.uint8) * 255

# 2. 'Signature' 텍스트를 붓글씨 느낌으로 그림
cv.putText(canvas, 'Signature', (30, 130), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 4, (0,), 8, cv.LINE_AA)

# 3. 이미지 이진화(글씨 흰색으로, 배경 검정색으로 반전)
_, binary = cv.threshold(canvas, 127, 255, cv.THRESH_BINARY_INV)

# 4. 모폴로지용 커널 생성(원형, 크기 7*7)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7, 7))

# 5. 모폴로지 연산 수행
erosion = cv.erode(binary, kernel, iterations=1)     # 침식(배경이 침투) / 객체 축소
dilation = cv.dilate(binary, kernel, iterations=1)     # 팽창(객체가 배경 침식) / 객체 확장
opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)     # 열림(침식 후 팽창) / 작은 잡음 제거
closing = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)     # 닫힘(팽창 후 침식) / 객체의 구멍 제거

# 6. 결과 출력
cv.imshow('Original Binary', binary)
cv.imshow('Erosion', erosion)
cv.imshow('Dilation', dilation)
cv.imshow('Opening', opening)
cv.imshow('Closing', closing)

cv.waitKey(0)
cv.destroyAllWindows()