from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.task import TaskCreate, TaskStatusResponse
from schemas.report import ReportResponse
from services.task import create_task, process_task, get_task_status, get_report
from database import get_db
from models.task import Task  # Task 모델 임포트
from models.report import Report  # Report 모델 임포트

router = APIRouter()

@router.post("/task_start", status_code=202)
def start_task(task_data: TaskCreate, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    task = create_task(db, task_data)
    background_tasks.add_task(process_task, task.id, db)
    return {"task_id": task.id, "message": "Task has started"}

@router.get("/task_status/{task_id}")
def task_status(task_id: int, db: Session = Depends(get_db)):
    # 태스크 조회
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # 태스크 상태 반환
    response = {
        "task_id": task.id,
        "status": task.status,
    }

    # 태스크가 완료되었으면 리포트 ID 포함
    if task.status == "completed":
        report = db.query(Report).filter(Report.task_id == task.id).first()
        if report:
            response["report_id"] = report.id

    return response

@router.get("/report/{report_id}", response_model=ReportResponse)
def get_report_data(report_id: int, db: Session = Depends(get_db)):
    report = get_report(report_id, db)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return {
        "course_id": report.course_id,
        "lecture_id": report.lecture_id,
        "analysis": report.analysis,
        "solution": report.solution,
    }