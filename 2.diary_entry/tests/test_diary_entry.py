from lib.diary_entry import DiaryEntry

def test_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry("My Title", "My Contents")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "My Contents"

def test_count_words_returns_word_of_contents():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five")
    assert diary_entry.count_words() == 5

def test_reading_time():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five")
    assert diary_entry.reading_time(2) == 3

def test_readable_chunk_first_chunk():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five")
    assert diary_entry.reading_chunk(2, 1) == "One Two"

def test_readable_chunk_second_chunk():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five")
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "Three Four"

def test_readable_chunk_third_chunk():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "Five"

def test_readable_chunk_third_chunk():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1) 
    assert diary_entry.reading_chunk(2, 1) == "One Two"

def test_readable_chunk_fourth_with_exact_chunks():
    diary_entry = DiaryEntry("My Title", "One Two Three Four Five Six")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1) 
    assert diary_entry.reading_chunk(2, 1) == "One Two"