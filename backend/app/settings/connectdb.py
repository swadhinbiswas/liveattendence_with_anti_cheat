import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os

class Firebase:
  path=os.path.join(os.path.dirname(__file__), "path/to/your/firebase/credentials.json")
  cred = credentials.Certificate(path)
  firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://database-faceapp-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
  ref=db.reference('students')
  







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