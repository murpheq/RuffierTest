from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from instr import *
import second_win

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initUI()
        self.show()
        
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.lbl_name = QLabel(f'имя: {self.exp.name}')
        self.lbl_age = QLabel(f'возраст: {self.exp.age}')
        self.work_heart = QLabel(txt_workheart + self.results())
        self.lbl_index = QLabel(txt_index + str(self.index))
        
        self.v_line = QVBoxLayout()
        
        self.v_line.addWidget(self.lbl_name, alignment=Qt.AlignCenter)

        self.v_line.addWidget(self.lbl_age, alignment=Qt.AlignCenter)

        self.v_line.addWidget(self.lbl_index, alignment=Qt.AlignCenter)

        self.v_line.addWidget(self.work_heart, alignment=Qt.AlignCenter)

        self.setLayout(self.v_line)

    def results(self):
        self.index = (4*(int(self.exp.result1) + int(self.exp.result2) + int(self.exp.result3)) - 200) / 10

        if self.exp.age >= 15:
            if self.index >= 15:
                return txt_res1
            elif self.index >= 11:
                return txt_res2
            elif self.index >= 6:
                return txt_res3
            elif self.index >= 0.5:
                return txt_res4
            return txt_res5

        elif self.exp.age >= 13:
            if self.index >= 16.5:
                return txt_res1
            elif self.index >= 12.5:
                return txt_res2
            elif self.index >= 7.5:
                return txt_res3
            elif self.index >= 2:
                return txt_res4
            return txt_res5

        elif self.exp.age >= 11:
            if self.index >= 18:
                return txt_res1
            elif self.index >= 14:
                return txt_res2
            elif self.index >= 9:
                return txt_res3
            elif self.index >= 3.5:
                return txt_res4
            return txt_res5

        elif self.exp.age >= 9:
            if self.index >= 19.5:
                return txt_res1
            elif self.index >= 15.5:
                return txt_res2
            elif self.index >= 10.5:
                return txt_res3
            elif self.index >= 5:
                return txt_res4
            return txt_res5

        elif self.exp.age >= 7:
            if self.index >= 21:
                return txt_res1
            elif self.index >= 17:
                return txt_res2
            elif self.index >= 12:
                return txt_res3
            elif self.index >= 6.5:
                return txt_res4
            return txt_res5
        