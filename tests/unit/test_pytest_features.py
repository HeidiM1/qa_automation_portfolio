#learning pytest features
from typing import Literal
import pytest

#fixture example (setup/teardown)
@pytest.fixture
def sample_users():
    #provide test data for multiple test
    return {"admin": "pass123", "user": "test123"}

def test_with_fixture(sample_users: dict[str, str]):
    #test using fixture
    assert "admin" in sample_users
    assert sample_users["admin"] == "pass123"

#parameterized tests - one test, multiple input
@pytest.mark.parametrize("input_a, input_b, expected", [
    (1, 1, 2),
    (5, 3, 8),
    (10, -2, 8),
])

def test_addition_variations(input_a: Literal[1] | Literal[5] | Literal[10], input_b: Literal[1] | Literal[3] | Literal[-2], expected: Literal[2] | Literal[8]):
    #one test, multiple data set
    result = input_a + input_b
    assert result == expected, f"{input_a} + {input_b} = {result}, expected {expected}"

#expected exceptions
def test_division_by_zero():
    #test that code resises expected errors
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0 #this should fail 

def test_key_error():
    #test missing dictionary key
    data = {"name": "Heidi", "role": "QA"}
    with pytest.raises(KeyError):
        value = data["age"] #key dosen't exsist

#skip tests
@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    #this will be skipped
    assert False #won't run

#custom messages
@pytest.mark.slow
def test_slow_operation():
    #marked as slow - can run seperately
    import time
    time.sleep(0.1) #simulate slow test
    assert True

@pytest.mark.login
def test_login_flow():
    #marked as login-related
    assert "user" in {"user": "pass"}

