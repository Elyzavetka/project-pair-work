import pytest
from unittest.mock import Mock
from lib.secret_diary import SecretDiary

def test_secret_diary_cant_be_readed():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as err:
        secret_diary.read()
    assert str(err.value) == "No access"

def test_unlocked_diary_cant_be_readed():
    diary = Mock()
    diary.read.return_value = "Interesting Content"
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Interesting Content"
    diary.read.assert_called()

def test_relocked_diary_cant_be_read():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as err:
        secret_diary.read()
    assert str(err.value) == "No access"
    diary.read.assert_not_called()