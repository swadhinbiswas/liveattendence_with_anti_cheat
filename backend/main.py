from app.functions.videoapp import Camera
from fastapi import FastAPI, Response
from app.models.studentmodel import StudentModel
from app.settings.connectdb import Firebase

app=FastAPI()


@app.get("/")
async def home():
    return {"message":"Welcome to the Live Attendance System"}



if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(app = "main:app", host="localhost", port=8000, reload=True)



  