import datetime

import pytest

from homework6.oop_2 import (DeadlineError, Homework, HomeworkResult, Student,
                             Teacher)

# constants:
good_student = Student("Petrov", "Ivan")
bad_student = Student("Sidorov", "Polykarp")
opp_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")


def test_homework_result_income_type_exception():
    """Testing not a Homework obj was given as a HomeworkResult attr"""

    with pytest.raises(ValueError, match="You gave a not Homework object"):
        HomeworkResult(
            "Not Homework type",
            "Bla-bla solution",
            good_student,
            datetime.datetime.now(),
        )


def test_deadline_exception():
    """Testing deadline error"""

    hw_deadlined = Homework("Some text", -1, datetime.datetime.now())

    with pytest.raises(DeadlineError, match="You are late"):
        good_student.do_homework(hw_deadlined, "Some solution")


def test_check_homework():
    """Testing Homework checking and result adding"""

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    result = good_student.do_homework(oop_hw, "I have done this hw")

    assert opp_teacher.check_homework(result) is True
    assert result.homework in opp_teacher.homework_done


def test_check_homework_negative_case():
    """Testing Homework checking for too short solution"""

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    result = bad_student.do_homework(oop_hw, "done")

    assert opp_teacher.check_homework(result) is False
    assert result.homework not in opp_teacher.homework_done


def test_homework_done():
    """Testing that Homework stores into Teacher class"""

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    result = good_student.do_homework(oop_hw, "I have done this hw")
    opp_teacher.check_homework(result)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result)
    temp_2 = Teacher.homework_done

    assert temp_1 == temp_2
