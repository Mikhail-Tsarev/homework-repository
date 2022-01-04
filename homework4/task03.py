import sys


def my_precious_logger(text: str):
    """
    Sends string starting with 'error' to stderr
    and to stdout otherwise
    :param text: String to process
    :return: Send string in stdout/stderr
    """

    if text.startswith("error"):
        return sys.stderr.write(text)
    else:
        return sys.stdout.write(text)
