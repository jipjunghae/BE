from database import SessionLocal, engine, Base
from models.course import Course
from models.lecture import Lecture
from models.notification import Notification

# 데이터베이스 초기화
Base.metadata.create_all(bind=engine)

# 데이터베이스 세션 생성
db = SessionLocal()

# 초기 데이터 삽입
def seed_data():
    # 기존 데이터 삭제 (선택 사항)
    db.query(Notification).delete()
    db.query(Lecture).delete()
    db.query(Course).delete()

    # 예시 강의 데이터
    course = Course(title="Physics 101", description="Introduction to Physics")
    db.add(course)
    db.commit()
    db.refresh(course)

    # 예시 강의 영상 데이터
    lectures = [
        Lecture(
            course_id=course.id,
            title="Newton's Laws",
            length=45,
            analysis=True,
            video_path="video/ewha.mp4",
        ),
        Lecture(
            course_id=course.id,
            title="Thermodynamics Basics",
            length=50,
            analysis=False,
            video_path="video/JSB.mp4",
        ),
    ]
    db.add_all(lectures)
    db.commit()

    # 예시 알림 데이터
    notifications = [
        Notification(
            course_id=course.id,
            lecture_id=lectures[0].id,
            message="Newton's Laws lecture has been updated.",
            is_read=False,
            link="https://example.com/lectures/1"
        ),
        Notification(
            course_id=course.id,
            lecture_id=lectures[1].id,
            message="Thermodynamics Basics lecture has been added.",
            is_read=False,
            link="https://example.com/lectures/2"
        ),
    ]
    db.add_all(notifications)
    db.commit()

    print("Seed data inserted!")

# 실행
if __name__ == "__main__":
    seed_data()
    db.close()