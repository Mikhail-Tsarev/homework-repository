import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from homework12.models import Homework, HomeworkResult, Student, Teacher

db = "sqlite:///" + os.getcwd() + "\\main.db"

engine = create_engine(db, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

query = (
    session.query(HomeworkResult, Homework, Student, Teacher)
    .join(HomeworkResult, HomeworkResult.homework == Homework.id)
    .join(Student, Student.id == HomeworkResult.author)
    .join(Teacher, Teacher.id == Homework.author)
    .all()
)

with open("report.csv", "w", newline="") as report:
    writer = csv.writer(report)
    for _, homework, student, teacher in query:
        row = [student, homework.created, teacher]
        writer.writerow(row)
    print()
    if len(query) != 1:
        print(f"{len(query)} records were added to report.csv")
    else:
        print("1 record was added to report.csv")
    print("       --- All done! ---")
