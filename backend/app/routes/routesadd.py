from fastapi import APIRouter
from app.admin.handelars import db_add
from app.functions.videoapp import videorouter
router = APIRouter()

router.include_router(db_add, prefix="/admin", tags=["Admin"])
router.include_router(videorouter, prefix="/video", tags=["Video"])

