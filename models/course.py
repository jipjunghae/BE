from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)

    lectures = relationship("Lecture", back_populates="course")
    notifications = relationship("Notification", back_populates="course")  # 추가