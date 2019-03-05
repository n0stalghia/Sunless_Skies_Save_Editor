# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_window.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(250, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Version = QtWidgets.QLabel(AboutDialog)
        self.label_Version.setObjectName("label_Version")
        self.verticalLayout.addWidget(self.label_Version)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_About_License = QtWidgets.QLabel(AboutDialog)
        self.label_About_License.setMinimumSize(QtCore.QSize(0, 0))
        self.label_About_License.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_About_License.setWordWrap(True)
        self.label_About_License.setObjectName("label_About_License")
        self.verticalLayout.addWidget(self.label_About_License)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_About_Close = QtWidgets.QPushButton(AboutDialog)
        self.pushButton_About_Close.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_About_Close.setObjectName("pushButton_About_Close")
        self.gridLayout.addWidget(self.pushButton_About_Close, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "Dialog"))
        self.label_Version.setText(_translate("AboutDialog", "Sunless Skies Save Editor"))
        self.label_About_License.setText(_translate("AboutDialog", "<html><head/><body><p>Distributed under <a href=\"https://www.gnu.org/licenses/gpl-3.0.en.html\"><span style=\" text-decoration: underline; color:#0000ff;\">GNU General Public License v3.0</span></a>.</p><p>Thanks to:</p><p>- 1410c and his <a href=\"https://steamcommunity.com/sharedfiles/filedetails/?id=1456294858\"><span style=\" text-decoration: underline; color:#0000ff;\">Steam Guide</span></a> that I extensively used for reference when creating this save editor.</p><p>- Felix for his help with the Linux releases</p><p>- Gibbed for his Save Editors (in particular for Borderlands 2 and TPS)</p></body></html>"))
        self.pushButton_About_Close.setText(_translate("AboutDialog", "Close"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutDialog = QtWidgets.QDialog()
    ui = Ui_AboutDialog()
    ui.setupUi(AboutDialog)
    AboutDialog.show()
    sys.exit(app.exec_())
