from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from scraping_data_page import ScrapData
from estimate_price_page import EstimatePrice


class Main(object):

    def open_scrap_data(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ScrapData()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_estimate_price(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = EstimatePrice()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(-10, -10, 821, 621))
        self.background.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")
        self.background.setText("")
        self.background.setObjectName("background")
        self.button2 = QtWidgets.QPushButton(Form)
        self.button2.setGeometry(QtCore.QRect(330, 330, 160, 60))
        self.button2.setStyleSheet("QPushButton{\n"
                                    "font-size:18px;\n"
                                    "border-radius:10px;\n"
                                    "background:rgba(85, 98, 112, 255);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color:rgba(255,107,107,255);\n"
                                    "}\n"
                                    "")
        self.button2.setObjectName("buttton2")
        self.button1 = QtWidgets.QPushButton(Form)
        self.button1.setGeometry(QtCore.QRect(330, 260, 160, 60))
        self.button1.setStyleSheet("QPushButton{\n"
                                   "font-size:18px;\n"
                                   "border-radius:10px;\n"
                                   "background:rgba(85, 98, 112, 255);\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color:rgba(255,107,107,255);\n"
                                   "}\n"
                                   "")
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.open_scrap_data)
        self.button2.clicked.connect(self.open_estimate_price)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(225, 50, 350, 111))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle("House Price Prediction")
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("House Price Prediction", "House Price Prediction"))
        self.button2.setText(_translate("Form", "Estimite Price"))
        self.button1.setText(_translate("Form", "Scrap Data"))
        self.label.setText(_translate("Form", "House Price Prediction"))
        Form.setWindowIcon(QIcon("logo.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Main()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
