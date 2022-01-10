import datetime
from collections import defaultdict


class Person:
    """Parent class for Student and Teacher

    Attributes
    ----------
    last_name: Person's last name
    first_name: Person's first name

    Methods
    --------
    __init__: Sets all required attributes
    """

    def __init__(self, last_name: str, first_name: str):
        """
        Sets all required attributes

        :param last_name: Person's last name
        :param first_name: Person's first name
        """

        self.last_name = last_name
        self.first_name = first_name


class DeadlineError(Exception):
    """Exception for timeout homework deadline"""

    pass


class Homework:
    """Creates homework object

    Attributes
    ----------
    text: Text of the task
    deadline: Number of days to complete
    created: Time and date of creation

    Methods
    --------
    __init__: Set all required attributes
    is_active: Checks if the deadline hasn't expired
    """

    def __init__(
        self,
        text: str,
        deadline: int,
        created: datetime = datetime.datetime.now(),
    ):
        """
        Set all required attributes

        :param text: Text of the task
        :param deadline: Number of days to complete
        :param created: Time and date of creation
        """

        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = created

    def is_active(self) -> bool:
        """
        Expired deadline check

        :return: True or False if the deadline hasn't expired
        """

        return datetime.datetime.now() < self.created + self.deadline


class HomeworkResult:
    """Student's work result

    Attributes
    ----------
    homework: Homework to be done
    solution: Student's answer
    author: Author of the solution
    created: Solution creation date and time

    Methods
    --------
    __init__: Sets all required attributes
    """

    def __init__(
        self,
        homework: Homework,
        solution: str,
        author: "Student",
        created: datetime,
    ):
        """
        Sets all required attributes

        homework: Homework to be done
        solution: Student's answer
        author: Author of the solution
        created: Solution creation date and time
        """

        if not isinstance(homework, Homework):
            raise ValueError("You gave a not Homework object")

        self.homework = homework
        self.solution = solution
        self.author = author
        self.created = created


class Student(Person):
    """Creates student person

    Attributes come from parent class Person

    Methods
    --------
    do_homework: Returns HomeworkResult or raises DeadlineError exception
    """

    def do_homework(self, homework: Homework, solution: str):
        """
        Method for doing homework

        :param homework: Homework class object
        :param solution: Result of the student's work
        :return: Homework object or raises DeadlineError exception
        """

        if homework.is_active():
            return HomeworkResult(
                homework, solution, self, datetime.datetime.now()
            )
        raise DeadlineError("You are late")


class Teacher(Person):
    """Creates teacher person

    Attributes:
    __________
     First and Last names come from parent class Person
     homework_done: Stores homework results

    Methods
    --------
    check_homework: Checks answer length (should be > 5)
    reset_results: Clear results stored in homework_done
    create_homework: Static method. Creates and returns homework object

    """

    homework_done = defaultdict(set)

    @classmethod
    def check_homework(cls, homework_result: HomeworkResult) -> bool:
        """
        Checks answer length (should be > 5).

        :param homework_result:
        :return: Is the solution has right length
        """

        if len(homework_result.solution) < 5:
            return False
        cls.homework_done[homework_result.homework].add(homework_result)
        return True

    @classmethod
    def reset_results(cls, homework=None):
        """
        Clear all results in homework_done if got None,
        else clear homework results

        :param homework:
        """

        cls.homework_done.clear() if homework is None else cls.homework_done[
            homework
        ].clear()

    @staticmethod
    def create_homework(text: str, deadline: int):
        """
        Creates homework object

        :param text: Text of the task
        :param deadline: Number of days to complete
        :return: Homework object
        """

        return Homework(text, deadline)
