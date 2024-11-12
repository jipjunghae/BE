from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    is_read = Column(Boolean, default=False)
    link = Column(String, nullable=True)  # 알림 관련 페이지로 이동할 링크 추가
