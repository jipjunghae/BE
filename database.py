from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 데이터베이스 URL 설정
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # SQLite 데이터베이스 파일 경로

# SQLAlchemy 엔진 설정
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 세션과 Base 초기화
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# DB 세션 생성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()