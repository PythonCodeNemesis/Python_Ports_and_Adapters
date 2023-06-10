class TaskApplication:
    def __init__(self, input_adapter, output_adapter):
        self.input_adapter = input_adapter
        self.output_adapter = output_adapter

    def create_task(self):
        task_description = self.input_adapter.create_task()
        task = f"[ ] {task_description}"
        self.output_adapter.display_task(task)
        self.output_adapter.save_task(task)

    def get_task(self, task_id):
        task = self.input_adapter.get_task(task_id)
        self.output_adapter.display_task(task)