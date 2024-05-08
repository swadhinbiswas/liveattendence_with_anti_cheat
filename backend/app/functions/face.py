import os
import pickle
import cv2
import numpy as np


from face_recognition import face_locations, face_encodings, compare_faces, face_distance
class Face():
  def __init__(self,frame):
    self.frame=frame
    self.ids=[]
  def facedefine(self):
    frame=self.frame
    filepath=os.path.join(os.path.dirname(__file__), "encodings.pickle")
    file = open(filepath, 'rb')
    encodeListKnownWithIds = pickle.load(file) 

    encodeListKnown, studentIds = encodeListKnownWithIds
    imgs=cv2.resize(frame,(0,0),None,0.25,0.25)
    imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
    faceCurFrame=face_locations(imgs)
    encodeCurFrame=face_encodings(imgs,faceCurFrame)
    if faceCurFrame:
      for encodeFace,faceLoc in zip(encodeCurFrame,faceCurFrame):
        matches=compare_faces(encodeListKnown,encodeFace)
        faceDis=face_distance(encodeListKnown,encodeFace)
        matchIndex=np.argmin(faceDis)
        self.ids.append(studentIds[matchIndex])
        if matches[matchIndex]:
          x=matches[matchIndex]
          y1,x2,y2,x1=faceLoc
          y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
          bbox=55+x1,162+y1,x2-x1,y2-y1
          cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
          cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
          cv2.putText(frame,studentIds[matchIndex],(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        else:
          y1,x2,y2,x1=faceLoc
          y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
          bbox=55+x1,162+y1,x2-x1,y2-y1
          cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),2)
          cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
          cv2.putText(frame,"Unknown",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)   
  
          return frame
  def get_student_id(self):
    return self.ids
        
        
# class Ids(Face):
#   def __init__(self):
#     super().__init__(frame)
#     self.ids=[]
    
#   def getstudentid(self):
#     return self.ids




       
        
        
  
  

  
  
  



