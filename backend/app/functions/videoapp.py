import cv2
import numpy as np
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.functions.face import Face
import streamlit as st
# from app.settings import setting
# camip=setting.CAM_IP
camip="192.168.0.100"



videorouter = APIRouter()

    


def video_feed():
    cap = cv2.VideoCapture("http://"+camip+":8080/video")
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        success, img = cap.read()
        x=Face(img)
        frame=x.facedefine()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    


@videorouter.get("/video_feed")
def stream():
    return StreamingResponse(video_feed(), media_type="multipart/x-mixed-replace; boundary=frame")
def fetch():
    st.write("hello")
    return "hello"


