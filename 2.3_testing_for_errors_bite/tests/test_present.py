import pytest
from lib.present import*

def test_present():
    present = Present()
    present.wrap(5)
    assert present.unwrap() == 5

def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No content have been wrapped."

def test_wrapping_already_wrapped():
    present = Present()
    present.wrap(11)
    with pytest.raises(Exception) as e:
        present.wrap(17)
    message = str(e.value)
    assert message == "A contents has already been wrapped."
