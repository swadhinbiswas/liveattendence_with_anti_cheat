from pydantic import BaseModel
from fastapi import UploadFile,File

class StudentModelshema(BaseModel):
    name: str
    email: str
    status: str
    Department: str
    Semester: str
    Section: str
    Total_Attendance: str
    id: str
    
