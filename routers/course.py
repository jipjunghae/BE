from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.course import Course, CourseCreate
from schemas.lecture import Lecture, LectureCreate
from models.course import Course as CourseModel
from models.lecture import Lecture as LectureModel
from database import get_db

router = APIRouter()

# 전체 강의 리스트 가져오기
@router.get("/courses", response_model=list[Course])
def get_courses(db: Session = Depends(get_db)):
    return db.query(CourseModel).all()

# 특정 강의 정보 가져오기
@router.get("/courses/{course_id}", response_model=Course)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

# 새로운 강의 추가
@router.post("/courses", response_model=Course)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = CourseModel(title=course.title, description=course.description)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

# 특정 강의의 전체 강의 영상 리스트 가져오기
@router.get("/courses/{course_id}/lectures", response_model=list[Lecture])
def get_lectures(course_id: int, db: Session = Depends(get_db)):
    lectures = db.query(LectureModel).filter(LectureModel.course_id == course_id).all()
    return lectures

# 특정 강의의 특정 강의 영상 정보 가져오기
@router.get("/courses/{course_id}/lectures/{lecture_id}", response_model=Lecture)
def get_lecture(course_id: int, lecture_id: int, db: Session = Depends(get_db)):
    lecture = (
        db.query(LectureModel)
        .filter(LectureModel.course_id == course_id, LectureModel.id == lecture_id)
        .first()
    )
    if not lecture:
        raise HTTPException(status_code=404, detail="Lecture not found")
    return lecture

# 특정 강의에 새로운 강의 영상 추가하기
@router.post("/courses/{course_id}/lectures", response_model=Lecture)
def create_lecture(course_id: int, lecture: LectureCreate, db: Session = Depends(get_db)):
    db_lecture = LectureModel(
        course_id=course_id,
        title=lecture.title,
        length=lecture.length,
        analysis=lecture.analysis,
        video_path=lecture.video_path,
    )
    db.add(db_lecture)
    db.commit()
    db.refresh(db_lecture)
    return db_lecture