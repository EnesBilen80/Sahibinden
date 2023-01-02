from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class EstimatePrice(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setStyleSheet("QLineEdit{\n"
                           "background-color:rgba(0,0,0,0);\n"
                           "border: 2px solid rgba(0,0,0,0);\n"
                           "border-bottom-color:rgba(46,82,101,200);\n"
                           "color:rgb(0,0,0);\n"
                           "padding-bottom:7px;\n"
                           "}")
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(-20, -10, 821, 621))
        self.background.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));")
        self.background.setText("")
        self.background.setObjectName("background")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 90, 331, 350))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setPlaceholderText("District")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(420, 90, 331, 350))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_9.setText("")
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_2.addWidget(self.lineEdit_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_2.addWidget(self.lineEdit_12)
        self.button1 = QtWidgets.QPushButton(Form)
        self.button1.setGeometry(QtCore.QRect(330, 490, 160, 60))
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
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(275, 30, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Estimate Price", "Estimate Price"))
        self.label.setText(_translate("Form", "City"))
        self.lineEdit.setPlaceholderText(_translate("Form", "City"))
        self.label_3.setText(_translate("Form", "District"))
        self.label_4.setText(_translate("Form", "Quarter"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Quarter"))
        self.label_2.setText(_translate("Form", "Net m²"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Net m²"))
        self.label_6.setText(_translate("Form", "Number of Rooms"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Number of Rooms"))
        self.label_5.setText(_translate("Form", "Building Age"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Building Age"))
        self.label_7.setText(_translate("Form", "Floor Location"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "Floor Location"))
        self.label_8.setText(_translate("Form", "Number of Floors"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", "Number of Floors"))
        self.label_9.setText(_translate("Form", "Heating"))
        self.lineEdit_9.setPlaceholderText(_translate("Form", "Heating"))
        self.label_10.setText(_translate("Form", "Number of Baths"))
        self.lineEdit_10.setPlaceholderText(_translate("Form", "Number of Baths"))
        self.label_11.setText(_translate("Form", "Balcony"))
        self.lineEdit_11.setPlaceholderText(_translate("Form", "Balcony(Y or N)"))
        self.label_12.setText(_translate("Form", "Furnished"))
        self.lineEdit_12.setPlaceholderText(_translate("Form", "Furnished(Y or N)"))
        self.button1.setText(_translate("Form", "Estimite Price"))
        self.label_13.setText(_translate("Form", "Estimite Price"))
        Form.setWindowIcon(QIcon("logo.png"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = EstimatePrice()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())