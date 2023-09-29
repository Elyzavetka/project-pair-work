import pytest
from lib.task_list import TaskList

@pytest.mark.skip
def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []

def test_by_mock_task_list_initially_empty():
    task_list = TaskList()
    mocks_initially = Fake_initially_empty()
    assert task_list.tasks == mocks_initially.list

@pytest.mark.skip
def test_adding_tasks():
    task_list = TaskList()
    task_list.add("Go shopping")
    task_list.add("Go for a walk")
    assert task_list.all() == ["Go shopping", "Go for a walk"]

def test_by_mock_adding_tasks():
    task_list = TaskList()
    fake_adding_tasks = Fake_adding_tasks()
    task_list.add("Go shopping")
    task_list.add("Go for a walk")
    assert task_list.all() == fake_adding_tasks.add()

@pytest.mark.skip
def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

def test_by_mock_tasks_initially_not_all_complete():
    task_list = TaskList()
    fake_not_all_complete = Fake_initially_not_all_complete()
    assert fake_not_all_complete.all_complete() is False

def test_by_mock_tasks_initially_all_complete():
    task_list = TaskList()
    fake_all_complete = Fake_initially_all_complete()
    assert fake_all_complete.all_complete() is True

# Unit test `#tasks` and `#all_complete` behaviour
class Fake_initially_empty():
    def __init__(self):
        self.list = []

class Fake_adding_tasks():
    def add(self):
        return ["Go shopping", "Go for a walk"]
    
class Fake_initially_not_all_complete():
    def all_complete(self):
        return False
    
class Fake_initially_all_complete():
    def all_complete(self):
        return True
