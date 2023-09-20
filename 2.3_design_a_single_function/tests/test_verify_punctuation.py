from lib.verify_punctuation import*

def test_verify_punctuation():
    result = verify_punctuation("Right punctuation.")
    assert result == True


def test_verify_punctuation_2():
    result = verify_punctuation("wrong punctuation")
    assert result == False