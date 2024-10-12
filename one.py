from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox

app = QApplication([])

app.setStyleSheet("Qlabel {font-size:16px}")

window = QWidget()
window.setWindowTitle("Конкурс від Crazy People")
window.resize(450,300)
window.move(500,300)


question = QLabel("В якому році канал отримав <золоту кнопку> від YouTube?")
number1 = QRadioButton("2005")
number2 = QRadioButton("2010")
number3 = QRadioButton("2020")
number4 = QRadioButton("2015")

layout1 = QHBoxLayout()
layout1.addWidget(number1, alignment= Qt.AlignCenter)
layout1.addWidget(number2, alignment= Qt.AlignCenter)

layout2 = QHBoxLayout()
layout2.addWidget(number3,alignment= Qt.AlignCenter)
layout2.addWidget(number4,alignment= Qt.AlignCenter)

main_layout = QVBoxLayout()
main_layout.addWidget(question, alignment= Qt.AlignCenter)
main_layout.addLayout(layout1)
main_layout.addLayout(layout2)

window.setLayout(main_layout)

def win():
    qm = QMessageBox()
    qm.setText("You win")
    qm.exec_()

def lose():
    qm = QMessageBox()
    qm.setText("You lose")
    qm.exec_()



number1.clicked.connect(lose)    
number2.clicked.connect(lose)    
number3.clicked.connect(lose)    
number4.clicked.connect(win)    


window.show()
app.exec_()
