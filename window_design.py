# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sunless_skies.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonOpen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.horizontalLayout_3.addWidget(self.pushButtonOpen)
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_3.addWidget(self.pushButtonSave)
        self.pushButtonAbout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAbout.setObjectName("pushButtonAbout")
        self.horizontalLayout_3.addWidget(self.pushButtonAbout)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelLoadedFile = QtWidgets.QLabel(self.centralwidget)
        self.labelLoadedFile.setMaximumSize(QtCore.QSize(90, 16777215))
        self.labelLoadedFile.setObjectName("labelLoadedFile")
        self.horizontalLayout_2.addWidget(self.labelLoadedFile)
        self.labelLoadedFileName = QtWidgets.QLabel(self.centralwidget)
        self.labelLoadedFileName.setObjectName("labelLoadedFileName")
        self.horizontalLayout_2.addWidget(self.labelLoadedFileName)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_stats = QtWidgets.QWidget()
        self.tab_stats.setObjectName("tab_stats")
        self.tabWidget.addTab(self.tab_stats, "")
        self.tab_hold = QtWidgets.QWidget()
        self.tab_hold.setObjectName("tab_hold")
        self.tabWidget.addTab(self.tab_hold, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sunless Skies Save Editor"))
        self.pushButtonOpen.setText(_translate("MainWindow", "Open"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonAbout.setText(_translate("MainWindow", "About"))
        self.labelLoadedFile.setText(_translate("MainWindow", "Loaded savefile:"))
        self.labelLoadedFileName.setText(_translate("MainWindow", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stats), _translate("MainWindow", "Stats"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_hold), _translate("MainWindow", "Hold"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
