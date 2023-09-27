from lib.diary_entries import DiaryEntry
from lib.diary import Diary


def test_add_experience_and_tast_in_diary():
    record = Diary()
    experience_1 = DiaryEntry("Today I visited a gym")
    experience_2 = DiaryEntry("Enjoyed a nice dinner")
    todo_task_1 = DiaryEntry(
        "I need to call my friend by number 07571111111")
    record.add(experience_1)
    record.add(experience_2)
    record.add(todo_task_1)
    assert record.get_list_of_diary_entries(
    ) == [experience_1, experience_2, todo_task_1]


def test_get_a_list_of_phone_numbers():
    numbers = Diary()
    todo_task_1 = DiaryEntry(
        "I need to call my friend by number 07571111111")
    todo_task_2 = DiaryEntry("I need to call somebody by number 07561111111")
    numbers.add(todo_task_1)
    numbers.add(todo_task_2)
    assert numbers.see_a_list_of_mobile_phones() == [
        "07571111111", "07561111111"]


def test_find_record_which_math_by_the_time():
    record = Diary()
    experience_1 = DiaryEntry("This morning I visited the gym")
    experience_2 = DiaryEntry("Enjoyed a nice dinner")
    record.add(experience_1)
    record.add(experience_2)
    assert record.get_diary_entry_by_the_time(
        5, 1) == "Enjoyed a nice dinner"
