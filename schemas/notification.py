from pydantic import BaseModel
from typing import Optional

class NotificationBase(BaseModel):
    course_id: Optional[int] = None  # 관련 강의 ID
    lecture_id: Optional[int] = None  # 관련 강의 영상 ID
    message: str  # 알림 메시지
    is_read: bool = False  # 읽음 상태
    link: Optional[str] = None  # 관련 링크

class NotificationCreate(NotificationBase):
    pass

class Notification(NotificationBase):
    id: int

    class Config:
        from_attributes = True  # ORM에서 데이터 추출 허용