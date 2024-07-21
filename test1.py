from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QHBoxLayout, QMessageBox, QRadioButton)
app = QApplication([])
main_win = QWidget()
question = QLabel('В каком году было основана Алгоритмика?')
btn_answer1 = QRadioButton('2013')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2016')
btn_answer4 = QRadioButton('2019')
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment= Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment= Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment= Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment= Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment= Qt.AlignCenter)
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)

def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Верно')
    victory_win.exec_()
def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('Неверно! Попробуйте снова!')
    victory_win.exec_()
btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_win)
btn_answer4.clicked.connect(show_lose)
main_win.setLayout(layout_main)
main_win.show()
app.exec_()