from lib.check_codeword import *

def test_check_codeword():

    result = check_codeword("horse")
    assert result == 'Correct! Come in.'

    result2 = check_codeword("house")
    assert result2 == "Close, but nope."

    result3 = check_codeword("door")
    assert result3 == "WRONG!"


