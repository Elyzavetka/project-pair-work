import pytest
from lib.task_formatter import TaskFormatter


def test_task_formatter_incomplete():
    task = MockTask("Go for a walk", False)
    formatter = TaskFormatter(task)
    formatted = formatter.format()
    assert formatted == "- [ ] Go for a walk"

def test_task_formatter_complete():
    task = MockTask("Go shopping", True)
    formatter = TaskFormatter(task)
    formatted = formatter.format()
    assert formatted == "- [x] Go shopping"

class MockTask:
    def __init__(self, title, complete):
        self.title = title
        self.complete = complete


