import pytest
from lib.password_checker import*

def test_password_checker():
    password = PasswordChecker()
    assert password.check("Absdg34567") == True

def test_password_error():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("Abs")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."