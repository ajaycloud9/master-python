import pytest
import time
import source.myfunctions as my_function
from utility.baselogger import BaseLogger
base_logger = BaseLogger()
logger = base_logger.test_logging()

def test_add():
    result = my_function.add_func(1,2)
    assert result == 3

def test_divide():
    result = my_function.divide_func(1,2)
    logger.info(f"Diving the number and {result}")
    assert result == 0.5

@pytest.mark.slow
def test_slow_add():
    time.sleep(1)
    result = my_function.add_func(1,2)
    logger.info(f"Diving the number and {result}")
    assert result == 3

@pytest.mark.skip(reason="This is a broken feature")
def test_add_skip():
    result = my_function.add_func(1,2)
    assert result == 3

@pytest.mark.xfail(reason="We know we can't divide by zero")
def test_divide_by_zero():
    my_function.divide_func(4,0)

