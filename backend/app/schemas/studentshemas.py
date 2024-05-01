from pydantic import BaseModel
from typing import Optional

class StudentBase(BaseModel):
    id: int
    name: str
    email: str
    status:str
    
    class Config:
        from_attributes = True


class StudentPhotosBase(BaseModel):
   id= int
   student_id: int
   photo:Optional[str]



   
   


   
    
    
    