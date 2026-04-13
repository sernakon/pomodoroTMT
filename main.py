from typing import Container

from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize, Qt

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button = QPushButton("Erase~~")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.btn_clicked)

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        
        self.setFixedSize(QSize(300, 400))


        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def btn_clicked(self):
        self.input.setText("")




app = QApplication(sys.argv)

window = MainWindow()
window.show()



app.exec()
