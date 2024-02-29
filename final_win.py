from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from instr import *
import second_win

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.lbl_name = QLabel(f'имя: ')
        self.lbl_age = QLabel(f'возраст: ')
        self.lbl_index = QLabel(txt_index)
        self.work_heart = QLabel(txt_workheart)
        
        self.v_line = QVBoxLayout()
        
        self.v_line.addWidget(self.lbl_name, alignment=Qt.AlignCenter)

        self.v_line.addWidget(self.lbl_age, alignment=Qt.AlignCenter)

        self.v_line.addWidget(self.lbl_index, alignment=Qt.AlignCenter)

        self.v_line.addWidget(self.work_heart, alignment=Qt.AlignCenter)

        self.setLayout(self.v_line)
