import datetime

from homework5.oop_1 import Homework, Student, Teacher

hw1 = Homework("do something", 5)
hw2 = Homework("do something else", 3)
hw3 = Homework("do something earlier", 0)
student1 = Student("Morozov", "Pavlik")
teacher1 = Teacher("Iscariot", "Judas")


def test_homework_initialization():
    """Testing that homework instance creates properly"""

    assert hw1.text == "do something" and hw1.deadline == datetime.timedelta(
        days=5
    )


def test_homework_is_active_pos_case():
    """Testing that homework is_active method
    works properly, positive case"""

    assert hw2.is_active() is True


def test_homework_is_active_neg_case():
    """Testing that homework is_active method
    works properly, negative case"""

    assert hw3.is_active() is False


def test_student_initialization():
    """Testing that student instance creates properly"""

    assert student1.last_name == "Morozov" and student1.first_name == "Pavlik"


def test_student_do_homework_in_time():
    """Testing that student.do_homework()
    works properly, positive case"""

    assert student1.do_homework(hw1) is hw1


def test_student_do_homework_expired(capfd):
    """Testing that student.do_homework()
    works properly, negative case"""

    student1.do_homework(hw3)
    out, err = capfd.readouterr()

    assert student1.do_homework(hw3) is None
    assert out == "You are late\n"
    assert err == ""


def test_teacher_initialization():
    """Testing that teacher instance creates properly"""

    assert teacher1.last_name == "Iscariot" and teacher1.first_name == "Judas"


def test_teacher_create_homework():
    """Testing that teacher.create_homework()
    works properly"""

    hw4 = teacher1.create_homework("The Price of Conscience", 33)
    assert hw4.text == "The Price of Conscience"
    assert hw4.deadline == datetime.timedelta(33)
