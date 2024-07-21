from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QPushButton, QLabel, QVBoxLayout)
from random import randint

app =QApplication([])
main_win = QWidget()
main_win.setWindowTitle('пределитель победителя')
but = QPushButton('Сгенерировать')
text = QLabel('Нажми чтобы узнать победителя')
winner = QLabel('?')
line = QVBoxLayout()
line.addWidget(text,alignment= Qt.AlignCenter)
line.addWidget(winner,alignment= Qt.AlignCenter)
line.addWidget(but, alignment= Qt.AlignCenter)

def show_winner():
    number = randint(0,99)
    winner.setText(str(number))
    text.setText('Победитель: ')

but.clicked.connect(show_winner)
main_win.setLayout(line)
main_win.show()
app.exec_()