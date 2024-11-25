from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=True)  # 강의 ID (선택적)
    lecture_id = Column(Integer, ForeignKey("lectures.id"), nullable=True)  # 강의 영상 ID (선택적)
    message = Column(String(255), nullable=False)  # 알림 메시지
    is_read = Column(Boolean, default=False)  # 읽음 상태
    link = Column(String(1024), nullable=True)  # 관련 링크

    # 관계 (옵션)
    course = relationship("Course", back_populates="notifications")
    lecture = relationship("Lecture", back_populates="notifications")