## 엠보싱 기법
## 정의: 이미지의 윤곽(에지, 경계선)을 강조하면서 음영을 주어 입체감을 표현하는 기법
import cv2 as cv
import numpy as np

# 이미지 불러오기
img = cv.imread('Ch.03/girl.jpg', cv.IMREAD_GRAYSCALE)
Small_img = cv.resize(img, (400, 600)) 

# 엠보싱 커널 정의
kernel = np.array([[-2, -1, 0],
                   [-1, 1, 1],
                   [0, 1, 2]], dtype=np.float32)

# 필터 적용(엠보싱)
embossed = cv.filter2D(Small_img, -1, kernel)

# 원래 이미지와 엠보싱 이미지 디스플레이
cv.imshow('Original', Small_img)
cv.imshow('Embossed', embossed)

cv.waitKey(0)
cv.destroyAllWindows()