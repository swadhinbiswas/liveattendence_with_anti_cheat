from sqlalchemy import Column,DateTime, Integer, String,Text,ForeignKey,Boolean,Float,String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional


Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    status = Column(Integer)
    student_photos = ForeignKey('student_photos.id')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __init__(self, name: str, email: str, password: str, status: int):
        self.name = name
        self.email = email
        self.password = password
        self.status = status
    
    def __repr__(self):
        return f"<Student({self.name},{self.email},{self.status})>"
      
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        
class StudentPhotos(Base):
    __tablename__ = 'student_photos'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    photo = Column(String(150))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __init__(self, student_id: int, photo: str):
        self.student_id = student_id
        self.photo = photo
    
    def __repr__(self):
        return f"<StudentPhotos({self.student_id},{self.photo})>"
      
    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "photo": self.photo,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }


  