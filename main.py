
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QSize, QTimer, Qt

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mode = 'work'
        self.work_time = 25
        self.short_break = 5
        self.long_break = 15
        self.session_count = 0
        self.next_time = self.short_break*60
        self.remaining = self.work_time*60
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_upd)

        self.setWindowTitle("My App")

        self.button_start = QPushButton("START")
        self.button_start.setCheckable(True)
        self.button_start.clicked.connect(self.btn_clicked)

        self.button_settings = QPushButton("settings")
        self.button_settings.setFixedWidth(120)

        self.main_timer = QLabel(f'{int(self.remaining)//60:02d}:{int(self.remaining%60):02d}')
        self.main_timer.setFixedHeight(70)
        self.main_timer.setStyleSheet("font-size:64px;")
        self.main_timer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.off_timer = QLabel(f'{int(self.next_time//60):02d}:{int(self.next_time%60):02d}')
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

        

    def timer_upd(self):
        self.remaining -= 1

        m = int(self.remaining//60)
        s = int(self.remaining%60)
        self.main_timer.setText(f'{m:02d}:{s:02d}')
        self.off_timer.setText(f'{int(self.next_time//60):02d}:{int(self.next_time%60):02d}')
        if self.remaining <= 0:
            if self.mode == 'work':
                self.session_count += 1
                if self.session_count % 4 == 0:
                    self.mode = 'long break'
                    self.remaining = self.long_break*60
                    self.session_count = 0
                    self.next_time = self.work_time*60
                else:
                    self.mode = 'break'
                    self.remaining = self.short_break*60
                    self.next_time = self.work_time*60

            else:
                self.mode = 'work'
                self.remaining = self.work_time*60
                if self.session_count % 3 == 0:
                    self.next_time = self.long_break*60
                else:
                    self.next_time = self.short_break*60

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
