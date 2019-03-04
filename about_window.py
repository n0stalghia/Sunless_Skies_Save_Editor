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
        AboutDialog.resize(220, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(AboutDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_About_License = QtWidgets.QLabel(AboutDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_About_License.sizePolicy().hasHeightForWidth())
        self.label_About_License.setSizePolicy(sizePolicy)
        self.label_About_License.setMinimumSize(QtCore.QSize(0, 100))
        self.label_About_License.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_About_License.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_About_License.setWordWrap(True)
        self.label_About_License.setObjectName("label_About_License")
        self.gridLayout.addWidget(self.label_About_License, 1, 0, 1, 1)
        self.label_Version = QtWidgets.QLabel(AboutDialog)
        self.label_Version.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_Version.setObjectName("label_Version")
        self.gridLayout.addWidget(self.label_Version, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_About_Close = QtWidgets.QPushButton(AboutDialog)
        self.pushButton_About_Close.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_About_Close.setObjectName("pushButton_About_Close")
        self.gridLayout_2.addWidget(self.pushButton_About_Close, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "Dialog"))
        self.label_About_License.setText(_translate("AboutDialog", "<html><head/><body><p>Distributed under <a href=\"https://www.gnu.org/licenses/gpl-3.0.en.html\"><span style=\" text-decoration: underline; color:#0000ff;\">GNU General Public License v3.0</span></a>.</p><p>Many thanks to 1410c and his <a href=\"https://steamcommunity.com/sharedfiles/filedetails/?id=1456294858\"><span style=\" text-decoration: underline; color:#0000ff;\">Steam Guide</span></a> that I extensively used for reference when creating this save editor.</p></body></html>"))
        self.label_Version.setText(_translate("AboutDialog", "Sunless Skies Save Editor "))
        self.pushButton_About_Close.setText(_translate("AboutDialog", "Close"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutDialog = QtWidgets.QDialog()
    ui = Ui_AboutDialog()
    ui.setupUi(AboutDialog)
    AboutDialog.show()
    sys.exit(app.exec_())
