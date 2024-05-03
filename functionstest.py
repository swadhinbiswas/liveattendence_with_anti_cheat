# import os
# import cv2
# import face_recognition
# from firebase_admin import credentials
# from firebase_admin import db,storage
# import firebase_admin


# image_dir=os.listdir("/home/swadhin/GitHubproject/liveattendence_with_anti_cheat/backend/app/functions/pictures")


# from firebase_admin import credentials
# from firebase_admin import db 


# imagepath="/home/swadhin/GitHubproject/liveattendence_with_anti_cheat/backend/app/functions/pictures"

# firbaseurl="https://database-faceapp-default-rtdb.asia-southeast1.firebasedatabase.app/"
# servicekey="/home/swadhin/GitHubproject/liveattendence_with_anti_cheat/backend/app/settings/serviceAccountKey.json"


# cred=credentials.Certificate(servicekey)

# firebase_admin.initialize_app(cred,{
#   'databaseURL': f'{firbaseurl}',
#   'storageBucket': 'database-faceapp.appspot.com',
# })
# # imagelist=os.listdir(imagepath)
# # print(imagelist)
# # buket=storage.bucket()

# # for img in imagelist:
# #   images=buket.get_blob(f"faceappimage/{img}")
# #   print(img)
# #   if not images:
# #    with open(f"{imagepath}/{img}","rb") as file:
# #     buket.blob(f"faceappimage/{img}").upload_from_file(file)

# # x=buket.list_blobs()
# # print(x)
  
# # ref=db.reference('ids')

# # x=ref.get()
# # print(x)

# # imageList=os.listdir(imagepath)



# # for img in imageList:
  
# #   id=img.split(".")[0]
# #   if not ref.child(id).get():
# #     if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg"):
# #         cv2img=cv2.imread(f"{imagepath}/{img}")
# #         img=cv2.cvtColor(cv2img,cv2.COLOR_BGR2RGB)
# #         encode=face_recognition.face_encodings(img)[0]
# #         ref.child(id).set(encode.tolist())
        
    

  


# # test={
# #   "img1":"swadhin", 
# #   "img2":"swadhin",
# #   "img3":"swadhin",
# #   "img4":"swadhin",
# #   "img5":"swadhin",
# # }

# # x=test.keys()
# # for i in x:
# #   print(i)


# # ids=['1','2','3','4','5','6','7','8','9','10']

# # id=[[1],[23],[4],5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# # known_face_encodings = [ids,id]

# # print(known_face_encodings)


# imageList=os.listdir(imagepath)
# for img in imageList:
#      bucket=storage.bucket()
#      if not bucket.get_blob(f"faceappimage/{img}"):
#       with open(f"{imagepath}/{img}","rb") as file:
#        x=bucket.blob(f"faceappimage/{img}").upload_from_file(file)
#        print(x)


# import os
# import pickle
# import face_recognition
# import cv2
# import numpy as np
# import cvzone
# from typing import Dict,Any




# cap=cv2.VideoCapture(0)

# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)
  
# while True:
#     _,img=cap.read()
#     cv2.imshow("FaceApp",img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break
# cap.release()

# cv2.destroyAllWindows()
    
  

# import cv2
# import time
# import uvicorn
# from fastapi import FastAPI, Request,WebSocket, WebSocketDisconnect
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import StreamingResponse






# from fastapi import FastAPI, StreamingResponse


# app = FastAPI()

# def generate_frames(cap):
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break
#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                 b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.get("/video_feed")
# async def video_feed():
#     cap = cv2.VideoCapture("https://192.168.0.103:3030/video")  # 0 for default webcam
#     return StreamingResponse(generate_frames(cap), media_type="multipart/x-mixed-replace;boundary=frame")

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)


# app=FastAPI()

# face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

# async def get_frame():
#   camera=cv2.VideoCapture("https://192.168.0.103:3030/video")
#   while True:
#     success,frame=camera.read()
#     if not success:
#       break
#     else:
#       ret,buffer=cv2.imencode('.jpg',frame)
#       frame=buffer.tobytes()
#       yield(b'--frame\r\n'
#             b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n')
#     time.sleep(0.01)
    
# @app.get('/')
# async def index():
  
#   return StreamingResponse(get_frame(),media_type='multipart/x-mixed-replace; boundary=frame')


# from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
# from fastapi.responses import HTMLResponse
# from websockets.exceptions import ConnectionClosed
# from fastapi.templating import Jinja2Templates
# import uvicorn
# import asyncio
# import cv2


# app = FastAPI()
# camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)



# @app.get('/')
# def index(request: Request):
  
#     return HTMLResponse("""
#                         <!DOCTYPE html>
# <html>
#     <head>
#         <title>Live Streaming</title>
#     </head>
#     <body>
#         <img id="frame" src="">
#         <script>
#             let ws = new WebSocket("ws://localhost:8000/ws");
#             let image = document.getElementById("frame");
#             image.onload = function(){
#                 URL.revokeObjectURL(this.src); // release the blob URL once the image is loaded
#             } 
#             ws.onmessage = function(event) {
#                 image.src = URL.createObjectURL(event.data);
#             };
#         </script>
#     </body>
# </html>
                        
#                         """)


# @app.websocket("/ws")
# async def get_stream(websocket: WebSocket):
#     await websocket.accept()
#     try:
#         while True:
#             success, frame = camera.read()
#             if not success:
#                 break
#             else:
#                 ret, buffer = cv2.imencode('.jpg', frame)
#                 await websocket.send_bytes(buffer.tobytes()) 
#             await asyncio.sleep(0.03)
#     except (WebSocketDisconnect, ConnectionClosed):
#         print("Client disconnected")   

 
# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)


# img=cv2.cvtColor(cv2img,cv2.COLOR_BGR2RGB)
# encode=face_recognition.face_encodings(img)[0]
# encodeListknown=[encode,'222156259']
# success, frame = cap.read()
# imagesmall=cv2.resize(frame,(0,0),None,0.25,0.25)
# imagesmall=cv2.cvtColor(imagesmall,cv2.COLOR_BGR2RGB)
# facesCurFrame=face_recognition.face_locations(imagesmall)
# encodecurrentframe=face_recognition.face_encodings(imagesmall,facesCurFrame)
# if  facesCurFrame:
#   for encodeface,faceloc in zip(encodecurrentframe,facesCurFrame):
#       matches=face_recognition.compare_faces(encodeListknown,encodeface)
#       facedis=face_recognition.face_distance(encodeListknown,encodeface)
#       matchindex=np.argmin(facedis)
#       if matches[matchindex]:
#           name="Swadhin"
#           y1,x2,y2,x1=faceloc
#           y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
#           cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
#           cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
#           cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)


import cv2
import numpy as np
from face_recognition import face_encodings, face_locations, compare_faces, face_distance 


path="/home/swadhin/GitHubproject/liveattendence_with_anti_cheat/backend/app/functions/pictures/222156259.jpeg"
img=cv2.resize(cv2.imread(path),(0,0),None,0.25,0.25)
encodex=face_encodings(img)[0]

frame="/home/swadhin/GitHubproject/liveattendence_with_anti_cheat/backend/app/functions/pictures/222156259.jpeg"

def detect_and_recognize_face(frame,encode):
    # Convert frame to RGB for face recognition
    frame=cv2.imread(frame)
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
          matches = compare_faces(encode, face_encoding)
          facedistance=face_distance(encode,face_encoding)
  
          matchindex=np.argmin(facedistance)
          print(matchindex)
            


detect_and_recognize_face(frame,encodex)