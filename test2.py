
import cv2
import streamlit as st
from fastapi import FastAPI
import face_recognition
import numpy as np
import time
import os
from fastapi.responses import StreamingResponse
app = FastAPI()
from face_recognition import face_locations, face_encodings
from firebase_admin import db ,credentials

import firebase_admin


imagepath="/home/swadhin/GitHubproject/liveattendence_with_anti_cheat/backend/app/functions/pictures"
piclepath="/home/swadhin/GitHubproject/liveattendence_with_anti_cheat/backend/app/functions/encodings.pickle"

firbaseurl="https://database-faceapp-default-rtdb.asia-southeast1.firebasedatabase.app/"
servicekey="/home/swadhin/GitHubproject/liveattendence_with_anti_cheat/backend/app/settings/serviceAccountKey.json"


cred=credentials.Certificate(servicekey)

firebase_admin.initialize_app(cred,{
  'databaseURL': f'{firbaseurl}',
  'storageBucket': 'database-faceapp.appspot.com',
})

path="/home/swadhin/GitHubproject/liveattendence_with_anti_cheat/backend/app/functions/pictures/222156259.jpeg"
img=cv2.imread(path)
encodex=face_encodings(img)[0]
print(encodex)

@st.cache_resource
def get_cap():
    return 0

def detect_and_recognize_face(frame,encode):
    # Convert frame to RGB for face recognition
    
    cut_frame=cv2.resize(frame,(0,0),None,0.25,0.25)
    rgb_frame = cv2.cvtColor(cut_frame, cv2.COLOR_BGR2RGB)
    frameencode=face_encodings(rgb_frame)
    
    
    

    # Find all faces and their encodings
    face_locations_list = face_locations(rgb_frame)
    currentfaceencode = face_encodings(frameencode, face_locations_list)
    
    if face_locations_list:

    # Loop through each detected face
      for face_encoding, face_location in zip(currentfaceencode, face_locations_list):
          # Compare face encoding with encodings in database/pickle file
          matches = face_recognition.compare_faces(encode, face_encoding)
          facedistance=face_recognition.face_distance(encode,face_encoding)
          print(facedistance)
          name = "Unknown"
          matchindex=np.argmin(facedistance)
          print(matchindex)
          
          # Draw rectangle and name around the face
          top, right, bottom, left = face_location
          cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
          cv2.putText(frame, name, (left + 6, top - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

    return frame

def generate_frames():
  cap=cv2.VideoCapture("https://192.168.0.100:8080/video")
  cap.set(3,640)
  cap.set(4,480)
  while True:
        
        success, frame = cap.read()  # read the camera frame
        
        frame=detect_and_recognize_face(frame,encode=encodex)
        
        if not success:
              break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
        # save_image=cv2.imwrite(os.path.join(/home/swadhin/GitHubproject/liveattendence_with_anti_cheat/backend/app/functions/screens)"test.jpg",x)
        
      
        
        






# def video_feed():
#     cap = get_cap()  # 0 for default webcam
#     return StreamingResponse(generate_frames(cap), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/")
async def home():
    return {"message":"Welcome to the Live Attendance System"}
  

@app.get("/video_feed")
async def video_feed():
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace;boundary=frame")
  
def main():
  app.run()
  
if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(app, host="localhost", port=8000)
        