def read_magic_number(path: str) -> bool:
    """
    Function to check if the first line in file
    is a number in [1, 3) interval

    :param path: File to process
    :return: Is the fist line is number in [1,3)
    """

    try:
        with open(path) as fi:
            num = float(fi.readline().strip())
            return 1 <= num < 3
    except ValueError:
        raise ValueError("Value error")
    except FileNotFoundError:
        raise FileNotFoundError("File not found error")
