from homework4.task03 import my_precious_logger


def test_send_to_stdout_case(capfd):
    """Testing that usual string goes to stdout"""

    my_precious_logger("test")
    stdout, stderr = capfd.readouterr()
    assert stdout == "test"
    assert stderr == ""


def test_send_to_stderr_case(capfd):
    """Testing that string starting with 'error' goes to stdout"""

    my_precious_logger("error: file not found")
    stdout, stderr = capfd.readouterr()
    assert stdout == ""
    assert stderr == "error: file not found"
