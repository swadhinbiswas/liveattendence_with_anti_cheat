from pydantic import BaseModel

class StudentModel(BaseModel):
    name: str
    email: str
    status: str
    Department: str
    Semester: str
    Section: str
    Total_Attendance: str
    last_seen: str 
    id: str
    
