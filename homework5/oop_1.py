import datetime


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


class Student:
    """Creates student person

    Attributes
    ----------
    last_name: Student's last name
    first_name: Student's first name

    Methods
    --------
    __init__: Set all required attributes
    do_homework: Static method. Returns homework or expired deadline warning
    """

    def __init__(self, last_name: str, first_name: str):
        """
        Set all required attributes

        :param last_name: Student's last name
        :param first_name: Student's first name
        """

        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework):
        """
        Static method for doing homework

        :param homework: Homework class object
        :return: Homework object or expired deadline warning
        """

        return homework if homework.is_active() else print("You are late")


class Teacher:
    """Creates teacher person

    Attributes
    ----------
    last_name: Student's last name
    first_name: Student's first name

    Methods
    --------
    __init__: Set all required attributes
    create_homework: Static method. Creates and returns homework object
    """

    def __init__(self, last_name: str, first_name: str):
        """
        Set all required attributes

        :param last_name: Teacher's last name
        :param first_name: Teacher's first name
        """

        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def create_homework(text: str, deadline: int):
        """
        Creates homework object

        :param text: Text of the task
        :param deadline: Number of days to complete
        :return: Homework object
        """

        return Homework(text, deadline)
