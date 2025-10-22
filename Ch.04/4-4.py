## GrabCut(사용자 상호작용)을 활용해 배경 제거하기
import cv2 as cv
import numpy as np

# 초기 설정
drawing = False
value = cv.GC_PR_FGD  # 기본은 왼쪽 클릭 → 물체
ix, iy = -1, -1

# 마우스 이벤트 콜백 함수
def draw_mask(event, x, y, flags, param):
    global drawing, ix, iy, value, mask, image_display

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        value = cv.GC_FGD  # 확실한 물체
        ix, iy = x, y

    elif event == cv.EVENT_RBUTTONDOWN:
        drawing = True
        value = cv.GC_BGD  # 확실한 배경
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.line(mask, (ix, iy), (x, y), value, 5)
            color = (0, 0, 255) if value == cv.GC_BGD else (0, 255, 0)
            cv.line(image_display, (ix, iy), (x, y), color, 5)
            ix, iy = x, y

    elif event == cv.EVENT_LBUTTONUP or event == cv.EVENT_RBUTTONUP:
        drawing = False

# 이미지 읽기 및 초기화
image = cv.imread('Ch.04/soccer.jpg')
Small_img = cv.resize(image, (400, 600)) 
image_display = Small_img.copy()
mask = np.full(Small_img.shape[:2], cv.GC_PR_BGD, dtype=np.uint8)  # 전경/배경 정보를 가진 마스크, 기본은 불확실 배경

cv.namedWindow('Input')
cv.setMouseCallback('Input', draw_mask)

print("왼쪽 클릭 → 물체, 오른쪽 클릭 → 배경, 그린 후 Enter 누르면 GrabCut 수행")

while True:
    cv.imshow('Input', image_display)
    key = cv.waitKey(1)

    if key == 13:  # Enter 키
        break
    elif key == 27:  # ESC 키
        cv.destroyAllWindows()
        exit()

# GrabCut 초기화용 배열
bgdModel = np.zeros((1, 65), np.float64)     # 내부적으로 사용하는 배경 모델 배열
fgdModel = np.zeros((1, 65), np.float64)     # 내부적으로 사용하는 전경 모델 배열

# GrabCut 적용
cv.grabCut(Small_img, mask, None, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_MASK)

# 결과 마스크 생성: 0,2=배경 / 1,3=물체
result_mask = np.where((mask == cv.GC_FGD) | (mask == cv.GC_PR_FGD), 255, 0).astype('uint8')

# 결과 적용
output = cv.bitwise_and(Small_img, Small_img, mask=result_mask)

# 결과 보기
cv.imshow('Extracted Object', output)
cv.waitKey(0)
cv.destroyAllWindows()