import cv2
import numpy as np
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.functions.face import Face
import streamlit as st 
from app.functions.encodeGenarator import EndcodeGenarator
from app.functions.getfacefromdatabase import GetgaceandData
import asyncio
# from app.settings import setting
# camip=setting.CAM_IP
camip="http://192.168.0.101:3030/video"



videorouter = APIRouter()

class Videofeed:
    def __init__(self):
        self.cap = cv2.VideoCapture(camip)
        self.data={}
        self.cap.set(3, 640)
        self.cap.set(4, 480)
    def video_feed(self):
        while True:
            success, img = self.cap.read()
            x=Face(img)
            frame=x.facedefine()
            self.data=x.get_student_id()
            if not success:
                break
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    
    def __del__(self):
        self.cap.release()
    def retunx(self):
        print(self.data)
        return self.data
        
        

def video_feed():
    
    cap = cv2.VideoCapture(camip)
    cap.set(3, 640)
    cap.set(4, 480)

    while True:
        success, img = cap.read()
        x=Face(img)
        frame=x.facedefine()
        
        y=x.get_student_id()
      
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
    

    


@videorouter.get("/video_feed")
async def stream():
    x=Videofeed()
    
    return StreamingResponse(x.video_feed(), media_type="multipart/x-mixed-replace; boundary=frame")

@videorouter.get("/user")
async def user():
    x=Videofeed()
    y=x.retunx()
    return y
   

@videorouter.get("/encode")
async def encode():
    x=EndcodeGenarator()
    y=x.findencoding()
    return y

@videorouter.get("/video")
def video():
    return st.markdown(f'<iframe width="560" height="315" src="http://{camip}:3030/video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', unsafe_allow_html=True)

@videorouter.get("/genarateface")
def genarateface():
   pass

@videorouter.get("/getstudentsphotos")
async def getstudentsphotos():
    x=GetgaceandData().get_picture()
    return x

@videorouter.get("/getstudentsdata")
async def getstudentsdata():
    x=GetgaceandData().get_data_by_key()
    return x

@videorouter.get("/getid")
async def getid():
   x=video_feed()
   