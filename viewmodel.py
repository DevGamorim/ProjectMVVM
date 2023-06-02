from model import Task

class TaskViewModel:
    def __init__(self, view):
        self.view = view

    def add_task(self):
        description = self.view.get_user_input()
        task = Task(description)
        self.view.tasks.append(task)

    def complete_task(self, index):
        self.view.tasks[index].completed = True

    def run(self):
        while True:
            self.view.display_tasks()
            command = input("Digite 'add' para adicionar uma tarefa ou 'complete <número>' para completar uma tarefa: ")

            if command == "add":
                self.add_task()
            elif command.startswith("complete"):
                index = int(command.split()[1])
                try:
                    self.complete_task(index)
                except:
                    print("Erro tente novamente!")
