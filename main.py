from fastapi import FastAPI
from database import Base, engine
from routers import course, lecture, notification

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# FastAPI 앱 초기화
app = FastAPI()

# 라우터 등록
app.include_router(course.router)
app.include_router(lecture.router)
app.include_router(notification.router) 