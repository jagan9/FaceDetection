import cv2

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('bbb.png')
video = cv2.VideoCapture(0)

while True:
	is_success, frame = video.read()

	grey_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	positions = face_detector.detectMultiScale(grey_frame)

	for (x,y,w,h) in positions:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)

	cv2.imshow("frame",frame)
	key = cv2.waitKey(1)

	if (key==81 or key==113):
		break;

video.release()


# grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# position = face_detector.detectMultiScale(grey_img)

# for (x,y,w,h) in position:
# 	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

# cv2.imshow("img",img)
# cv2.waitKey(0)

