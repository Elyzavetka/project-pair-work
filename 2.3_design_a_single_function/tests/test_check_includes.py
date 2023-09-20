from lib.check_includes import*

def test_check_includes():
    result = check_includes("Here is one #TODO")
    assert result == True

def test_check_includes_2():
    result = check_includes("and another one")
    assert result == False