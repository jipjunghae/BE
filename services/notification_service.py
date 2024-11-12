from sqlalchemy.orm import Session
from models.notification import Notification
from schemas.notification import NotificationCreateRequest

# 모든 알림 목록을 가져오는 함수 (읽지 않은 알림만 포함)
def get_all_notifications(db: Session):
    return db.query(Notification).filter(Notification.is_read == False).all()

# 새로운 알림을 추가하는 함수
def create_notification(db: Session, notification_data: NotificationCreateRequest):
    db_notification = Notification(
        message=notification_data.message,
        is_read=notification_data.is_read,
        link=notification_data.link
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification
