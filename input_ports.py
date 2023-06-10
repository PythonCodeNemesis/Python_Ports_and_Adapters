class TaskInputPort:
    def create_task(self, task):
        raise NotImplementedError

    def get_task(self, task_id):
        raise NotImplementedError

class ConsoleTaskInputAdapter(TaskInputPort):
    def create_task(self, task):
        return input("Enter a task: ")

    def get_task(self, task_id):
        return task_id