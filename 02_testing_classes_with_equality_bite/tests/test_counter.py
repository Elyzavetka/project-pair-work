from lib.counter import *

def test_counter():
    instance = Counter()
    instance.add(3)
    result = instance.report()
    assert result == "Counted to 3 so far."