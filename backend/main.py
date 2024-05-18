
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, APIRouter
from app.routes.routesadd import router

# from app.models.studentmodel import StudentModel
from app.settings.connectdb import Firebase
origins=[
    "*"
]

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
async def home():
    return {"message":"Welcome to the Live Attendance System"}


 
   


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(app = "main:app", host="localhost", port=8000, reload=True)



  