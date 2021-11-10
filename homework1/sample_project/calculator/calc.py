def check_power_of_2(a: int) -> bool:
    if a != 0:
        return not (a & (a - 1))
    return False