from pydantic import BaseModel
from typing import Optional, List
from schemas.lecture import Lecture

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    lectures: List[Lecture] = []  # 강의에 포함된 강의 영상 리스트

    class Config:
        from_attributes = True  # Pydantic v2 문법