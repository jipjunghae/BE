from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    title = Column(String, nullable=False)
    length = Column(Integer, nullable=False)
    analysis = Column(Boolean, default=False)
    video_path = Column(String, nullable=True)

    course = relationship("Course", back_populates="lectures")
    notifications = relationship("Notification", back_populates="lecture")  # 추가