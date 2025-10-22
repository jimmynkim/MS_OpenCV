## 마우스를 이용하여 이미지에 사각형 그리기
import cv2 as cv

# 전역변수 선언
drawing = False     # 마우스 클릭 상태 저장(드래그 중인지 여부)
start_point = (-1, -1)     # 시작점
end_point = (-1, -1)     # 끝점

# 마우스 콜백 함수 정의
def draw_rectangle(event, x, y, flags, param):
    global drawing, start_point, end_point, Small_img, temp_img

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        end_point = (x, y)
        temp_img = Small_img.copy()     # 드래그 시작 시 이미지 복사
    
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            end_point = (x, y)
            temp_img = Small_img.copy()
            cv.rectangle(temp_img, start_point, end_point, (255, 0, 0), 2)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        cv.rectangle(Small_img, start_point, end_point, (255, 0, 0), 2)
        temp_img = Small_img.copy()

# 이미지 로드
img = cv.imread('Ch.02/girl.jpg')
if img is None:
    print('이미지 파일을 찾을 수 없습니다.')
    exit()

Small_img = cv.resize(img, (500, 700))
temp_img = Small_img.copy()

# 윈도우 생성 및 마우스 콜백 등록
cv.namedWindow('Draw Rectangle')
cv.setMouseCallback('Draw Rectangle', draw_rectangle)

# 루프를 돌면서 이미지 표시
while True:
    cv.imshow('Draw Rectangle', temp_img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:     # ESC 키를 누르면 종료
        break

cv.destroyAllWindows()