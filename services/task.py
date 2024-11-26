from sqlalchemy.orm import Session
from models.task import Task
from models.report import Report
from schemas.task import TaskCreate
import time

def create_task(db: Session, task_data: TaskCreate):
    task = Task(
        course_id=task_data.course_id,  # course_id 추가
        lecture_id=task_data.lecture_id,  # lecture_id 추가
        playback=[seg.dict() for seg in task_data.playback],
        status="pending"
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def process_task(task_id: int, db: Session):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None

    task.status = "in_progress"
    db.commit()

    # Simulated processing logic
    total_time = sum(seg["end_time"] - seg["start_time"] for seg in task.playback)
    analysis = {"total_time": total_time, "detail": "Analysis complete"}
    solution = {"recommendation": "Review sections A and B for better understanding."}

    # Save report
    report = Report(
        course_id=task.course_id,  # course_id 추가
        lecture_id=task.lecture_id,  # lecture_id 추가
        task_id=task.id,
        analysis=analysis,
        solution=solution
    )
    db.add(report)
    task.status = "completed"
    db.commit()
    return report

def get_task_status(task_id: int, db: Session):
    task = db.query(Task).filter(Task.id == task_id).first()
    return task

def get_report(report_id: int, db: Session):
    report = db.query(Report).filter(Report.id == report_id).first()
    return report