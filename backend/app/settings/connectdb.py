import firebase_admin
from typing import Dict,Any
from firebase_admin import credentials
from firebase_admin import db,storage
import firebase_admin
import os
# from app.settings import setting


class Firebase:
  
  firebase_url="https://database-faceapp-default-rtdb.asia-southeast1.firebasedatabase.app/"
  path=os.path.join(os.path.dirname(__file__), "serviceAccountKey.json")
  cred = credentials.Certificate(path)
  firebase_admin.initialize_app(cred,{
    'databaseURL': f'{firebase_url}',
    'storageBucket': "database-faceapp.appspot.com"
})
  ref=db.reference('students')
  idsref=db.reference('ids')
  bucket=storage.bucket()
  
  
  def get_data(self)->Dict[str,Any]:
    return self.ref.get()
  
  
  def set_data(self,data:Dict[str,Any])->Dict[str,Any]:
    for key,value in data.items():
        self.ref.child(key).set(value)
        return {"message":"Data Added Successfully",
                "data":data}
      
      
  
  def update_data(self,key:str,data:Dict[str,Any])->Dict[str,Any]:
    self.ref.child(key).update(data)
    new_data=self.ref.child(key).get()
    return {
      "message":"Data Updated Successfully",
      "data":new_data
    }
    
    
  def delete_data(self,key:str)->Dict[str,Any]:
    self.ref.child(key).delete()
    return {"message":"Data Deleted Successfully"}
    
  def get_data_by_key(self,key:str)->Dict[str,Any]:
    return self.ref.child(key).get()
  
  def get_data_by_child(self,child:str)->Dict[str,Any]:
    return self.ref.order_by_child(child).get()
  
  def get_data_by_child_value(self,child:str,value:str)->Dict[str,Any]:
    return self.ref.order_by_child(child).equal_to(value).get()
  
  def get_data_by_child_range(self,child:str,start:int,end:int)->Dict[str,Any]:
    return self.ref.order_by_child(child).start_at(start).end_at(end).get()
  
  def get_data_by_child_limit(self,child:str,limit:int)->Dict[str,Any]:
    return self.ref.order_by_child(child).limit_to_first(limit).get()
  
  def get_data_by_present(self)->Dict[str,Any]:
    return self.ref.order_by_child("status").equal_to("Present").get()
  
  
  def get_picture(self,img:str)->Dict[str,Any]:
    bucket=storage.bucket()
    return bucket.get_blob(f"faceappimage/{img}")
  
  
 









# # Example
# ref=db.reference('students')
# data=ref.get()
# print(data)

# # Example

# ref=db.reference('students')







# data={
#   "222156299": {
#     "name": "Naimul Islam",
#     "email": "naimulislam.cse@gmail.com",
#     "status": "Present",
#     "Department": "CSE",
#     "Semester": "6th",
#     "Section": "D",
#     "Total_Attendance": "75%",
#     "last_seen": "22-09-2021 10:00:00",
    
#   },
  
# }

# for key,value in data.items():
#     ref.child(key).set(value)