class TaskView:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        for task in self.tasks:
            if task.completed:
                print("[X] " + task.description)
            else:
                print("[ ] " + task.description)

    def get_user_input(self):
        return input("Digite a descrição da tarefa: ")
