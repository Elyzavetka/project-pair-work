from lib.estimated_time_to_read import *
    
def test_estimated_time_to_read():
    result = estimated_time_to_read("Follow the design recipe to implement the following user stories")
    assert result == 0.05
