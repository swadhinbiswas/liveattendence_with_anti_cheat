from face_recognition import face_encodings, load_image_file
from app.settings.connectdb import Firebase
from app.admin.imagepath import imagepaths
import cv2
import os 
import pickle
from app.picklepath import picklepathcode

class Encoding:
  def __init__(self,id,path):
    self.known_face_encodings = []
    self.known_face_names = []
    self.picklepathcode=picklepathcode
    self.imagepath=imagepaths
    self.id=id
    self.ref=Firebase().ref
    self.bucket=Firebase().bucket
    self.idsref=Firebase().idsref 
    self.known_face_encodings = []
    self.studentids = []
    self.encodingslist = []
    
  def encodings(self):
    img=f"{self.imagepath}/{self.id}"
    try:
      studentid=img.split(".")[0]
      if not self.ref.child(studentid).get():
        cv2img=cv2.imread(f"{self.imagepath}/{img}")
        img=cv2.cvtColor(cv2img,cv2.COLOR_BGR2RGB)
        encode=face_encodings(img)[0]
        self.known_face_encodings.append(encode)
        self.known_face_names.append(studentid)
        self.idsref.child(studentid).set(encode)
      encodeKnowlist=[self.known_face_encodings,self.known_face_names]
      file=open(self.picklepathcode,"wb")
      pickle.dump(encodeKnowlist,file)
      file.close()
    except Exception as e:
      return {"message":str(e)}
 
  
  
    
    
  

    
    