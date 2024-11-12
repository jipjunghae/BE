from sqlalchemy.orm import Session
from models.course import Course

# 모든 강의 목록을 가져오는 함수
def get_all_courses(db: Session):
    return db.query(Course).all()

# 특정 course 정보를 가져오는 함수
def get_course_info(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()
