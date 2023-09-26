from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_adda_and_lists_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My Contents 1")
    entry_2 = DiaryEntry("My Title 2", "My Contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

def test_count_words_returns_count_of_all_words_in_all_antry_contents():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One Two")
    entry_2 = DiaryEntry("My Title 2", "Three Four Five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5

def test_reading_time_returns_time_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One Two")
    entry_2 = DiaryEntry("My Title 2", "Three Four Five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3

def test_find_best_entry_for_reading_time_returns_entry_that_fits_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One Two")
    entry_2 = DiaryEntry("My Title 2", "One two tree four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

def test_find_best_entry_for_reading_time_returns_single_entry_thats_fit_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One Two")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

def test_find_best_entry_for_reading_time_returns_none_if_single_entry_doesnt_fit():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One Two Three Four Five Six Seven")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None

def test_find_best_entry_for_reading_time_returns_the_longer_readable():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "One Two")
    entry_2 = DiaryEntry("My Title 2", "One two tree four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_2