from sqlalchemy.orm import Session
from models.course import Course
from schemas.course import CourseCreate

def get_all_courses(db: Session):
    return db.query(Course).all()

def create_new_course(db: Session, course: CourseCreate):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course