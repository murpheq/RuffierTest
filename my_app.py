from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from instr import *
from second_win import TestWin

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.next_btn = QPushButton(txt_next)
        
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.hello_text, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.instruction, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.next_btn, alignment=Qt.AlignCenter)
        self.setLayout(self.v_line)

    def connects(self):
        self.next_btn.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = TestWin()

app = QApplication([])
main = MainWindow()
app.exec()
    