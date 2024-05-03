from pydantic import BaseModel

class StudentModelshema(BaseModel):
    name: str
    email: str
    status: str
    Department: str
    Semester: str
    Section: str
    Total_Attendance: str
    id: str
    
