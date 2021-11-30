import datetime


class Homework:
    def __init__(
        self,
        text: str,
        deadline: int,
        created: datetime = datetime.datetime.now(),
    ):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = created

    def is_active(self) -> bool:
        return datetime.datetime.now() < self.created + self.deadline


class Student:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework):
        return homework if homework.is_active() else print("You are late")


class Teacher:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text: str, deadline: int):
        return Homework(text, deadline)
