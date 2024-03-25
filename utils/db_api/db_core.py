from utils.db_api.models import Group, Teacher
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


def delete_teacher(id):
    session = sessionmaker(bind=engine)()
    try:
        teacher = session.query(Teacher).filter(Teacher.id == id).first()
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

# from sqlalchemy.orm import sessionmaker
# from utils.db_api.models import Group
# from data.config import engine
#
# Session = sessionmaker(bind=engine)
#
# def operate_on_group(func):
#     def wrapper(*args, **kwargs):
#         session = Session()
#         try:
#             result = func(session, *args, **kwargs)
#             session.commit()
#             return result
#         except Exception as e:
#             session.rollback()
#             raise e
#         finally:
#             session.close()
#     return wrapper
#
# @operate_on_group
# def create_group(session, **kwargs):
#     group = Group(**kwargs)
#     session.add(group)
#     session.flush()  # Use flush to get the ID immediately
#     return group.id
#
# @operate_on_group
# def read_group(session, id):
#     return session.query(Group).filter(Group.id == id).first()
#
# @operate_on_group
# def read_groups(session, id):
#     return session.query(Group).filter(Group.id == id).all()
#
# @operate_on_group
# def read_all_groups(session):
#     return session.query(Group).all()
#
# @operate_on_group
# def delete_group(session, id):
#     group = session.query(Group).filter(Group.id == id).first()
#     if group:
#         session.delete(group)
#         return True
#     return False
