from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout,
                             QHBoxLayout, QMessageBox, QRadioButton,
                             QPushButton)
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Мое первое приложение')
N1 = QRadioButton('1')
N2 = QRadioButton('2')
N3 = QRadioButton('3')
but = QPushButton('Проверить')
layout_main = QVBoxLayout()
layoutN1 = QHBoxLayout()
layoutN2 = QHBoxLayout()
layoutN3 = QHBoxLayout()
layoutN4 = QHBoxLayout()
layoutN1.addWidget(N1, alignment= Qt.AlignLeft)
layoutN2.addWidget(N2, alignment= Qt.AlignLeft)
layoutN3.addWidget(N3, alignment= Qt.AlignLeft)
layoutN4.addWidget(but, alignment= Qt.AlignCenter)
layout_main.addLayout(layoutN1)
layout_main.addLayout(layoutN2)
layout_main.addLayout(layoutN3)
layout_main.addLayout(layoutN4)

my_win.setLayout(layout_main)
my_win.show()
app.exec_()