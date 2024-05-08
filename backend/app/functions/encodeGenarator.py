import os
import pickle
import face_recognition
import cv2
import asyncio
from app.settings.connectdb import Firebase







class EndcodeGenarator:
  def __init__(self):
    self.known_face_encodings = []
    self.studentids = []
    self.encodings = []
    self.pathlist = os.listdir(os.path.join(os.path.dirname(__file__), "pictures"))
    self.picklepath = os.path.join(os.path.dirname(__file__), "encodings.pickle")
    self.imagepath = os.path.join(os.path.dirname(__file__), "pictures")
    self.ref = Firebase().ref
    self.bucket = Firebase().bucket
    self.idsref = Firebase().idsref
  
  async def findencoding(self):
    imageList=self.pathlist
    for img in imageList:
     bucket=self.bucket
     ref=self.ref 
     if not bucket.get_blob(f"faceappimage/{img}"):
      with open(f"{self.imagepath}/{img}","rb") as file:
       bucket.blob(f"faceappimage/{img}").upload_from_file(file)
     id=img.split(".")[0]
     self.studentids.append(id)
     if not ref.child(id).get():
       if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg"):
        cv2img=cv2.imread(f"{self.imagepath}/{img}")
        img=cv2.cvtColor(cv2img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        self.encodings.append(encode)
        self.idsref.child(id).set(encode)
    encodeKnowlist=[self.encodings,self.studentids]
    file=open(self.picklepath,"wb")
    pickle.dump(encodeKnowlist,file)
    file.close()
    
    return {
      "message":"encoding done",
      "status":"success",
      "data":"Knowlist saved in pickle file and Stored in firebase",
    }


   
    
    
  

    
      
      
      
      
 
  
  

# phots_path = os.path.join(os.path.dirname(__file__), "pictures")

# pickle_path = os.path.join(os.path.dirname(__file__), "encodings.pickle")

# pathlist = os.listdir(phots_path)
# print(pathlist)

# print(phots_path)




# class EncodeGenarator:
    # def __init__(self):
    #     self.known_face_encodings = []
    #     self.known_face_names = []
    #     self.path = os.path.join(os.path.dirname(__file__), "encodings.pickle")
    #     self.load_encodings()
        
    # def load_encodings(self):
    #     if os.path.exists(self.path):
    #         with open(self.path, "rb") as f:
    #             self.known_face_encodings, self.known_face_names = pickle.load(f)
    
    # def save_encodings(self):
    #     with open(self.path, "wb") as f:
    #         pickle.dump([self.known_face_encodings, self.known_face_names], f)
    
    # def add_encoding(self, name: str, face_encoding: np.ndarray):
    #     self.known_face_encodings.append(face_encoding)
    #     self.known_face_names.append(name)
    #     self.save_encodings()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    # def __init__(self):
    #     self.known_face_encodings = []
    #     self.known_face_names = []
    #     self.path = os.path.join(os.path.dirname(__file__), "encodings.pickle")
    #     self.load_encodings()

    # def load_encodings(self):
    #     if os.path.exists(self.path):
    #         with open(self.path, "rb") as f:
    #             self.known_face_encodings, self.known_face_names = pickle.load(f)

    # def save_encodings(self):
    #     with open(self.path, "wb") as f:
    #         pickle.dump([self.known_face_encodings, self.known_face_names], f)

    # def add_encoding(self, name: str, face_encoding: np.ndarray):
    #     self.known_face_encodings.append(face_encoding)
    #     self.known_face_names.append(name)
    #     self.save_encodings()

    # def get_face_encodings(self, image: np.ndarray) -> Dict[str, Any]:
    #     face_locations = face_recognition.face_locations(image)
    #     face_encodings = face_recognition.face_encodings(image, face_locations)
    #     face_names = []
    #     for face_encoding in face_encodings:
    #         matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, setting.TOLERANCE)
    #         name = "Unknown"
    #         if True in matches:
    #             first_match_index = matches.index(True)
    #             name = self.known_face_names[first_match_index]
    #         face_names.append(name)
    #     return {"face_locations": face_locations, "face_names": face_names}

    # def get_face_encodings_from_image(self, image_path: str) -> Dict[str, Any]:
    #     image = cv2.imread(image_path)
    #     rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #     return self.get_face_encodings(rgb_image)