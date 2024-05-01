from fastapi import Depends, HTTPException, status
from app.models.studentmodel import StudentModel
from fastapi import APIRouter
from app.settings.connectdb import Firebase



db_add=APIRouter()


@db_add.post("/create")
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
    
    ref.push(data)
    return {data:data}
