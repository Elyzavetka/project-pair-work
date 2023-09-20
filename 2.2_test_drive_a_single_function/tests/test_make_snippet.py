from lib.pairing_exersizes import*

def test_make_snippet():
    result = make_snippet("You may immediately think I know how to code that!. Resist that temptation and stick to the test-driving process")
    assert result == "You may immediately think I..."