## 감마(밝기) 보정
## 1을 기준으로 감마 값이 클수록 이미지가 어둡고, 명암 대비가 뚜렷해지며, 채도가 진해짐 
import cv2 as cv
import numpy as np

# 감마 보정 함수 (단일 이미지 처리)
def adjust_gamma(image, gamma):
    image1 = image / 255.0
    return np.uint8(255*(image1**gamma))

# 이미지 불러오기
img = cv.imread('Ch.03/dog.jpg')    
img = cv.resize(img, (300, 300))

# 감마 값 리스트
gammas = [0.5, 0.75, 1, 2, 3]    

# 각 감마값에 대해 이미지 처리 및 표시
for gamma in gammas:
    adjusted = adjust_gamma(img, gamma)
    window_name = f'Gamma {gamma}'
    cv.imshow(window_name, adjusted)

# 아무 키나 누를 때까지 대기 후 창 닫기
cv.waitKey(0)
cv.destroyAllWindows()