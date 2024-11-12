from pydantic import BaseModel

# 강의 정보 응답 스키마
class LectureInfoResponse(BaseModel):
    lectureName: str
    lectureLength: int
    analysis: bool

    class Config:
        orm_mode = True

# 강의 영상 응답 스키마
class LecturePlayResponse(BaseModel):
    lecture: bytes  # 비디오 파일의 바이트 데이터를 반환
