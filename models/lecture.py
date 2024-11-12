from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True, index=True)
    lecture_name = Column(String, index=True)   # 강의명
    lecture_length = Column(Integer)            # 강의 길이 (분 단위)
    analysis = Column(Boolean, default=False)   # 분석 여부
    video_path = Column(String)                 # 강의 비디오 파일 경로
    
    # course_id 추가: Lecture가 어느 Course에 속하는지 식별
    course_id = Column(Integer, ForeignKey("courses.id"))
    
    # 관계 설정: Lecture와 Course 연결
    course = relationship("Course", back_populates="lectures")