from lib.todo_list import TodoList
from lib.todo import Todo

def test_initially_has_one_entry_in_list():
    my_todo_list = TodoList()
    todo_task1 = Todo("Buy milk")
    my_todo_list.add(todo_task1)
    result = my_todo_list.incomplete()
    assert result == ["Buy milk"]

def test_initially_has_two_entry_in_list():
    my_todo_list = TodoList()
    todo_task1 = Todo("Buy milk")
    todo_task2 = Todo("Buy bread")
    my_todo_list.add(todo_task1)
    my_todo_list.add(todo_task2)
    result = my_todo_list.incomplete()
    assert result == ["Buy milk", "Buy bread"]

def test_initially_has_two_entry_one_complete_in_list():
    my_todo_list = TodoList()
    todo_task1 = Todo("Buy milk")
    todo_task2 = Todo("Buy bread")
    my_todo_list.add(todo_task1)
    my_todo_list.add(todo_task2)
    todo_task1.mark_complete()


def test_initially_has_two_entry_then_give_up():
    my_todo_list = TodoList()
    todo_task1 = Todo("Buy milk")
    todo_task2 = Todo("Buy bread")
    my_todo_list.add(todo_task1)
    my_todo_list.add(todo_task2)
    my_todo_list.give_up()
    result = my_todo_list.complete()
    assert result == ["Buy milk", "Buy bread"]
