from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from window_design import Ui_MainWindow
import sys
import window_helper as wh
import json_handler as jh


ERRORS = False
FILE_PATH = ''
SAVE_FILE = {}


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Button Events
        self.ui.pushButton_Open.clicked.connect(self.open_file_dialog)
        self.ui.pushButton_Save.clicked.connect(self.save_file)

        # Line Edit Events
        self.ui.lineEdit_Lvl_Sovereigns.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_Sovereigns,
            effective_level=self.ui.lineEdit_Effective_Sovereigns,
            selection=self.ui.lineEdit_Lvl_Sovereigns,
            val_id=131137
        ))
        self.ui.lineEdit_Lvl_Terror.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_Terror,
            effective_level=self.ui.lineEdit_Effective_Terror,
            selection=self.ui.lineEdit_Lvl_Terror,
            val_id=131232
        ))
        self.ui.lineEdit_Lvl_Hull.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_Hull,
            effective_level=self.ui.lineEdit_Effective_Hull,
            selection=self.ui.lineEdit_Lvl_Hull,
            modifier=self.ui.lineEdit_Modifier_Hull,
            val_id=131237
        ))
        self.ui.lineEdit_Modifier_Hull.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Modifier_Hull,
            effective_level=self.ui.lineEdit_Effective_Hull,
            selection=self.ui.lineEdit_Modifier_Hull,
            modifier=self.ui.lineEdit_Lvl_Hull,
            val_id=131237
        ))
        self.ui.lineEdit_Lvl_Crew.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_Crew,
            effective_level=self.ui.lineEdit_Effective_Crew,
            selection=self.ui.lineEdit_Lvl_Crew,
            val_id=131235
        ))
        self.ui.lineEdit_Lvl_Date.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_Date,
            effective_level=self.ui.lineEdit_Effective_Date,
            selection=self.ui.lineEdit_Lvl_Date,
            val_id=132055
        ))
        self.ui.lineEdit_Lvl_Hold.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_Hold,
            effective_level=self.ui.lineEdit_Effective_Hold,
            selection=self.ui.lineEdit_Lvl_Hold,
            val_id=132788,
            modifier=self.ui.lineEdit_Modifier_Hold
        ))
        self.ui.lineEdit_Modifier_Hold.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Modifier_Hold,
            effective_level=self.ui.lineEdit_Effective_Hold,
            selection=self.ui.lineEdit_Modifier_Hold,
            val_id=132788,
            modifier=self.ui.lineEdit_Lvl_Hold
        ))
        self.ui.lineEdit_Lvl_Hearts.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_Hearts,
            effective_level=self.ui.lineEdit_Effective_Hearts,
            selection=self.ui.lineEdit_Lvl_Hearts,
            val_id=131138,
            modifier=self.ui.lineEdit_Modifier_Hearts
        ))
        self.ui.lineEdit_Modifier_Hearts.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Modifier_Hearts,
            effective_level=self.ui.lineEdit_Effective_Hearts,
            selection=self.ui.lineEdit_Modifier_Hearts,
            val_id=131138,
            modifier=self.ui.lineEdit_Lvl_Hearts
        ))
        self.ui.lineEdit_Lvl_Veils.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_Veils,
            effective_level=self.ui.lineEdit_Effective_Veils,
            selection=self.ui.lineEdit_Lvl_Veils,
            val_id=131140,
            modifier=self.ui.lineEdit_Modifier_Veils
        ))
        self.ui.lineEdit_Modifier_Veils.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Modifier_Veils,
            effective_level=self.ui.lineEdit_Effective_Veils,
            selection=self.ui.lineEdit_Modifier_Veils,
            val_id=131140,
            modifier=self.ui.lineEdit_Lvl_Veils
        ))
        self.ui.lineEdit_Lvl_Iron.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_Iron,
            effective_level=self.ui.lineEdit_Effective_Iron,
            selection=self.ui.lineEdit_Lvl_Iron,
            val_id=131139,
            modifier=self.ui.lineEdit_Modifier_Iron
        ))
        self.ui.lineEdit_Modifier_Iron.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Modifier_Iron,
            effective_level=self.ui.lineEdit_Effective_Iron,
            selection=self.ui.lineEdit_Modifier_Iron,
            val_id=131139,
            modifier=self.ui.lineEdit_Lvl_Iron
        ))
        self.ui.lineEdit_Lvl_Mirrors.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_Mirrors,
            effective_level=self.ui.lineEdit_Effective_Mirrors,
            selection=self.ui.lineEdit_Lvl_Mirrors,
            val_id=131141,
            modifier=self.ui.lineEdit_Modifier_Mirrors
        ))
        self.ui.lineEdit_Modifier_Mirrors.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Modifier_Mirrors,
            effective_level=self.ui.lineEdit_Effective_Mirrors,
            selection=self.ui.lineEdit_Modifier_Mirrors,
            val_id=131141,
            modifier=self.ui.lineEdit_Lvl_Mirrors
        ))
        self.ui.lineEdit_Lvl_CharLvl.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_CharLvl,
            effective_level=self.ui.lineEdit_Effective_CharLvl,
            val_id=131233,
            selection=self.ui.lineEdit_Lvl_CharLvl
        ))
        self.ui.lineEdit_Lvl_CharPts.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_CharPts,
            effective_level=self.ui.lineEdit_Effective_CharPts,
            val_id=132996,
            selection=self.ui.lineEdit_Lvl_CharPts
        ))
        self.ui.lineEdit_Lvl_Exp.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_Exp,
            effective_level=self.ui.lineEdit_Effective_Exp,
            val_id=131234,
            selection=self.ui.lineEdit_Lvl_Exp
        ))
        self.ui.lineEdit_Lvl_SecretComp.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_SecretComp,
            effective_level=self.ui.lineEdit_Effective_SecretComp,
            selection=self.ui.lineEdit_Lvl_SecretComp,
            val_id=139041,
            modifier=self.ui.lineEdit_Modifier_SecretComp
        ))
        self.ui.lineEdit_Modifier_SecretComp.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Modifier_SecretComp,
            effective_level=self.ui.lineEdit_Effective_SecretComp,
            selection=self.ui.lineEdit_Modifier_SecretComp,
            val_id=139041,
            modifier=self.ui.lineEdit_Lvl_SecretComp
        ))
        self.ui.lineEdit_Lvl_Condition.textEdited.connect(lambda: self.update_values(
            level=self.ui.lineEdit_Lvl_Condition,
            effective_level=self.ui.lineEdit_Effective_Condition,
            val_id=131221,
            selection=self.ui.lineEdit_Lvl_Condition
        ))

        self.show()

    def open_file_dialog(self):
        global FILE_PATH, SAVE_FILE
        path = wh.get_file_path(sys.platform)
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            'Open',
            path,
            'Autosave (autosave_s.json);;JSON Files (*.json);;All Files (*)',
            options=options
        )
        if file_name:
            FILE_PATH = file_name
            self.ui.label_LoadedFileName.setText(wh.get_display_name(file_name))
            SAVE_FILE = jh.open_savefile(file_name)
            self.append_values(SAVE_FILE)

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

    def update_values(self, level, effective_level, selection, val_id, modifier=None):
        global ERRORS, SAVE_FILE

        val_level = level.text()
        val_modifier = modifier.text() if modifier else '0'

        try:
            val1 = int(val_level)
            val2 = int(val_modifier)

            level.setStyleSheet('color: rgb(0,0,0)')
            effective_level.setStyleSheet('color: rgb(0,0,0)')
            if modifier:
                modifier.setStyleSheet('color: rgb(0,0,0)')

            effective_level.setText(str(val1 + val2))
            SAVE_FILE = jh.write_values(SAVE_FILE, val1, val2, val_id)

            ERRORS = False

        except ValueError:
            selection.setStyleSheet('color: rgb(255,0,0)')
            effective_level.setStyleSheet('color: rgb(255,0,0)')

            ERRORS = True

    def save_file(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
