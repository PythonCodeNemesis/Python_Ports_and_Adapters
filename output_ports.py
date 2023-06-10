class TaskOutputPort:
    def display_task(self, task):
        raise NotImplementedError

    def save_task(self, task):
        raise NotImplementedError

class FileTaskOutputAdapter(TaskOutputPort):
    def display_task(self, task):
        print(f"Task: {task}")

    def save_task(self, task):
        with open("tasks.txt", "a") as file:
            file.write(f"{task}\n")