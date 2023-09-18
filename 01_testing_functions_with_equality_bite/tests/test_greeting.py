from lib.greet import *

def test_greet():
    result = greet("Rachel")
    assert result == "Hello, Rachel!"