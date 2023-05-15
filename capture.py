import cv2
import os
import uuid

VERI_PATH = os.path.join('app', 'application_data', 'verification_images')
INP_PATH = os.path.join('app', 'application_data', 'input_image')

os.makedirs(VERI_PATH, exist_ok=True)
os.makedirs(INP_PATH, exist_ok=True)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (250, 250))
    if cv2.waitKey(1) & 0XFF == ord('c'):
        imgname = os.path.join(VERI_PATH, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgname, frame)

    cv2.imshow('Image Collection', frame)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
