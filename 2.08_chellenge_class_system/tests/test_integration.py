from lib.todo_list import TodoList
from lib.todo import Todo

def test_initially_has_empty_entries():
    my_todo_list = TodoList()
    todo_task1 = Todo("Buy milk")
    my_todo_list.add(todo_task1)
    result = my_todo_list.incomplete()
    assert result == ["Buy milk"]

    # todo_task = my_todo_list.Todo()    
    # my_todo_list.add("Buy milk")
    # my_todo_list = todo_task.Todo
