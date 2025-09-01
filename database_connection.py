from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

sqlite_url = f"sqlite:///./database.db"

connect_args = {"check_same_thread": False}

engine = create_engine(sqlite_url, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
