from pydantic import BaseModel

class CourseResponse(BaseModel):
    courseName: str  
    professorName: str  

    class Config:
        from_attributes = True

