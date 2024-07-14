from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker
from models import Student, Grade, Subject, Teacher, Group

DATABASE_URL = "postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/my_postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    return session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_id):
    return session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()

def select_3(subject_id):
    return session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Student).join(Grade).filter(Grade.subject_id == subject_id).group_by(Group.id).all()

def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).all()

def select_5(teacher_id):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

def select_6(group_id):
    return session.query(Student.name).filter(Student.group_id == group_id).all()

def select_7(group_id, subject_id):
    return session.query(Student.name, Grade.grade).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()

def select_8(teacher_id):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Subject).filter(Subject.teacher_id == teacher_id).all()

def select_9(student_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id).all()

def select_10(student_id, teacher_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).all()

# Виклики функцій для тестування
if __name__ == "__main__":
    print(select_1())
    print(select_2(1))
    print(select_3(1))
    print(select_4())
    print(select_5(1))
    print(select_6(1))
    print(select_7(1, 1))
    print(select_8(1))
    print(select_9(1))
    print(select_10(1, 1))

session.close()
