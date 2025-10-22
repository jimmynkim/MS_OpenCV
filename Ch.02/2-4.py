## 이미지 파일에 도형과 글씨 추가하기
import cv2 as cv     
import sys     

img = cv.imread('Ch.02/girl.jpg')     

if img is None:
    sys.exit('File Not Found') 
    
# 이미지에 사각형 그리기 (최상단(330,470), 우하단(530,640), 파란색, 두께 3)
cv.rectangle(img, (330, 470), (530, 640), color=(255, 0, 0), thickness=3)

# 이미지에 텍스트 쓰기 ("Hello OpenCV", 위치(330,450), 폰트, 크기 1, 초록색, 두께 2)
cv.putText(img, "Hello OpenCV", org=(330, 450), fontFace=cv.FONT_HERSHEY_SIMPLEX,
           fontScale=1, color=(0, 255, 0), thickness=2)

cv.imshow('Image Display', img)

cv.waitKey()     

cv.destroyWindow()  