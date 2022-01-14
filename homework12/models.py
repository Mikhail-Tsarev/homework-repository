from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Homework(Base):
    """Table that stores records about homeworks"""

    __tablename__ = "homeworks"

    id = Column(Integer, primary_key=True)
    text = Column(String(150), nullable=False)
    deadline = Column(Integer, nullable=False)
    created = Column(DateTime(), default=datetime.now().replace(microsecond=0))
    author = Column(Integer, ForeignKey("teachers.id"))

    def __repr__(self) -> str:
        return self.text


class HomeworkResult(Base):
    """Table that stores records about homework solutions"""

    __tablename__ = "homework_results"

    id = Column(Integer, primary_key=True)
    homework = Column(Integer, ForeignKey("homeworks.id"))
    solution = Column(String(150), nullable=False)
    created = Column(DateTime(), default=datetime.now)
    author = Column(Integer, ForeignKey("students.id"))

    def __repr__(self) -> str:
        return self.solution


class Student(Base):
    """Table that stores records about students"""

    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    def __repr__(self) -> str:
        return f"{self.last_name} {self.first_name}"


class Teacher(Base):
    """Table that stores records about teachers"""

    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    def __repr__(self) -> str:
        return f"{self.last_name} {self.first_name}"
