## 영상 보간
## 의미: 알려진 데이터 포인트들을 이용해 그 사이의 알 수 없는 값을 추정하여 채워 넣는 작업
import cv2 as cv

# 이미지 불러오기
img = cv.imread('Ch.03/dog.jpg')
Small_img = cv.resize(img, (200, 300)) 

# 새 크기 지정 (예: 원본보다 2배 확대)
new_size = (Small_img.shape[1]*2, Small_img.shape[0]*2)

# 서로 다른 보간 방법으로 리사이즈
res_nearest = cv.resize(Small_img, new_size, interpolation=cv.INTER_NEAREST)     # 최근방 이웃 보간법, 빠르지만 이미지가 확대될 때 계단 현상발생
res_linear = cv.resize(Small_img, new_size, interpolation=cv.INTER_LINEAR)     # 선형 보간법, 더 부드러운 이미지 확장을 제공
res_cublic = cv.resize(Small_img, new_size, interpolation=cv.INTER_CUBIC)     # 3차 보간법으로, 이미지 확장 시 매우 부드러운 결과를 얻을 수 있지만 계산량이 많음

# 결과 출력
cv.imshow('Original', Small_img)
cv.imshow('INTER_NEAREST', res_nearest)
cv.imshow('INTER_LINEAR', res_linear)
cv.imshow('INTER_CUBIC', res_cublic)

cv.waitKey(0)
cv.destroyAllWindows()