from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from datetime import datetime, timedelta
from models import Base, Group, Student, Teacher, Subject, Grade

DATABASE_URL = "postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/my_postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# Додавання груп
groups = [Group(name=f"Group {i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()

# Додавання викладачів
teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

# Додавання предметів
subjects = [Subject(name=fake.word(), teacher=random.choice(teachers)) for _ in range(8)]
session.add_all(subjects)
session.commit()

# Додавання студентів
students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()

# Додавання оцінок
for student in students:
    for subject in subjects:
        grades = [Grade(student=student, subject=subject, grade=random.uniform(1, 100), date=fake.date_time_between(start_date='-1y', end_date='now')) for _ in range(random.randint(1, 20))]
        session.add_all(grades)
session.commit()

session.close()
