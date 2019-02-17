from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from window_design import Ui_MainWindow
import sys
import window_helper


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Button Events
        self.ui.pushButton_Open.clicked.connect(self.open_file_dialog)

        self.show()

    def open_file_dialog(self):
        file_path = window_helper.get_file_path(sys.platform)
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open', file_path,
                                                   'Autosave (autosave_s.json);;JSON Files (*.json);;All Files (*)',
                                                   options=options)
        if file_name:
            self.ui.label_LoadedFileName.setText(window_helper.get_display_name(file_name))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
