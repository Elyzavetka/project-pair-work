from lib.count_words import*

def test_count_words():
    result = count_words("that takes a string as an argument and returns the number of words in that string")
    assert result == 16