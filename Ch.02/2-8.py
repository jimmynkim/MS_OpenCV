## 웹캠에서 캡쳐한 영상을 메모리에 저장하기
import cv2 as cv

# 웹캠 열기 (기본 장치는 0번)
cap = cv.VideoCapture(0)

# 웹캠 열기에 실패했는지 확인
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

captured_images = []     # 캡쳐된 이미지 저장용 리스트

print("▶ 'a' 키: 한 장 캡쳐, 'q' 키: 캡쳐 이미지 보기 및 종료")

while True:
    ret, frame = cap.read()     # 한 프레임 읽기
    if not ret:
        print("프레임을 가져올 수 없습니다. 종료합니다.")
        break

    # 🔑 추가: 화면을 좌우 반전(수평 뒤집기)하는  코드
    frame = cv.flip(frame, 1) # 두 번째 인자 1은 수평(Horizontal) 뒤집기를 의미

    # 프레임을 창에 출력
    cv.imshow('Live WebCam', frame)
    key = cv.waitKey(1) & 0xFF

    if key == ord('a'):
        # 현재 프레임을 복사해서 저장
        captured_images.append(frame.copy())
        print(f"📸 {len(captured_images)}번째 이미지 캡쳐됨")

    elif key == ord('q'):
        print(f"🖼️ 총 {len(captured_images)}장의 이미지가 캡쳐되었습니다.")
        break

# 사용한 자원 해제
cap.release()
cv.destroyAllWindows()

# 캡쳐된 이미지들을 하나씩 보여주기
for idx, img in enumerate(captured_images):
    cv.imshow(f'Captured Image {idx+1}', img)
    cv.waitKey(0)     # 아무 키 누르면 다음 이미지로

cv.destroyAllWindows()