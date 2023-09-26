class TaskTracker():
    def __init__(self):
        self._tasks = []

    def add(self, task):
        # Parameters:
        #   task: string representing a task
        self._tasks.append(task)

    def list_incomplete(self):
        # Returns:
        #   A list of incomplete task
        return self._tasks
    
    def mark_complete(self, index):
        # Parameters:
        # index: on representing the task to complete
        # Side-effect: 
        # Remove the task at index from the list of tasks
        if index < 0 or index >= len(self._tasks):
            raise Exception("No such task to mark complete")
        del self._tasks[index]