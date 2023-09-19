from lib.gratitudes import *

def test_gratitudes():
    instance = Gratitudes()
    instance.add("Sunny days")
    result = instance.format()
    assert result == "Be grateful for: Sunny days"

def test_gratitudes_adding_multiple_items():
    instance = Gratitudes()
    instance.add("Sunny days")
    instance.add("cake")
    instance.add("weekends")
    result = instance.format()
    assert result == "Be grateful for: Sunny days, cake, weekends"