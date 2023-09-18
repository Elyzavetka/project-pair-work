from lib.string_builder import *

def test_string_builder():
    instance = StringBuilder()
    instance.add("Hello world")
    result = instance.size()
    assert result == 11
    output_result = instance.output()
    assert output_result == "Hello world"


def test_string_builder_2():
    instance = StringBuilder()
    instance.add("Hello world")
    instance.add("Hello world")
    result = instance.size()
    assert result == 22
    output_result = instance.output()
    assert output_result == "Hello worldHello world"



    