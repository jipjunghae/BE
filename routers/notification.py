from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.notification import NotificationResponse, NotificationCreateRequest
from services.notification_service import get_all_notifications, create_notification
from typing import List

router = APIRouter()

# 의존성 주입 - 데이터베이스 세션
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 모든 알림을 조회하는 엔드포인트 (읽지 않은 알림만 반환)
@router.get("/notification-list", response_model=List[NotificationResponse])
async def read_notifications(db: Session = Depends(get_db)):
    notifications = get_all_notifications(db)
    if notifications:
        response_data = [
            {
                "courseName": n.course.name if n.course else "Unknown Course",  # 연결된 강의 이름
                "message": n.message,
                "is_read": n.is_read,
                "link": n.link
            }
            for n in notifications
        ]
        return {"success": True, "data": response_data}
    else:
        raise HTTPException(status_code=404, detail="No unread notifications found")

# 새로운 알림을 추가하는 엔드포인트
@router.post("/notification", response_model=NotificationResponse)
async def add_notification(notification: NotificationCreateRequest, db: Session = Depends(get_db)):
    created_notification = create_notification(db=db, notification_data=notification)
    return created_notification
