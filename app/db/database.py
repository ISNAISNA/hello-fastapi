from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir="C:/oracle/instantclient_23_7")

SQLALCHEMY_DATABASE_URL = "oracle+cx_oracle://system:oracle1@localhost:1521/XE"

# SQLAlchemy engine 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)

# DB 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class 생성하기
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
