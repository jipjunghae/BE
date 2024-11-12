from sqlalchemy.orm import Session
from models.course import Course
from models.lecture import Lecture

# 특정 course 정보를 가져오는 함수
def get_course_info(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()

# 특정 course에 속한 모든 lecture 목록을 가져오는 함수
def get_lectures_by_course_id(db: Session, course_id: int):
    return db.query(Lecture).filter(Lecture.course_id == course_id).all()

# 특정 lecture 정보를 가져오는 함수
def get_lecture_info(db: Session, lecture_id: int):
    return db.query(Lecture).filter(Lecture.id == lecture_id).first()

# 특정 lecture 비디오 파일 경로를 가져오는 함수
def get_lecture_video_path(db: Session, lecture_id: int):
    lecture = db.query(Lecture).filter(Lecture.id == lecture_id).first()
    if lecture and lecture.video_path:
        return lecture.video_path
    return None
