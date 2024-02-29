from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QLCDNumber
from instr import *
from final_win import FinalWin

class TestWin(QWidget):
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
        self.name = QLabel(txt_name)
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText(txt_hintname)
        self.get_name = self.name_input.text()

        self.age = QLabel(txt_age)
        self.age_input = QLineEdit()
        self.get_age = self.age_input.text()
        # self.age_input.setPlaceholderText()

        self.test_1 = QLabel(txt_test1)
        self.btn_begin_1 = QPushButton(txt_starttest1)
        self.result1_input = QLineEdit()
        self.result1_input.setPlaceholderText(txt_hinttest1)

        self.test_2 = QLabel(txt_test2)
        self.btn_begin_2 = QPushButton(txt_starttest2)

        self.test_3 = QLabel(txt_test3)
        self.btn_begin_3 = QPushButton(txt_starttest3)
        self.result2_input = QLineEdit()
        self.result3_input = QLineEdit()
        self.result2_input.setPlaceholderText(txt_hinttest2)
        self.result3_input.setPlaceholderText(txt_hinttest3)

        self.btn_total = QPushButton(txt_sendresults)

        self.timer = QLabel(txt_timer)

        self.h_line = QHBoxLayout()

        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.name, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.name_input, alignment=Qt.AlignLeft)

        self.v_line.addWidget(self.age, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.age_input, alignment=Qt.AlignLeft)

        self.v_line.addWidget(self.test_1, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.btn_begin_1, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.result1_input, alignment=Qt.AlignLeft)

        self.v_line.addWidget(self.test_2, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.btn_begin_2, alignment=Qt.AlignLeft)

        self.v_line.addWidget(self.test_3, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.btn_begin_3, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.result2_input, alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.result3_input, alignment=Qt.AlignLeft)

        self.v_line.addWidget(self.btn_total, alignment=Qt.AlignCenter)

        self.v_line2 = QVBoxLayout()

        self.v_line2.addWidget(self.timer, alignment=Qt.AlignRight)
                
        self.h_line.addLayout(self.v_line)
        self.h_line.addLayout(self.v_line2)
        self.setLayout(self.h_line)

    def connects(self):
        self.btn_total.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.fw = FinalWin()
