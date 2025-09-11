import sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QListWidget
)

class TaskManagerWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Manager (QT6)")
        self.resize(800, 600)

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Write a task (i.e: Buy milk tomorrow at 9am)")

        self.add_button = QPushButton("Add Task")
        self.delete_button = QPushButton("Delete Task")

        self.task_list = QListWidget()

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.task_input)
        main_layout.addWidget(self.task_list)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(self.delete_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TaskManagerWindow()
    window.show()

    sys.exit(app.exec())
