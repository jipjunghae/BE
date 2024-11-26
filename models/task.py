from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("lectures.course_id"), nullable=False)
    lecture_id = Column(Integer, ForeignKey("lectures.course_id"), nullable=False)
    status = Column(String, default="pending")  # 작업 상태: pending, in_progress, completed
    playback = Column(JSON)  # 재생 구간 데이터

    report = relationship("Report", back_populates="task", foreign_keys="Report.task_id")
    