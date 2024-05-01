from app.functions.videoapp import Camera
from fastapi import FastAPI, Response
from app.models.studentmodel import StudentModel
from app.settings.connectdb import Firebase

app=FastAPI()


@app.get("/")
async def home():
    return {"message":"Welcome to the Live Attendance System"}

@app.post("/create")
async def add_to_db(Student:StudentModel):
    ref=Firebase.ref
    data={
        Student.id: {
            "name": Student.name,
            "email": Student.email,
            "status": Student.status,
            "Department": Student.Department,
            "Semester": Student.Semester,
            "Section": Student.Section,
            "Total_Attendance": Student.Total_Attendance,
            "last_seen": Student.last_seen,
        }
    }
    
    for key,value in data.items():
        ref.child(key).set(value)
    return data

if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(app = "main:app", host="localhost", port=8000, reload=True)



  