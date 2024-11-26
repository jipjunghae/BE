from sqlalchemy import Column, Integer, JSON, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("tasks.course_id"), nullable=False)
    lecture_id = Column(Integer, ForeignKey("tasks.lecture_id"), nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    analysis = Column(JSON)  # 분석 결과
    solution = Column(JSON)  # 솔루션

    task = relationship("Task", back_populates="report", foreign_keys=[task_id])