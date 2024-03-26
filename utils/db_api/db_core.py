from utils.db_api.models import Group, Teacher, Student
from sqlalchemy.orm import sessionmaker
from data.config import engine


def create_group(**kwargs):
    session = sessionmaker(bind=engine)()
    try:
        group = Group(**kwargs)
        session.add(group)
        session.commit()
        return group.id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def read_group(id):
    session = sessionmaker(bind=engine)()
    try:
        return session.query(Group).filter(Group.group == id).first()
    finally:
        session.close()


def read_all_groups():
    session = sessionmaker(bind=engine)()
    try:
        return session.query(Group).all()
    finally:
        session.close()


def delete_group(id):
    session = sessionmaker(bind=engine)()
    try:
        group = session.query(Group).filter(Group.id == id).first()
        if group:
            session.delete(group)
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def create_teacher(**kwargs):
    session = sessionmaker(bind=engine)()
    try:
        teacher = Teacher(**kwargs)
        session.add(teacher)
        session.commit()
        return teacher.id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def read_teachers(id):
    session = sessionmaker(bind=engine)()
    try:
        return session.query(Teacher).filter(Teacher.group_id == id).all()
    finally:
        session.close()


def read_all_teachers():
    session = sessionmaker(bind=engine)()
    try:
        return session.query(Teacher).filter(Teacher.teacher_id == id).all()
    finally:
        session.close()


def delete_teacher(id, group_id):
    session = sessionmaker(bind=engine)()
    try:
        teacher = session.query(Teacher).filter(Teacher.teacher_id == id and Teacher.group_id == group_id).first()
        if teacher:
            session.delete(teacher)
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def create_student(**kwargs):
    session = sessionmaker(bind=engine)()
    try:
        student = Student(**kwargs)
        session.add(student)
        session.commit()
        return student.id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def get_student(hemis_id):
    session = sessionmaker(bind=engine)()
    try:
        return session.query(Student).filter(Student.hemis_id == hemis_id).first()
    finally:
        session.close()
