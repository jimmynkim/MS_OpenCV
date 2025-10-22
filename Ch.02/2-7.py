## 웹캠 촬영 영상을 모니터에 표시하기
import cv2 as cv

# 웹캠 열기 (기본 장치는 0번)
cap = cv.VideoCapture(0)

# 웹캠 열기에 실패했는지 확인
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()     # 한 프레임 읽기
    if not ret:
        print("프레임을 가져올 수 없습니다. 종료합니다.")
        break

    # 🔑 추가: 화면을 좌우 반전(수평 뒤집기)하는  코드
    frame = cv.flip(frame, 1) # 두 번째 인자 1은 수평(Horizontal) 뒤집기를 의미

    # 프레임을 창에 출력
    cv.imshow('Live Video', frame)

    # 키보드에서 'q'를 누르면 루프 종료
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 사용한 자원 해제
cap.release()
cv.destroyAllWindows()