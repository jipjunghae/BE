from pydantic import BaseModel

class ReportResponse(BaseModel):
    course_id: int
    lecture_id: int
    analysis: dict
    solution: dict