from lib.diary import Diary

def test_can_read_diary():
    diary = Diary("My Content")
    assert diary.read() == "My Content"