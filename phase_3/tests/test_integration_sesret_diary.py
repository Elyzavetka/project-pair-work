import pytest
from lib.secret_diary import SecretDiary
from lib.diary import Diary

def test_secret_diary_cant_be_readed():
    diary = Diary("My Content")
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as err:
        secret_diary.read()
    assert str(err.value) == "No access"

def test_secret_diary_can_be_read():
    diary = Diary("My Content")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "My Content"

def test_reloced_diary_cant_be_read():
    diary = Diary("My Content")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as err:
        secret_diary.read()
    assert str(err.value) == "No access"


