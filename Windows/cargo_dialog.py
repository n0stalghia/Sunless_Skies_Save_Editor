# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cargo_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CargoDialog(object):
    def setupUi(self, CargoDialog):
        CargoDialog.setObjectName("CargoDialog")
        CargoDialog.resize(400, 500)
        CargoDialog.setStyleSheet("QLineEdit[valid=false]{color: rgb(255,0,0)}\n"
"QLineEdit[valid=true]{color: rgb(0,0,0)}\n"
"QLabel[valid=false]{color: rgb(255,0,0)}\n"
"QLabel[valid=true]{color: rgb(0,0,0)}")
        self.verticalLayout = QtWidgets.QVBoxLayout(CargoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_Cargo_Amount = QtWidgets.QLineEdit(CargoDialog)
        self.lineEdit_Cargo_Amount.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_Cargo_Amount.setObjectName("lineEdit_Cargo_Amount")
        self.gridLayout.addWidget(self.lineEdit_Cargo_Amount, 1, 1, 1, 1)
        self.lineEdit_Cargo_ID = QtWidgets.QLineEdit(CargoDialog)
        self.lineEdit_Cargo_ID.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_Cargo_ID.setObjectName("lineEdit_Cargo_ID")
        self.gridLayout.addWidget(self.lineEdit_Cargo_ID, 1, 0, 1, 1)
        self.label_Cargo_ID = QtWidgets.QLabel(CargoDialog)
        self.label_Cargo_ID.setObjectName("label_Cargo_ID")
        self.gridLayout.addWidget(self.label_Cargo_ID, 0, 0, 1, 1)
        self.label_Amount = QtWidgets.QLabel(CargoDialog)
        self.label_Amount.setObjectName("label_Amount")
        self.gridLayout.addWidget(self.label_Amount, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.listWidget_Cargo = QtWidgets.QListWidget(CargoDialog)
        self.listWidget_Cargo.setObjectName("listWidget_Cargo")
        self.verticalLayout.addWidget(self.listWidget_Cargo)
        self.label_Info = QtWidgets.QLabel(CargoDialog)
        self.label_Info.setWordWrap(True)
        self.label_Info.setObjectName("label_Info")
        self.verticalLayout.addWidget(self.label_Info)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Add = QtWidgets.QPushButton(CargoDialog)
        self.pushButton_Add.setEnabled(False)
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.horizontalLayout.addWidget(self.pushButton_Add)
        self.pushButton_Discard = QtWidgets.QPushButton(CargoDialog)
        self.pushButton_Discard.setObjectName("pushButton_Discard")
        self.horizontalLayout.addWidget(self.pushButton_Discard)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(CargoDialog)
        QtCore.QMetaObject.connectSlotsByName(CargoDialog)
        CargoDialog.setTabOrder(self.lineEdit_Cargo_ID, self.lineEdit_Cargo_Amount)
        CargoDialog.setTabOrder(self.lineEdit_Cargo_Amount, self.listWidget_Cargo)
        CargoDialog.setTabOrder(self.listWidget_Cargo, self.pushButton_Add)
        CargoDialog.setTabOrder(self.pushButton_Add, self.pushButton_Discard)

    def retranslateUi(self, CargoDialog):
        _translate = QtCore.QCoreApplication.translate
        CargoDialog.setWindowTitle(_translate("CargoDialog", "Add Cargo"))
        self.label_Cargo_ID.setText(_translate("CargoDialog", "Cargo ID"))
        self.label_Amount.setText(_translate("CargoDialog", "Amount"))
        self.label_Info.setText(_translate("CargoDialog", "Select an item from the list above or provide a custom ID if what you\'re looking for is not present in the list"))
        self.pushButton_Add.setText(_translate("CargoDialog", "Add"))
        self.pushButton_Discard.setText(_translate("CargoDialog", "Discard"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CargoDialog = QtWidgets.QDialog()
    ui = Ui_CargoDialog()
    ui.setupUi(CargoDialog)
    CargoDialog.show()
    sys.exit(app.exec_())
