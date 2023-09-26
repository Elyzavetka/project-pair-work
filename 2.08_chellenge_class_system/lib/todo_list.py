class TodoList:
    def __init__(self):
        self._todolist = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        return self._todolist.append(todo)

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_list = []
        for item in self._todolist:
            if item.complete_property == False:
                incomplete_list.append(item.task)
        return incomplete_list

    def complete(self):
        complete_list = []
        for item in self._todolist:
            if item.complete_property == True:
                complete_list.append(item.task)
        return complete_list

        # Returns:
        #   A list of Todo instances representing the todos that are complete
        

    def give_up(self):
        for item in self._todolist:
            item.complete_property = True

        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        
