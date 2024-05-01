import cv2
from app.settings import setting

class Camera:
    def __init__(self):
        self.cam = cv2.VideoCapture(f"http://{setting.CAM_IP}:{setting.CAM_PORT}/video")
        
    def get_frame(self):
        ret, frame = self.cam.read()
        if ret:
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
        else:
            return None

    def __del__(self):
        self.cam.release()
    
