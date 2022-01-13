from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Homework, HomeworkResult, Student, Teacher

engine = create_engine("sqlite:///main.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

records = [
    Student(first_name="Ivan", last_name="Petrov"),
    Student(first_name="Polykarp", last_name="Sidorov"),
    Teacher(first_name="Daniil", last_name="Shadrin"),
    Teacher(first_name="Aleksandr", last_name="Smetanin"),
    Homework(text="Learn OOP", deadline=1, author=1),
    Homework(text="Learn more about OOP", deadline=5, author=2),
    HomeworkResult(homework=1, solution="I've done hw", author=1),
    HomeworkResult(homework=2, solution="All done!", author=2),
]

session.add_all(records)
session.commit()
