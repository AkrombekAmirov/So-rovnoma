from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import SQLModel, create_engine, Field
from data.config import DATABASE_URL

Base = declarative_base()


class Group(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    group: str


class Teacher(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    group_id: str
    name: str
    teacher_id: str


class Student(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    group_id: str
    name: str
    hemis_id: str
    telegram_id: str
    username: str


def create_db_and_tables():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)


def main():
    create_db_and_tables()


if __name__ == "__main__":
    main()
