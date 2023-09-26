import pytest
from lib.task_tracker import TaskTracker

#initially, there are no tasks

def test_initially_has_no_tasks():
    tracker = TaskTracker()
    assert tracker.list_incomplete() == []

def test_add_task_reflected_in_tasks():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    assert tracker.list_incomplete() == ["Walk the dog"]

def test_add_multiple_tasks():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the frog")
    assert tracker.list_incomplete() == ["Walk the dog", "Walk the cat", "Walk the frog"]

def test_marks_tasks_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    tracker.add("Walk the cat")
    tracker.add("Walk the frog")
    tracker.mark_complete(1)
    assert tracker.list_incomplete() == ["Walk the dog", "Walk the frog"]

def test_mark_task_that_is_too_low_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(-1)
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk the dog"]

def test_mark_task_that_is_too_high_complete():
    tracker = TaskTracker()
    tracker.add("Walk the dog")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(1)
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["Walk the dog"]




