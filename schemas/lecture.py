from pydantic import BaseModel
from typing import Optional

class LectureBase(BaseModel):
    title: str
    length: int
    analysis: Optional[bool] = False
    video_path: Optional[str] = None

class LectureCreate(LectureBase):
    pass

class Lecture(LectureBase):
    id: int
    course_id: int

    class Config:
        from_attributes = True