import sys
import random
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from FahrenheitConverter import Ui_MainWindow as Ui_FahConv
from WordGuesser import Ui_Guesser
from Writer import Ui_MainWindow as Ui_Writer
from Sphere_volume import Ui_MainWindow as Ui_SphereVolume


class TemperatureConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(TemperatureConv, self).__init__()
        self.ui = Ui_FahConv()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Fahrenheit')
        self.ui.line_Input.setPlaceholderText(
            'Entry temperature in Fahrenheit:')

        self.ui.btn_Convert.clicked.connect(self.converter)
        self.ui.btn_Quit.clicked.connect(self.close)

    def converter(self):
        input_line = int(self.ui.line_Input.text())
        celseus = round((input_line-32)*5/9, 4)
        self.ui.label_Input.setText(str(celseus))


class WordGuesser(QtWidgets.QMainWindow):
    words = {
        'car': 'автомобиль', 'boat': 'лодка', 'helicopter': 'вертолёт', 'bike': 'велосипед',
        'driver': 'водитель', 'wheel': 'колесо', 'magazine': 'журнал'}
    counter = 5

    def __init__(self):
        super(WordGuesser, self).__init__()
        self.ui = Ui_Guesser()
        self.ui.setupUi(self)
        random.seed()
        self.init_Guess()

    def init_Guess(self):
        self.setWindowTitle('Word guesser')

        self.ruword = ''
        i = random.randint(0, len(self.words))
        for key, val in self.words.items():
            if i == 0:
                self.ruword = val
            i -= 1
        self.ui.label_ruword.setText(self.ruword)
        self.ui.lcdNumber.display(self.counter)

        self.ui.pushButton_confirm.clicked.connect(self.guessing)

    def guessing(self):
        enword = self.ui.lineEdit_enword.text()
        f = False
        for key, var in self.words.items():
            if self.ruword == var and enword == key:
                f = True
                self.ui.label.setText('Вы угадали!')
                self.ui.lcdNumber.display(999)
        if not f:
            self.ui.label.setText('Вы не угадали :(')
            self.counter -= 1
            self.ui.lcdNumber.display(self.counter)
            self.ui.lineEdit_enword.setText('')
            if self.counter == 0:
                self.close()

class Writer(QtWidgets.QMainWindow):
    def __init__(self):
        super(Writer, self).__init__()
        self.ui = Ui_Writer()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('File creator')
        self.ui.textEdit.setPlaceholderText('Entry text there:')
        self.ui.comboBox.addItem('txt')
        self.ui.comboBox.addItem('html')

        self.ui.pushButton.clicked.connect(self.genfile)

    def genfile(self):
        text = self.ui.textEdit.toPlainText()
        if self.ui.comboBox.currentText() == 'txt':
            # Запись в txt
            file = open('Legal.txt', 'w')
            file.write(text)
            file.close()
        elif self.ui.comboBox.currentText() == 'html':
            # Запись в html
            file = open('Illegal.html', 'w')
            file.write(text)
            file.close()

class SphereVolume(QtWidgets.QMainWindow):
    def __init__(self):
        super(SphereVolume, self).__init__()
        self.ui = Ui_SphereVolume()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Calculate sphere volume')
        self.ui.lineEdit_radius.setPlaceholderText('Entry number there:')
        self.ui.comboBox.addItem('Text')
        self.ui.comboBox.addItem('HTML')
        self.ui.pushButton_calculate.clicked.connect(self.calculate)
        self.ui.pushButton_save.clicked.connect(self.genfile)


    def calculate(self):
        line = self.ui.lineEdit_radius.text()
        try:
            self.volume = 4/3*math.pi*float(line)**3
            self.ui.lineEdit_result.setText(str(round(self.volume, 4)))
        except ValueError:
            self.ui.lineEdit_radius.setText('')
            self.ui.lineEdit_radius.setPlaceholderText('Only number!')



    def genfile(self):
        self.calculate()
        if self.ui.comboBox.currentText() == 'Text':
            # Запись в txt
            file = open('VolumeT.txt', 'w')
            file.write(str(round(self.volume, 6)))
            file.close()
        elif self.ui.comboBox.currentText() == 'HTML':
            # Запись в html
            volume = str(round(self.volume, 6))
            html = """
            <!DOCTYPE html>
            <html lang="Ru">
            <head>
                <meta charset="UTF-8">
            </head>
            <body>
                <div class="result">
                    <h1>"""+ volume +"""</h1>
                </div>
            </body>
            """
            file = open('VolumeH.html', 'w')
            file.write(html)
            file.close()


if __name__ == '__main__':
    ex = int(input('Введите номер задания: '))
    if ex == 1:
        app = QtWidgets.QApplication([])
        appllication = TemperatureConv()
        appllication.show()
        sys.exit(app.exec_())
    elif ex == 2:
        app = QtWidgets.QApplication([])
        appllication = WordGuesser()
        appllication.show()
        sys.exit(app.exec_())
    elif ex == 3:
        app = QtWidgets.QApplication([])
        appllication = Writer()
        appllication.show()
        sys.exit(app.exec_())
    elif ex == 4:
        app = QtWidgets.QApplication([])
        appllication = SphereVolume()
        appllication.show()
        sys.exit(app.exec_())
