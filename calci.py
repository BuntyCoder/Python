# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calci.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 556)
        self.btn_div = QtWidgets.QPushButton(Form)
        self.btn_div.setGeometry(QtCore.QRect(386, 281, 80, 25))
        self.btn_div.setObjectName("btn_div")
        
        
        self.btn_mul = QtWidgets.QPushButton(Form)
        self.btn_mul.setGeometry(QtCore.QRect(291, 281, 80, 25))
        self.btn_mul.setObjectName("btn_mul")
        
        self.btn_add = QtWidgets.QPushButton(Form)
        self.btn_add.setGeometry(QtCore.QRect(101, 281, 80, 25))
        self.btn_add.setObjectName("btn_add")
        self.btn_add.clicked.connect(self.add)


        self.btn_sub = QtWidgets.QPushButton(Form)
        self.btn_sub.setGeometry(QtCore.QRect(196, 281, 80, 25))
        self.btn_sub.setObjectName("btn_sub")
        
        self.txt1 = QtWidgets.QLineEdit(Form)
        self.txt1.setGeometry(QtCore.QRect(90, 120, 113, 25))
        self.txt1.setObjectName("txt1")
        a = self.txt1.text()
        
        self.txt2 = QtWidgets.QLineEdit(Form)
        self.txt2.setGeometry(QtCore.QRect(290, 120, 113, 25))
        self.txt2.setObjectName("txt2")
        b = self.txt2.text()
        

        self.output = QtWidgets.QLineEdit(Form)
        self.output.setGeometry(QtCore.QRect(490, 120, 113, 25))
        self.output.setObjectName("output")


        # self.output = QtWidgets.QLabel(Form)
        # self.output.setGeometry(QtCore.QRect(546, 116, 111, 31))
        # self.output.setObjectName("output")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_div.setText(_translate("Form", "Div"))
        self.btn_mul.setText(_translate("Form", "Mul"))
        self.btn_add.setText(_translate("Form", "Add"))
        self.btn_sub.setText(_translate("Form", "Sub"))
        #self.output.setText(_translate("Form", "Output"))
    
    def add(self, Form):
        a = int(self.txt1.text())
        b = int(self.txt2.text())
        self.output.setText(str(a + b))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
