

from fastapi import FastAPI, APIRouter
from app.routes.routesadd import router

# from app.models.studentmodel import StudentModel
from app.settings.connectdb import Firebase

app=FastAPI()

app.include_router(router)


@app.get("/")
async def home():
    return {"message":"Welcome to the Live Attendance System"}


 
   


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(app = "main:app", host="localhost", port=8000, reload=True)



  