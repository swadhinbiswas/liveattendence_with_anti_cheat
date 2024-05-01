from sqlalchemy import Column,DateTime, Integer, String,Text,ForeignKey,Boolean,Float,String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional


Base = declarative_base()

class Admin(Base):
    """
    Admin Model
    
    Args:
        Base ([type]): [description]
        
        Returns:
        [type]: [description]
        
        """
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))
    role = Column(String(100))
    status = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    """
    __init__ function
    """
    def __init__(self, name: str, email: str, password: str, role: str, status: int):
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.status = status
    
    def __repr__(self):
        return f"<Admin({self.name},{self.email},{self.role},{self.status})>"
    
    """
    to_dict function
    """
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "role": self.role,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        
