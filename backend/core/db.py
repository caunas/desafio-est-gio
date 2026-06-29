from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATABASE_URL = "sqlite:///./db.sqlite"

engine = create_engine(
    DATABASE_URL,
    echo = False,
    connect_args = {"check_same_thread": False}
)

SessionLocal = sessionmaker(
    bind = engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass

from models import Account, CheckingAccount, SavingsAccount

def create_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
