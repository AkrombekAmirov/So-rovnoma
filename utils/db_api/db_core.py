

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from data.config import engine, Base


def create_teacher(**kwargs):
    try:
        session = sessionmaker(bind=engine)()
        teacher = User(**kwargs)
        session.add(teacher)
        session.commit()
        session.close()
        return teacher.id
    except Exception as e:
        return e


def student_create(**kwargs):
    try:
        session = sessionmaker(bind=engine)()
        student = Student(**kwargs)
        session.add(student)
        session.commit()
        session.close()
        return student.id
    except Exception as e:
        return e


def create_question(**kwargs):
    try:
        session = sessionmaker(bind=engine)()
        question = Question(**kwargs)
        session.add(question)
        session.commit()
        session.close()
        return question.id
    except Exception as e:
        return e


def create_option(**kwargs):
    try:
        session = sessionmaker(bind=engine)()
        option = Option(**kwargs)
        session.add(option)
        session.commit()
        session.close()
        return option.id
    except Exception as e:
        return e


def get_user(user_id: int):
    try:
        session = sessionmaker(bind=engine)()
        user = session.query(User).filter_by(id=user_id).first()
        session.close()
        return user
    except Exception as e:
        return e
