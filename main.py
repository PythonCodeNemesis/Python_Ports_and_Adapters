from input_ports import ConsoleTaskInputAdapter
from output_ports import FileTaskOutputAdapter
from application import TaskApplication

if __name__ == "__main__":
    input_adapter = ConsoleTaskInputAdapter()
    output_adapter = FileTaskOutputAdapter()
    app = TaskApplication(input_adapter, output_adapter)

    app.create_task()
    app.get_task(1)