## 이진화 알고리즘 - 오츄(OTSU) 알고리즘
## 정의: 이미지의 히스토그램을 분석하여 두 개의 클래스(배경과 객체)간의 분산이 최대가 되는 임계값을 자동으로 찾아주는 방법
## 방법: 픽셀값을 기준으로 두 그룹(배경/객체)로 나누되 두 그룹간의 분산(분리도)가 가장 큰 지점을 임계값으로 설정
import cv2 as cv

# 이미지 불러오기
img = cv.imread('Ch.03/dog.jpg', cv.IMREAD_GRAYSCALE)

# 오츄 이진화 적용
ret, binary_img = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

print("자동 계산된 임계값:", ret)

# 결과 출력
cv.imshow('Original', img)
cv.imshow('Otsu Threshoulding', binary_img)
cv.waitKey(0)
cv.destroyAllWindows()