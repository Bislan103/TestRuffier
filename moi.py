import random

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QPushButton, QLabel, QVBoxLayout)
from random import randint
lst = ['пончик', 'кофе', 'сникерс', 'сок']
app =QApplication([])
my_win = QWidget()
v_line = QVBoxLayout()
text = QLabel('')
but = QPushButton('Кликни на меня')
v_line.addWidget(but,alignment= Qt.AlignCenter)

def show_text():
    text.setText('Купи мне ' + random.choice(lst))
    v_line.addWidget(text, alignment= Qt.AlignVCenter)

my_win.setLayout(v_line)
my_win.setWindowTitle('Программист')
my_win.move(500,70)
my_win.resize(400,200)
but.clicked.connect(show_text)
my_win.show()
app.exec_()