from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.course import CourseResponse
from schemas.lecture import LectureInfoResponse
from services.course_service import get_all_courses, get_course_info
from services.lecture_service import get_lectures_by_course_id, get_lecture_info, get_lecture_video_path
from typing import List
from fastapi.responses import FileResponse


router = APIRouter()

# 의존성 주입 - 데이터베이스 세션
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. 전체 강좌 목록 조회
@router.get("/courses", response_model=List[CourseResponse])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_all_courses(db)
    if courses:
        return {"success": True, "data": courses}
    else:
        raise HTTPException(status_code=404, detail="No courses found")

# 2. 특정 course 정보 조회
@router.get("/courses/{course_id}", response_model=CourseResponse)
async def read_course_info(course_id: int, db: Session = Depends(get_db)):
    course = get_course_info(db, course_id)
    if course:
        return {"courseName": course.name, "professorName": course.description}
    else:
        raise HTTPException(status_code=404, detail="Course not found")

# 3. 특정 course에 속한 모든 lecture 목록 조회
@router.get("/courses/{course_id}/lectures", response_model=List[LectureInfoResponse])
async def read_lectures_for_course(course_id: int, db: Session = Depends(get_db)):
    lectures = get_lectures_by_course_id(db, course_id)
    if lectures:
        return {"success": True, "data": lectures}
    else:
        raise HTTPException(status_code=404, detail="No lectures found for this course")

# 4. 특정 lecture의 정보 조회
@router.get("/courses/{course_id}/lectures/{lecture_id}", response_model=LectureInfoResponse)
async def read_lecture_info(course_id: int, lecture_id: int, db: Session = Depends(get_db)):
    lecture = get_lecture_info(db, lecture_id)
    if lecture and lecture.course_id == course_id:
        return {
            "lectureName": lecture.lecture_name,
            "lectureLength": lecture.lecture_length,
            "analysis": lecture.analysis
        }
    else:
        raise HTTPException(status_code=404, detail="Lecture not found in this course")

# 5. 특정 lecture의 비디오 파일 제공
@router.get("/courses/{course_id}/lectures/{lecture_id}/play")
async def play_lecture_video(course_id: int, lecture_id: int, db: Session = Depends(get_db)):
    video_path = get_lecture_video_path(db, lecture_id)
    lecture = get_lecture_info(db, lecture_id)
    if video_path and lecture and lecture.course_id == course_id:
        return FileResponse(video_path, media_type="video/mp4")
    else:
        raise HTTPException(status_code=404, detail="Video not found or lecture is not part of this course")
