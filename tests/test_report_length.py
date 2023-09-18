from lib.report_length import *

def test_report_length():
    result = report_length("any I think")
    assert result == "This string was 11 characters long."