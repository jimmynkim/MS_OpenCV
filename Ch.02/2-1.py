import cv2 as cv     # OpenCV 라이브러리 가져오기
import sys     # 시스템 종료 등의 기능을 위한 sys 모듈 가져옴

img = cv.imread('Ch.02/soccer.jpg')     # 이미지 파일 읽기

if img is None:
    sys.exit('File Not Found')     # 이미지 파일을 찾을 수 없으면 프로그램 종료

cv.imshow('Image Display', img)     # 이미지 화면에 출력

cv.imwrite('Ch.02/soccer2.jpg', img)     # 이미지를 새로운 파일로 저장

cv.waitKey()     # 키보드 입력이 있을 때까지 대기

cv.destroyWindow()     # 열려 있는 모든 OpenCV 창 닫기