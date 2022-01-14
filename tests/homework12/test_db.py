from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from homework12.models import Student, Teacher

db = (
    "sqlite:///"
    + str(Path(__file__).parent.parent.parent)
    + "\\homework12\\main.db"
)


def test_database_structure():
    """Testing that created records exist in database tables"""

    engine = create_engine(db, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    students = session.query(Student).all()
    teachers = session.query(Teacher).all()

    assert str(students[1]) == "Sidorov Polykarp"
    assert str(teachers[1]) == "Smetanin Aleksandr"


def test_new_records_adding():
    """Testing the creation of new records"""

    engine = create_engine(db, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_student = Student(first_name="John", last_name="Smith")
    new_teacher = Teacher(first_name="Vladimir", last_name="Lenin")
    session.add(new_student)
    session.add(new_teacher)
    session.commit()

    query1 = session.query(Student).filter(Student.last_name == "Smith")
    query2 = session.query(Teacher).filter(Teacher.last_name == "Lenin")

    tmp_student = str(query1.first())
    tmp_teacher = str(query2.first())

    query1.delete(synchronize_session=False)
    query2.delete(synchronize_session=False)
    session.commit()

    assert tmp_student == "Smith John"
    assert tmp_teacher == "Lenin Vladimir"
