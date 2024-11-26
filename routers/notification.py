from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.notification import Notification  # SQLAlchemy 모델
from schemas.notification import Notification as NotificationSchema, NotificationCreate
from database import get_db

router = APIRouter()

# 안 읽은 알림 가져오기
@router.get("/notification", response_model=list[NotificationSchema])  # Pydantic 스키마 사용
def get_unread_notifications(db: Session = Depends(get_db)):
    notifications = db.query(Notification).filter(Notification.is_read == False).all()
    return notifications

# 새로운 알림 추가하기
@router.post("/notification", response_model=NotificationSchema)
def create_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    db_notification = Notification(
        course_id=notification.course_id,
        lecture_id=notification.lecture_id,
        message=notification.message,
        is_read=notification.is_read,
        link=notification.link,
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

# 알림 읽음 상태 업데이트
@router.put("/notification/{notification_id}/read", response_model=dict)
def mark_notification_as_read(notification_id: int, db: Session = Depends(get_db)):
    # 알림 조회
    notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    # 읽음 상태 업데이트
    notification.is_read = True
    db.commit()
    db.refresh(notification)

    return {"message": f"Notification {notification_id} marked as read"}