from view import TaskView
from viewmodel import TaskViewModel

view = TaskView()
viewModel = TaskViewModel(view)
viewModel.run()
