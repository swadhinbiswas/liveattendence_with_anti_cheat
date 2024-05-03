import cv2
import time
import numpy as np

import pickle
from face_recognition import face_locations, face_encodings, compare_faces, face_distance

folderpath="/home/swadhin/GitHubproject/liveattendence_with_anti_cheat/backend/app/functions/pictures/222156259.jpeg"

pic=cv2.imread(folderpath)
pic=cv2.resize(pic,(0,0),None,0.25,0.25)
encode=face_encodings(pic)[0]
studentIds = ['222156259']
encodelist=[]
encodelist.append(encode)
incodelistnown=[encodelist,studentIds]
file=open('EncodeFile.p','wb')
pickle.dump(incodelistnown,file)
file.close()    


cap = cv2.VideoCapture("https://192.168.0.100:8080/video")
cap.set(3, 640)
cap.set(4, 480)

file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)

encodeListKnown, studentIds = encodeListKnownWithIds


while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faceCurFrame = face_locations(imgS)
    encodeCurFrame =face_encodings(imgS, faceCurFrame)
    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = compare_faces(encodeListKnown, encodeFace)
            faceDis = face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, studentIds[matchIndex], (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()

        
    
    
    
    

    
        
        


