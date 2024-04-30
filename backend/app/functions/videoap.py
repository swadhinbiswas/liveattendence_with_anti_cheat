import cv2
cap = cv2.VideoCapture("http://192.168.0.103:3030/video")

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
cap.release()

cv2.destroyAllWindows()

# Path: liveattendence_with_anti_cheat/backend/app/functions/videoap.py