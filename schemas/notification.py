from pydantic import BaseModel

# 알림 생성 요청 스키마
class NotificationCreateRequest(BaseModel):
    message: str
    is_read: bool = False
    link: str  # 알림과 연결된 링크

class NotificationResponse(BaseModel):
    courseName: str
    message: str
    is_read: bool
    link: str  # 링크 추가

    class Config:
        from_attributes = True
