import webbrowser
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class WebSite(QMainWindow):
    def __init__(self):
        super(WebSite, self).__init__()
        self.setGeometry(500, 500, 300, 300)
        self.setWindowTitle("Click To Browse")
        self.initUI()

    def initUI(self):
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Google.com")
        self.b1.setGeometry(QtCore.QRect(180, 260, 89, 25))
        self.b1.clicked.connect(self.clicked)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("EXIT")
        self.b2.setGeometry(QtCore.QRect(330, 260, 89, 25))
        self.b2.clicked.connect(self.clicked2)

    def clicked(self):
        webbrowser.open("https://google.com")
    def clicked2(self):
        exit()

def window():
    app = QApplication(sys.argv)
    win = WebSite()
    win.show()
    sys.exit(app.exec_())
window()

