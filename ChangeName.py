from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow 
import sys


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setGeometry(500, 500, 300, 300)
        self.setWindowTitle("Pranav is Great")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Whats your Name?")
        self.label.move(50,50)
        self.update()

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Here")
        self.b1.setGeometry(QtCore.QRect(180, 260, 89, 25))
        self.b1.clicked.connect(self.clicked)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Clear")
        self.b2.setGeometry(QtCore.QRect(330, 260, 89, 25))
        self.b2.clicked.connect(self.clicked2)
    
    def clicked(self):
        self.label.setText("This is Pranav")
        self.update()

    def clicked2(self):
        self.label.setText(" ")
        self.update()


    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())
window()

