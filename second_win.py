from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QLCDNumber, QMessageBox
from PyQt5.QtGui import QFont
from instr import *
from final_win import FinalWin

class Experiment():
    def __init__(self, name, age, result1, result2, result3):
        self.name = name
        self.age = age
        self.result1 = result1
        self.result2 = result2
        self.result3 = result3

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
        self.result1_input.setDisabled(True)
        self.result1_input.setPlaceholderText(txt_hinttest1)

        self.test_2 = QLabel(txt_test2)
        self.btn_begin_2 = QPushButton(txt_starttest2)
        self.btn_begin_2.setDisabled(True)

        self.test_3 = QLabel(txt_test3)
        self.btn_begin_3 = QPushButton(txt_starttest3)
        self.btn_begin_3.setDisabled(True)
        self.result2_input = QLineEdit()
        self.result2_input.setDisabled(True)
        self.result3_input = QLineEdit()
        self.result3_input.setDisabled(True)
        self.result2_input.setPlaceholderText(txt_hinttest2)
        self.result3_input.setPlaceholderText(txt_hinttest3)

        self.btn_total = QPushButton(txt_sendresults)

        self.text_timer = QLabel(txt_timer)

        self.error = QMessageBox()

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

        self.v_line2.addWidget(self.text_timer, alignment=Qt.AlignRight)
                
        self.h_line.addLayout(self.v_line)
        self.h_line.addLayout(self.v_line2)
        self.setLayout(self.h_line)

    def connects(self):
        self.btn_total.clicked.connect(self.next_click)
        self.btn_begin_1.clicked.connect(self.first_timer)
        self.btn_begin_2.clicked.connect(self.second_timer)
        self.btn_begin_3.clicked.connect(self.third_timer)

    def first_timer(self):
        global time
        
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time

        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('mm:ss'))
        self.text_timer.setFont(QFont('Times', 32, QFont.Bold))

        if time.toString('mm:ss') == '00:00':
            self.btn_begin_2.setDisabled(False)
            self.btn_begin_1.setDisabled(True)

            self.result1_input.setDisabled(False)

            self.timer.stop()

    def second_timer(self):
        global time

        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        global time

        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('ss'))
        self.text_timer.setFont(QFont('Times', 32, QFont.Bold))

        if time.toString('ss') == '00':
            self.btn_begin_3.setDisabled(False)
            self.btn_begin_2.setDisabled(True)
            self.timer.stop()

    def third_timer(self):
        global time

        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer3Event(self):
        global time

        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:ss'))
        self.text_timer.setFont(QFont('Times', 32, QFont.Bold))

        if time.toString('hh:ss') == '00:00':
            self.result3_input.setDisabled(False)

            self.timer.stop()
        
        if time.toString('hh:ss') >= '00:45':
            self.text_timer.setStyleSheet('color: #00FF00')
        elif time.toString('hh:ss') <= '00:15':
            self.text_timer.setStyleSheet('color: #00FF00')
        else:
            self.text_timer.setStyleSheet('color: #000000')
            self.result2_input.setDisabled(False)

    def next_click(self):
        if not self.name_input.text():
            self.error.setText('Ошибка! Не введено имя!')
            self.error.show()
        elif not self.age_input.text() or not self.age_input.text().isdigit() or int(self.age_input.text()) < 7:
            self.error.setText('Ошибка! Некорректное значение возраста!')
            self.error.show()
        
        elif not self.result1_input.text() or not self.result1_input.text().isdigit() or int(self.result1_input.text()) <= 0:
            self.error.setText('Ошибка! Некоректное значение первого измерения!')
            self.error.show()

        elif not self.result2_input.text() or not self.result2_input.text().isdigit() or int(self.result1_input.text()) <= 0:
            self.error.setText('Ошибка! Некоректное значение второго измерения!')
            self.error.show()

        elif not self.result3_input.text() or not self.result3_input.text().isdigit() or int(self.result1_input.text()) <= 0:
            self.error.setText('Ошибка! Некоректное значение третьего измерения!')
            self.error.show()

        else:
            self.hide()

            self.exp = Experiment(self.name_input.text(), int(self.age_input.text()), int(self.result1_input.text()),
            int(self.result2_input.text()), int(self.result3_input.text()))
            self.fw = FinalWin(self.exp)
