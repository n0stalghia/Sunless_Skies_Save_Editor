from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from window_design import Ui_MainWindow
import sys
import window_helper as wh
import json_handler as jh


ERRORS = False


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Button Events
        self.ui.pushButton_Open.clicked.connect(self.open_file_dialog)

        # Line Edit Events
        self.ui.lineEdit_Lvl_Sovereigns.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_Sovereigns,
            target=self.ui.lineEdit_Effective_Sovereigns,
            value=self.ui.lineEdit_Lvl_Sovereigns.text()
        ))
        self.ui.lineEdit_Lvl_Terror.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_Terror,
            target=self.ui.lineEdit_Effective_Terror,
            value=self.ui.lineEdit_Lvl_Terror.text()
        ))
        self.ui.lineEdit_Lvl_Hull.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_Hull,
            target=self.ui.lineEdit_Effective_Hull,
            value=self.ui.lineEdit_Lvl_Hull.text()
        ))
        self.ui.lineEdit_Lvl_Date.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_Date,
            target=self.ui.lineEdit_Effective_Date,
            value=self.ui.lineEdit_Lvl_Date.text()
        ))
        self.ui.lineEdit_Modifier_Hold.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Modifier_Hold,
            target=self.ui.lineEdit_Effective_Hold,
            value=self.ui.lineEdit_Modifier_Hold.text()
        ))
        self.ui.lineEdit_Lvl_Hearts.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_Hearts,
            target=self.ui.lineEdit_Effective_Hearts,
            value=self.ui.lineEdit_Lvl_Hearts.text(),
            value2=self.ui.lineEdit_Modifier_Hearts.text()
        ))
        self.ui.lineEdit_Modifier_Hearts.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Modifier_Hearts,
            target=self.ui.lineEdit_Effective_Hearts,
            value=self.ui.lineEdit_Modifier_Hearts.text(),
            value2=self.ui.lineEdit_Lvl_Hearts.text()
        ))
        self.ui.lineEdit_Lvl_Veils.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_Veils,
            target=self.ui.lineEdit_Effective_Veils,
            value=self.ui.lineEdit_Lvl_Veils.text(),
            value2=self.ui.lineEdit_Modifier_Veils.text()
        ))
        self.ui.lineEdit_Modifier_Veils.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Modifier_Veils,
            target=self.ui.lineEdit_Effective_Veils,
            value=self.ui.lineEdit_Modifier_Veils.text(),
            value2=self.ui.lineEdit_Lvl_Veils.text()
        ))
        self.ui.lineEdit_Lvl_Iron.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_Iron,
            target=self.ui.lineEdit_Effective_Iron,
            value=self.ui.lineEdit_Lvl_Iron.text(),
            value2=self.ui.lineEdit_Modifier_Iron.text()
        ))
        self.ui.lineEdit_Modifier_Iron.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Modifier_Iron,
            target=self.ui.lineEdit_Effective_Iron,
            value=self.ui.lineEdit_Modifier_Iron.text(),
            value2=self.ui.lineEdit_Lvl_Iron.text()
        ))
        self.ui.lineEdit_Lvl_Mirrors.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_Mirrors,
            target=self.ui.lineEdit_Effective_Mirrors,
            value=self.ui.lineEdit_Lvl_Mirrors.text(),
            value2=self.ui.lineEdit_Modifier_Mirrors.text()
        ))
        self.ui.lineEdit_Modifier_Mirrors.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Modifier_Mirrors,
            target=self.ui.lineEdit_Effective_Mirrors,
            value=self.ui.lineEdit_Modifier_Mirrors.text(),
            value2=self.ui.lineEdit_Lvl_Mirrors.text()
        ))
        self.ui.lineEdit_Lvl_CharLvl.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_CharLvl,
            target=self.ui.lineEdit_Effective_CharLvl,
            value=self.ui.lineEdit_Lvl_CharLvl.text()
        ))
        self.ui.lineEdit_Lvl_CharPts.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_CharPts,
            target=self.ui.lineEdit_Effective_CharPts,
            value=self.ui.lineEdit_Lvl_CharPts.text()
        ))
        self.ui.lineEdit_Lvl_Exp.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_Exp,
            target=self.ui.lineEdit_Effective_Exp,
            value=self.ui.lineEdit_Lvl_Exp.text()
        ))
        self.ui.lineEdit_Lvl_SecretComp.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_SecretComp,
            target=self.ui.lineEdit_Effective_SecretComp,
            value=self.ui.lineEdit_Lvl_SecretComp.text()
        ))
        self.ui.lineEdit_Lvl_Condition.textEdited.connect(lambda: self.update_values(
            origin=self.ui.lineEdit_Lvl_Condition,
            target=self.ui.lineEdit_Effective_Condition,
            value=self.ui.lineEdit_Lvl_Condition.text()
        ))

        self.show()

    def open_file_dialog(self):
        file_path = wh.get_file_path(sys.platform)
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open', file_path,
                                                   'Autosave (autosave_s.json);;JSON Files (*.json);;All Files (*)',
                                                   options=options)
        if file_name:
            self.ui.label_LoadedFileName.setText(wh.get_display_name(file_name))
            save_file = jh.open_savefile(file_name)
            self.append_values(save_file)

    def append_values(self, save_file):
        # Sovereigns
        self.ui.lineEdit_Lvl_Sovereigns.setText(jh.get_value(save_file, 'Level', 131137))
        self.ui.lineEdit_Effective_Sovereigns.setText(jh.get_value(save_file, 'EffectiveLevel', 131137))
        # Hearts
        self.ui.lineEdit_Lvl_Hearts.setText(jh.get_value(save_file, 'Level', 131138))
        self.ui.lineEdit_Modifier_Hearts.setText(jh.get_value(save_file, 'EffectiveLevelModifier', 131138))
        self.ui.lineEdit_Effective_Hearts.setText(jh.get_value(save_file, 'EffectiveLevel', 131138))
        # Iron
        self.ui.lineEdit_Lvl_Iron.setText(jh.get_value(save_file, 'Level', 131139))
        self.ui.lineEdit_Modifier_Iron.setText(jh.get_value(save_file, 'EffectiveLevelModifier', 131139))
        self.ui.lineEdit_Effective_Iron.setText(jh.get_value(save_file, 'EffectiveLevel', 131139))
        # Veils
        self.ui.lineEdit_Lvl_Veils.setText(jh.get_value(save_file, 'Level', 131140))
        self.ui.lineEdit_Modifier_Veils.setText(jh.get_value(save_file, 'EffectiveLevelModifier', 131140))
        self.ui.lineEdit_Effective_Veils.setText(jh.get_value(save_file, 'EffectiveLevel', 131140))
        # Mirrors
        self.ui.lineEdit_Lvl_Mirrors.setText(jh.get_value(save_file, 'Level', 131141))
        self.ui.lineEdit_Modifier_Mirrors.setText(jh.get_value(save_file, 'EffectiveLevelModifier', 131141))
        self.ui.lineEdit_Effective_Mirrors.setText(jh.get_value(save_file, 'EffectiveLevel', 131141))
        # Condition
        self.ui.lineEdit_Lvl_Condition.setText(jh.get_value(save_file, 'Level', 131221))
        self.ui.lineEdit_Effective_Condition.setText(jh.get_value(save_file, 'EffectiveLevel', 131221))
        # Terror
        self.ui.lineEdit_Lvl_Terror.setText(jh.get_value(save_file, 'Level', 131232))
        self.ui.lineEdit_Effective_Terror.setText(jh.get_value(save_file, 'EffectiveLevel', 131232))
        # Character Level
        self.ui.lineEdit_Lvl_CharLvl.setText(jh.get_value(save_file, 'Level', 131233))
        self.ui.lineEdit_Effective_CharLvl.setText(jh.get_value(save_file, 'EffectiveLevel', 131233))
        # Experience
        self.ui.lineEdit_Lvl_Exp.setText(jh.get_value(save_file, 'Level', 131234))
        self.ui.lineEdit_Effective_Exp.setText(jh.get_value(save_file, 'EffectiveLevel', 131234))
        # Crew
        self.ui.lineEdit_Lvl_Crew.setText(jh.get_value(save_file, 'Level', 131235))
        self.ui.lineEdit_Effective_Crew.setText(jh.get_value(save_file, 'EffectiveLevel', 131235))
        # Hull
        self.ui.lineEdit_Lvl_Hull.setText(jh.get_value(save_file, 'Level', 131237))
        self.ui.lineEdit_Modifier_Hull.setText(jh.get_value(save_file, 'EffectiveLevelModifier', 131237))
        self.ui.lineEdit_Effective_Hull.setText(jh.get_value(save_file, 'EffectiveLevel', 131237))
        # Date
        self.ui.lineEdit_Lvl_Date.setText(jh.get_value(save_file, 'Level', 132055))
        self.ui.lineEdit_Effective_Date.setText(jh.get_value(save_file, 'EffectiveLevel', 132055))
        # Hold
        self.ui.lineEdit_Lvl_Hold.setText(jh.get_value(save_file, 'Level', 132788))
        self.ui.lineEdit_Modifier_Hold.setText(jh.get_value(save_file, 'EffectiveLevelModifier', 132788))
        self.ui.lineEdit_Effective_Hold.setText(jh.get_value(save_file, 'EffectiveLevel', 132788))
        # Character Points
        self.ui.lineEdit_Lvl_CharPts.setText(jh.get_value(save_file, 'Level', 132996))
        self.ui.lineEdit_Effective_CharPts.setText(jh.get_value(save_file, 'EffectiveLevel', 132996))
        # Secret Compartments
        self.ui.lineEdit_Lvl_SecretComp.setText(jh.get_value(save_file, 'Level', 139041))
        self.ui.lineEdit_Modifier_SecretComp.setText(jh.get_value(save_file, 'EffectiveLevelModifier', 139041))
        self.ui.lineEdit_Effective_SecretComp.setText(jh.get_value(save_file, 'EffectiveLevel', 139041))

    def update_values(self, origin, target, value, value2='0'):
        global ERROR
        try:
            val1 = int(value) if value2 != '' else 0
            val2 = int(value2) if value2 != '' else 0
            target.setText(str(val1 + val2))
            origin.setStyleSheet('color: rgb(0,0,0)')
            target.setStyleSheet('color: rgb(0,0,0)')
            ERROR = False
        except ValueError:
            origin.setStyleSheet('color: rgb(255,0,0)')
            target.setStyleSheet('color: rgb(255,0,0)')
            ERROR = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
