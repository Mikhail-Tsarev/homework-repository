def check_power_of_2(a: int) -> bool:
    """Check if a integer is a power of 2
    :param a: int
    :return: bool
    """

    if a != 0:
        return not (a & (a - 1))
    return False
