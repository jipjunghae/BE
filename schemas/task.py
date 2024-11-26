from pydantic import BaseModel
from typing import List

class PlaybackSegment(BaseModel):
    start_time: float
    end_time: float

class TaskCreate(BaseModel):
    course_id: int
    lecture_id: int
    playback: List[PlaybackSegment]

class TaskStatusResponse(BaseModel):
    status: str