from homework6.counter import instances_counter


@instances_counter
class User:
    pass


def test_zero_instances():
    """Testing that class without initialised instances
    return 0 instances"""

    @instances_counter
    class User1:
        pass

    assert User1.get_created_instances() == 0


def test_3_instances():
    """Testing that class with 3 initialised instances
    return 3 instances"""

    @instances_counter
    class User2:
        pass

    user, _, _ = User2(), User2(), User2()

    assert user.get_created_instances() == 3


def test_reset_counter():
    """Testing that class with 3 initialised instances
    return 3 instances during reset and 0 instances
    after reset"""

    @instances_counter
    class User3:
        pass

    user, _, _ = User3(), User3(), User3()
    before_reset_value = user.reset_instances_counter()

    assert before_reset_value == 3 and user.get_created_instances() == 0
