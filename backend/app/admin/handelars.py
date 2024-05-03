from fastapi import Depends, HTTPException, status,UploadFile,File
from app.models.studentmodel import StudentModelshema
from fastapi import APIRouter
from app.settings.connectdb import Firebase
from typing import Dict,Any,Optional
from datetime import datetime
from app.functions.encodeGenarator import EndcodeGenarator


db_add=APIRouter()
db=Firebase()
imagepath=EndcodeGenarator().imagepath
picklepath=EndcodeGenarator().picklepath


@db_add.post("/create")
async def add_to_db(Student:StudentModelshema):
    
    data={
        Student.id: {
            "name": Student.name,
            "email": Student.email,
            "status": Student.status,
            "Department": Student.Department,
            "Semester": Student.Semester,
            "Section": Student.Section,
            "Total_Attendance": Student.Total_Attendance,
            "last_seen": f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
        }
    }
    x=db.set_data(data)
    return x

@db_add.get("/getstudents")
async def get_from_db():
    data=db.get_data()
    return data

@db_add.get("/getstudent/{id}")
async def get_from_db(id:str):
    data=db.get_data_by_key(id)
    return data

@db_add.put("/updatestudent/{id}")
async def update_db(id:str,data:Dict[str,Any])->Dict[str,Any]:
    x=db.update_data(id,data)
    return x

@db_add.delete("/deletestudent/{id}")
async def delete_from_db(id:str):
    x=db.delete_data(id)
    return x

@db_add.get("/getstudentbydepartment/{department}")
async def get_from_db(department:str):
    data=db.get_data_by_child_value("Department",department)
    return data
@db_add.get("/getpresentstudents")
async def get_from_db():
    data=db.get_data_by_present()
    return data
@db_add.get("/getstudentbyrange/{start}/{end}")
async def get_from_db(start:int,end:int):
    data=db.get_data_by_child_range("Total_Attendance",start,end)
    return data

@db_add.get("/getstudentbylimit/{limit}")
async def get_from_db(limit:int):
    data=db.get_data_by_child_limit("Total_Attendance",limit)
    return data

@db_add.get("/uploadimage")
async def uploadimage(img:UploadFile=File(...)):
    try:
        content = await img.read()
        with open(imagepath, "wb") as file:
            file.write(content)
        return {"message":"Image uploaded"} 
    
    except Exception as e:
        return {"message":str(e)}
    finally:
        file.close()
@db_add.get("/encoding")
async def encoding():
    x=EndcodeGenarator().findencoding()
    return x

   




