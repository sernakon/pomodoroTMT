
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize, QTimer, Qt

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button_start = QPushButton("START")
        self.button_start.setCheckable(True)
        self.button_start.clicked.connect(self.btn_clicked)

        self.button_settings = QPushButton("settings")
        self.button_settings.setFixedWidth(120)

        self.main_timer = QLabel("24:59")
        self.main_timer.setFixedHeight(70)
        self.main_timer.setStyleSheet("font-size:64px;")
        self.main_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.off_timer = QLabel("15:00")
        self.off_timer.setStyleSheet("font-size:24px;")
        self.off_timer.setAlignment(Qt.AlignmentFlag.AlignHCenter)


        self.setFixedSize(QSize(300, 400))


        layout = QVBoxLayout() 
        layout.addWidget(self.button_settings)
        layout.addStretch()
        layout.addWidget(self.main_timer)
        layout.addWidget(self.off_timer)
        layout.addStretch()
        layout.addWidget(self.button_start)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.seconds = 66
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_upd)

    def timer_upd(self):
        self.seconds -= 1
        m = self.seconds//60
        s = self.seconds%60
        self.main_timer.setText(f'{m:02d}:{s:02d}')
        if self.seconds <= 0:
            self.main_timer.setText("next cycle")

    def btn_clicked(self):
        if self.button_start.text() == "START":
            self.button_start.setText("STOP")
            self.timer.start(1000)
        else:
            self.button_start.setText("START")
            self.timer.stop()




app = QApplication(sys.argv)

window = MainWindow()
window.show()



app.exec()
