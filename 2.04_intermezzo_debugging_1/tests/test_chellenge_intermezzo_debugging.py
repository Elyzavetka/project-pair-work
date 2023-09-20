from lib.chellenge_intermezzo_debugging import*

def test_chellenge_intermezzo_debugging():
    result = get_most_common_letter("the roof, the roof, the roof is on fire!")
    assert result == "o"
