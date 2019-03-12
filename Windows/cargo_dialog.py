# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/mark/PycharmProjects/Sunless Skies Save Editor/Qt Designer UI/cargo_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CargoDialog(object):
    def setupUi(self, CargoDialog):
        CargoDialog.setObjectName("CargoDialog")
        CargoDialog.resize(384, 350)
        self.verticalLayout = QtWidgets.QVBoxLayout(CargoDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(CargoDialog)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(CargoDialog)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(CargoDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(CargoDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.listWidget = QtWidgets.QListWidget(CargoDialog)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.label_3 = QtWidgets.QLabel(CargoDialog)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(CargoDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CargoDialog)
        self.buttonBox.accepted.connect(CargoDialog.accept)
        self.buttonBox.rejected.connect(CargoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CargoDialog)

    def retranslateUi(self, CargoDialog):
        _translate = QtCore.QCoreApplication.translate
        CargoDialog.setWindowTitle(_translate("CargoDialog", "Dialog"))
        self.label.setText(_translate("CargoDialog", "Cargo ID"))
        self.label_2.setText(_translate("CargoDialog", "Amount"))
        self.label_3.setText(_translate("CargoDialog", "Select an ID from the list above or provide a custom ID if what you\'re looking for is not present in the list"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CargoDialog = QtWidgets.QDialog()
    ui = Ui_CargoDialog()
    ui.setupUi(CargoDialog)
    CargoDialog.show()
    sys.exit(app.exec_())
