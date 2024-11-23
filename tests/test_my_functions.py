import pytest
import time
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1, 4)
    assert result == 5

def test_divide():
    result = my_functions.divide(6, 2)
    assert result == 3

def test_divide_by_zero():
    # with pytest.raises(ZeroDivisionError): -- without modifying 'divide' should work
    with pytest.raises(ValueError): #changed to ValueError because of modifying 'divide'
        my_functions.divide(6, 0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.divide(6, 2)
    assert result == 3

@pytest.mark.skip(reason = "this feature is currently broken")
def test_broken_add():
    assert my_functions.add(2, 2) == 3

@pytest.mark.xfail(reason = "We Know we cannot divide by zero")
def test_divide_zero_error():
    my_functions.divide(4, 0)