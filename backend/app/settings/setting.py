from dotenv import load_dotenv
import os

load_dotenv()

class Setting:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('DEBUG')
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS')
    DATABASES_URL = os.getenv('DATABASES_URL')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_ENGINE = os.getenv('DATABASE_ENGINE')
    CAM_IP=os.getenv('CAM_IP')
    CAM_PORT=os.getenv('CAM_PORT')
    CAM_PORT=int(os.getenv('CAM_PORT'))
    
    
    

setting = Setting()
    