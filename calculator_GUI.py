# from __future__ import unicode_literal  # obsługa polskich liter
import calculator
from PyQt5.QtWidgets import QApplication, QWidget  # importujemy klasy z modulu
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout  # linia edyccji, przycisk
from PyQt5.QtWidgets import QMessageBox  # tworzy komunikaty
from PyQt5.QtCore import Qt  # zawiera stale


class calculator_window(QWidget):  # klasa dziedziczaca
    def __init__(self, parent=None):  # zwraca nam klase rodzica i wywoluje jego konstruktor
        super().__init__(parent)

        self.interfejs()  # wywolujemy konstruktor / klasa interfejs

    def interfejs(self):
        """
           - etykiety
           - przypisanie widgetow do ukladu tabelarycznego
           - przypisanie utworzonego ukladu do okna
           - widzeta
           - okna do wprowadzenia danych
           - przyciski działań matematycznych
           - zwiazanie przyciskow do funkcji operacji
        """

        label1 = QLabel("Number 1:", self)  # etykiety
        label2 = QLabel("Number 2:", self)
        label3 = QLabel("Result:", self)

        layoutT = QGridLayout()  # QGridLayout - przypisanie umiejscowienia widgetow do ukladu tabelarycznego
        layoutT.addWidget(label1, 0, 0)  # addWidget - przypisanie etykiety do okna aplikacji
        layoutT.addWidget(label2, 0, 1)
        layoutT.addWidget(label3, 0, 2)

        self.setLayout(layoutT)  # przypisanie utworzonego układu do okna aplikacji

        self.number1Edt = QLineEdit()  # 1-liniowe pola edycyjne
        self.number2Edt = QLineEdit()
        self.resultEdt = QLineEdit()

        self.resultEdt.readonly = True  # mozliwosc odczytu pola tekstowego
        self.resultEdt.setToolTip("")  # ustala odpowiedz

        layoutT.addWidget(self.number1Edt, 1, 0)
        layoutT.addWidget(self.number2Edt, 1, 1)
        layoutT.addWidget(self.resultEdt, 1, 2)

        addBtn = QPushButton("&Add", self)  # przyciski
        subtractBtn = QPushButton("&Subtract", self)
        divideBtn = QPushButton("&Divide", self)
        multiplyBtn = QPushButton("&Multiply", self)
        exitBtn = QPushButton("&Exit", self)
        exitBtn.resize(exitBtn.sizeHint())  # sugerowana wielkosc obiektu

        exitBtn.clicked.connect(self.exit)  # zwiazanie przycisku "Exit" z metoda exit
        addBtn.clicked.connect(self.operation)
        subtractBtn.clicked.connect(self.operation)
        multiplyBtn.clicked.connect(self.operation)
        divideBtn.clicked.connect(self.operation)

        layoutH = QHBoxLayout()  # uklad horyzontalny
        layoutH.addWidget(addBtn)
        layoutH.addWidget(subtractBtn)
        layoutH.addWidget(divideBtn)
        layoutH.addWidget(multiplyBtn)

        layoutT.addLayout(layoutH, 2, 0, 1, 3)  # uklad tabelaryczny przyciskow: co chcemy wstawic, wiersze i kolumny wstawiania
        layoutT.addWidget(exitBtn, 3, 0, 1, 3)

        self.setGeometry(150, 150, 300, 100)  # okresla polozenia okna aplikacji
        self.setWindowIcon(QIcon('calculator_icon.png'))  # setWindowIcon - stworzenie widzety - ikony kalkulatora
        self.setWindowTitle("Simple calculator")  # setWindowTitle - opis nagłowka programu
        self.show()

    def exit(self):
        """
            Exit the program.
        """
        self.close()

    def closeEvent(self, event):  # nazwa funkcji jest bardzo wazna! - nie zmieniac
        """
            Dialog box "Are you sure you shut up?" when exiting the program.
        """

        answer = QMessageBox.question(  # tworze okno dialogowe
            self, 'message',  # naglowek okna
            "Are you sure you want to close?",  # pytanie w oknie
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  # komibancja przyciskow "YES' i "NO" oraz przycisku domyslnego

        if answer == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):  # nazwa funkcji jest bardzo wazna! - nie zmieniac
        """
            Close the program with the ESC button.
        """
        if e.key() == Qt.Key_Escape:
            self.close()

    def operation(self):
        """
            Entered data is sent back to the calculation module (calculator.py) and the result is obtained back.
        """
        user = self.sender()


        try:  # jesli wprowadzone zmienne nie da rady zmienic na float wyswietl blad
            number1 = float(self.number1Edt.text())
            number2 = float(self.number2Edt.text())
            result = ""
            self.calc = calculator.Calculator(number1, number2)

            if user.text() == "&Add":
                result = self.calc.add()
            elif user.text() == "&Subtract":
                result = self.calc.subtract()
            elif user.text() == "&Multiply":
                result = self.calc.multiply()
            else:  # dzielenie
                try:
                    result = round(self.calc.divide(), 9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Error", "Can not divide by zero!")
                    return

            self.resultEdt.setText(str(result))  # wyswietlanie wyniku w oknie "Result"

        except ValueError:
            QMessageBox.warning(self, "Error", "Incorrect data", QMessageBox.Ok)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)  # reprezentuje aplikacje
    window = calculator_window()
    sys.exit(app.exec_())  # głowna petla programu