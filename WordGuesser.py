# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guesser.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Guesser(object):
    def setupUi(self, Guesser):
        Guesser.setObjectName("Guesser")
        Guesser.resize(300, 200)
        self.centralwidget = QtWidgets.QWidget(Guesser)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 301, 180))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_tries = QtWidgets.QLabel(self.frame)
        self.label_tries.setGeometry(QtCore.QRect(20, 10, 121, 16))
        self.label_tries.setObjectName("label_tries")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 10, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lineEdit_enword = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_enword.setGeometry(QtCore.QRect(80, 80, 140, 20))
        self.lineEdit_enword.setObjectName("lineEdit_enword")
        self.pushButton_confirm = QtWidgets.QPushButton(self.frame)
        self.pushButton_confirm.setGeometry(QtCore.QRect(110, 130, 75, 23))
        self.pushButton_confirm.setObjectName("pushButton_confirm")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 110, 81, 16))
        self.label.setObjectName("label")
        self.label_ruword = QtWidgets.QLabel(self.frame)
        self.label_ruword.setGeometry(QtCore.QRect(70, 50, 141, 16))
        self.label_ruword.setObjectName("label_ruword")
        Guesser.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Guesser)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        Guesser.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Guesser)
        self.statusbar.setObjectName("statusbar")
        Guesser.setStatusBar(self.statusbar)

        self.retranslateUi(Guesser)
        QtCore.QMetaObject.connectSlotsByName(Guesser)

    def retranslateUi(self, Guesser):
        _translate = QtCore.QCoreApplication.translate
        Guesser.setWindowTitle(_translate("Guesser", "Guess the translation"))
        self.label_tries.setText(_translate("Guesser", "Оставшиеся попытки:"))
        self.pushButton_confirm.setText(_translate("Guesser", "Проверить"))
        self.label.setText(_translate("Guesser", ""))
        self.label_ruword.setText(_translate("Guesser", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Guesser = QtWidgets.QMainWindow()
    ui = Ui_Guesser()
    ui.setupUi(Guesser)
    Guesser.show()
    sys.exit(app.exec_())