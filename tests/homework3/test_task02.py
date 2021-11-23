import time

from homework3.task02 import multi_process_func, slow_calculate


def test_run_time_60_pools_case():
    """Testing that the time of calculation with 60 pools
    less than 1 minute"""
    start_time = time.time()
    multi_process_func(slow_calculate, range(500))
    execution_time = time.time() - start_time
    assert execution_time < 60
