def check_power_of_2(a: int) -> bool:
    """

    Check if a integer is a power of 2

    :param a: Integer to check
    :return: Is a power of 2 or not
    """

    if a != 0:
        return not (a & (a - 1))
    return False
