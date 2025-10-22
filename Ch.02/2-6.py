## 마우스를 이용하여 이미지에 페인팅 해보기
import cv2 as cv

# 마우스 이벤트 콜백 함수
def draw(event, x, y, flags, param):
    global drawing_left, drawing_right, img

    # 왼쪽 버튼 클릭 -> 드래그 시작
    if event == cv.EVENT_LBUTTONDOWN:
        drawing_left = True

    # 왼쪽 버튼 드래그 중
    elif event == cv.EVENT_MOUSEMOVE and drawing_left:
        cv.circle(img, (x, y), 5, (255, 0, 0), -1)     # 파란색 원

    # 왼쪽 버튼 드래그 종료
    elif event == cv.EVENT_LBUTTONUP:
        drawing_left = False

    # 오른쪽 버튼 클릭 -> 드래그 시작
    elif event == cv.EVENT_RBUTTONDOWN:
        drawing_right = True

    # 오른쪽 버튼 드래그 중
    elif event == cv.EVENT_MOUSEMOVE and drawing_right:
        cv.circle(img, (x, y), 5, (0, 0, 255), -1)     # 빨간색 원

    # 오른쪽 버튼 드래그 종료
    elif event == cv.EVENT_RBUTTONUP:
        drawing_right = False

# 이미지 준비
img = cv.imread('Ch.02/soccer.jpg')
if img is None:
    print('이미지를 불러올 수 없습니다.')
    exit()

# 드래그 상태 플래그
drawing_left = False
drawing_right = False

# 창 생성 및 마우스 콜백 연결
cv.namedWindow('Draw Circles')
cv.setMouseCallback('Draw Circles', draw)

# 루프를 돌며 이미지 출력
while True:
    cv.imshow('Draw Circles', img)
    key = cv.waitKey(1) & 0xFF
    if key == 27:     # ESC 키
        break

cv.destroyAllWindows()