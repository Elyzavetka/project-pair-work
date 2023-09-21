from lib.drive_a_class_chellenge import*

def test_verify_punctuation():
    grammar_check = GrammarStats()
    result = grammar_check.check("Right punctuation.")
    assert result == True

def test_verify_punctuation_2():
    grammar_check = GrammarStats()
    result = grammar_check.check("wrong punctuation")
    assert result == False

def test_percentage_good():
    percentage = GrammarStats()
    result = percentage.percentage_good()
    assert result == 0
