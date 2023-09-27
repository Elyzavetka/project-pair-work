class DiaryEntry():
    def __init__(self, entry_text):
        self._experience = entry_text
        self._todo_list = []
        # self._phone_number = None

    def add_todo_task(self, todo_task):
        self._todo_list.append(todo_task)
