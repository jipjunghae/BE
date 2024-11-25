from fastapi import APIRouter

router = APIRouter()

# 필요하지 않은 라우트는 삭제 또는 주석 처리
# @router.get("/lectures")
# def get_lectures():
#     return [{"id": 1, "title": "Sample Lecture"}]

# @router.post("/lectures")
# def create_lecture():
#     return {"message": "Lecture created"}