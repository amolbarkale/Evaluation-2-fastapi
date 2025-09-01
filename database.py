from sqlalchemy import Field, Session, create_engine
from sqlalchemy.orm import declarative_base

sqlite_url = f"sqlite:///./database.db"

connect_args = {"check_same_thread": False}

engine = create_engine(sqlite_url, connect_args=connect_args)

SessionLocal = Session(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
