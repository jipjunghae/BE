from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from database import engine, Base
from routers import course, notification, bt

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# FastAPI 앱 초기화
app = FastAPI()

# 예외 핸들러 추가
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "message": exc.detail},
    )

# 라우터 등록
app.include_router(course.router, tags=["Courses"])
app.include_router(notification.router, tags=["Notifications"])
app.include_router(bt.router, tags=["Bluetooth"])

# 기본 엔드포인트
@app.get("/")
async def root():
    return {"message": "API is running successfully"}
