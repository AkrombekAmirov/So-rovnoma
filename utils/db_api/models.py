from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import SQLModel, create_engine, Field
from data.config import DATABASE_URL

Base = declarative_base()


class User(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    role: str
    name: str
    phone_number: str
    created_date: datetime = Field(default=datetime.now().strftime("%Y-%m-%d"), index=True)


class Student(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str
    phone_number: str
    username: str
    created_date: datetime = Field(default=datetime.now().strftime("%Y-%m-%d"), index=True)
    created_time: datetime = Field(default=datetime.now().strftime("%H:%M:%S"), index=True)


class Question(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    question: str
    created_date: datetime = Field(default=datetime.now().strftime("%Y-%m-%d"), index=True)


class Option(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    question_id: int
    answer: str
    option: str
    created_date: datetime = Field(default=datetime.now().strftime("%Y-%m-%d"), index=True)


def create_db_and_tables():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)


def main():
    create_db_and_tables()


if __name__ == "__main__":
    main()
