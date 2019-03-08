from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog
from Windows.main_window import Ui_MainWindow
from Windows.about_window import Ui_AboutDialog
from Data.globals import *
import sys
import window_helper as wh
import json_handler as jh


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Button Events
        self.ui.pushButton_Open.clicked.connect(self.open_file_dialog)
        self.ui.pushButton_Save.clicked.connect(self.save_file_dialog)
        self.ui.pushButton_About.clicked.connect(self.open_about_window)

        # Stats/Line Edit Events
        self.ui.lineEdit_Lvl_Sovereigns.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_Sovereigns,
            effective_level=self.ui.lineEdit_Effective_Sovereigns,
            selection=self.ui.lineEdit_Lvl_Sovereigns,
            val_id=131137
        ))
        self.ui.lineEdit_Lvl_Terror.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_Terror,
            effective_level=self.ui.lineEdit_Effective_Terror,
            selection=self.ui.lineEdit_Lvl_Terror,
            val_id=131232
        ))
        self.ui.lineEdit_Lvl_Hull.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_Hull,
            effective_level=self.ui.lineEdit_Effective_Hull,
            selection=self.ui.lineEdit_Lvl_Hull,
            modifier=self.ui.lineEdit_Modifier_Hull,
            val_id=131237
        ))
        self.ui.lineEdit_Modifier_Hull.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Modifier_Hull,
            effective_level=self.ui.lineEdit_Effective_Hull,
            selection=self.ui.lineEdit_Modifier_Hull,
            modifier=self.ui.lineEdit_Lvl_Hull,
            val_id=131237
        ))
        self.ui.lineEdit_Lvl_Crew.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_Crew,
            effective_level=self.ui.lineEdit_Effective_Crew,
            selection=self.ui.lineEdit_Lvl_Crew,
            val_id=131235
        ))
        self.ui.lineEdit_Lvl_Date.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_Date,
            effective_level=self.ui.lineEdit_Effective_Date,
            selection=self.ui.lineEdit_Lvl_Date,
            val_id=132055
        ))
        self.ui.lineEdit_Lvl_Hold.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_Hold,
            effective_level=self.ui.lineEdit_Effective_Hold,
            selection=self.ui.lineEdit_Lvl_Hold,
            val_id=132788,
            modifier=self.ui.lineEdit_Modifier_Hold
        ))
        self.ui.lineEdit_Modifier_Hold.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Modifier_Hold,
            effective_level=self.ui.lineEdit_Effective_Hold,
            selection=self.ui.lineEdit_Modifier_Hold,
            val_id=132788,
            modifier=self.ui.lineEdit_Lvl_Hold
        ))
        self.ui.lineEdit_Lvl_Hearts.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_Hearts,
            effective_level=self.ui.lineEdit_Effective_Hearts,
            selection=self.ui.lineEdit_Lvl_Hearts,
            val_id=131138,
            modifier=self.ui.lineEdit_Modifier_Hearts
        ))
        self.ui.lineEdit_Modifier_Hearts.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Modifier_Hearts,
            effective_level=self.ui.lineEdit_Effective_Hearts,
            selection=self.ui.lineEdit_Modifier_Hearts,
            val_id=131138,
            modifier=self.ui.lineEdit_Lvl_Hearts
        ))
        self.ui.lineEdit_Lvl_Veils.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_Veils,
            effective_level=self.ui.lineEdit_Effective_Veils,
            selection=self.ui.lineEdit_Lvl_Veils,
            val_id=131140,
            modifier=self.ui.lineEdit_Modifier_Veils
        ))
        self.ui.lineEdit_Modifier_Veils.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Modifier_Veils,
            effective_level=self.ui.lineEdit_Effective_Veils,
            selection=self.ui.lineEdit_Modifier_Veils,
            val_id=131140,
            modifier=self.ui.lineEdit_Lvl_Veils
        ))
        self.ui.lineEdit_Lvl_Iron.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_Iron,
            effective_level=self.ui.lineEdit_Effective_Iron,
            selection=self.ui.lineEdit_Lvl_Iron,
            val_id=131139,
            modifier=self.ui.lineEdit_Modifier_Iron
        ))
        self.ui.lineEdit_Modifier_Iron.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Modifier_Iron,
            effective_level=self.ui.lineEdit_Effective_Iron,
            selection=self.ui.lineEdit_Modifier_Iron,
            val_id=131139,
            modifier=self.ui.lineEdit_Lvl_Iron
        ))
        self.ui.lineEdit_Lvl_Mirrors.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_Mirrors,
            effective_level=self.ui.lineEdit_Effective_Mirrors,
            selection=self.ui.lineEdit_Lvl_Mirrors,
            val_id=131141,
            modifier=self.ui.lineEdit_Modifier_Mirrors
        ))
        self.ui.lineEdit_Modifier_Mirrors.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Modifier_Mirrors,
            effective_level=self.ui.lineEdit_Effective_Mirrors,
            selection=self.ui.lineEdit_Modifier_Mirrors,
            val_id=131141,
            modifier=self.ui.lineEdit_Lvl_Mirrors
        ))
        self.ui.lineEdit_Lvl_CharLvl.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_CharLvl,
            effective_level=self.ui.lineEdit_Effective_CharLvl,
            val_id=131233,
            selection=self.ui.lineEdit_Lvl_CharLvl
        ))
        self.ui.lineEdit_Lvl_CharPts.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_CharPts,
            effective_level=self.ui.lineEdit_Effective_CharPts,
            val_id=132996,
            selection=self.ui.lineEdit_Lvl_CharPts
        ))
        self.ui.lineEdit_Lvl_Exp.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_Exp,
            effective_level=self.ui.lineEdit_Effective_Exp,
            val_id=131234,
            selection=self.ui.lineEdit_Lvl_Exp
        ))
        self.ui.lineEdit_Lvl_SecretComp.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_SecretComp,
            effective_level=self.ui.lineEdit_Effective_SecretComp,
            selection=self.ui.lineEdit_Lvl_SecretComp,
            val_id=139041,
            modifier=self.ui.lineEdit_Modifier_SecretComp
        ))
        self.ui.lineEdit_Modifier_SecretComp.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Modifier_SecretComp,
            effective_level=self.ui.lineEdit_Effective_SecretComp,
            selection=self.ui.lineEdit_Modifier_SecretComp,
            val_id=139041,
            modifier=self.ui.lineEdit_Lvl_SecretComp
        ))
        self.ui.lineEdit_Lvl_Condition.textEdited.connect(lambda: self.update_stats(
            level=self.ui.lineEdit_Lvl_Condition,
            effective_level=self.ui.lineEdit_Effective_Condition,
            val_id=131221,
            selection=self.ui.lineEdit_Lvl_Condition
        ))

        # Map/Combo Box Events
        self.ui.comboBox_Region.currentTextChanged.connect(lambda: self.generate_port_list(
            self.ui.comboBox_Region
        ))
        self.ui.comboBox_Port.currentTextChanged.connect(lambda: self.update_current_port(
            self.ui.comboBox_Port.currentText()
        ))
        self.ui.checkBox_FoW_Reach.stateChanged.connect(lambda: self.update_fow_state(
            self.ui.checkBox_FoW_Reach.checkState(),
            'The Reach'
        ))
        self.ui.checkBox_FoW_Albion.stateChanged.connect(lambda: self.update_fow_state(
            self.ui.checkBox_FoW_Albion.checkState(),
            'Albion'
        ))
        self.ui.checkBox_FoW_Eleutheria.stateChanged.connect(lambda: self.update_fow_state(
            self.ui.checkBox_FoW_Eleutheria.checkState(),
            'Eleutheria'
        ))
        self.ui.checkBox_FoW_BlueKingdom.stateChanged.connect(lambda: self.update_fow_state(
            self.ui.checkBox_FoW_BlueKingdom.checkState(),
            'The Blue Kingdom'
        ))

        # Possession Events
        #Academe
        self.ui.lineEdit_Poss_Academe_Specimen.textChanged.connect(lambda: self.update_possessions(
            self.ui.lineEdit_Poss_Academe_Specimen,
            131123
        ))

        self.show()

    def open_file_dialog(self):
        global SAVEFILE_PATH, SAVE_FILE, INITIALIZATION, CACHED_SAVEFILE
        INITIALIZATION = True
        SAVEFILE_PATH = wh.get_file_path(sys.platform)
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            'Open',
            SAVEFILE_PATH,
            'Autosave (autosave_s.json);;JSON Files (*.json);;All Files (*)',
            options=options
        )

        if file_name:
            self.ui.label_LoadedFileName.setText(wh.get_display_name(file_name))
            SAVE_FILE = jh.open_json_file(file_name)
            CACHED_SAVEFILE = SAVE_FILE
            self.initialize_values(SAVE_FILE)
            INITIALIZATION = False

    def save_file_dialog(self):
        if not ERRORS:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(
                self,
                'Save',
                SAVEFILE_PATH,
                'Autosave (autosave_s.json);;JSON Files (*.json);;All Files (*)',
                options=options
            )
            if file_name:
                jh.save_json_file(file_name, SAVE_FILE)

    def open_about_window(self):
        dialog = AboutWindow()
        dialog.exec_()

    def initialize_values(self, save_file):
        self.append_stats(save_file)
        self.append_map(save_file)
        self.append_possessions(save_file)

    def append_stats(self, save_file):
        # Sovereigns
        self.ui.lineEdit_Lvl_Sovereigns.setText(jh.get_quality_value(save_file, 131137, 'Level'))
        self.ui.lineEdit_Effective_Sovereigns.setText(jh.get_quality_value(save_file, 131137))
        # Hearts
        self.ui.lineEdit_Lvl_Hearts.setText(jh.get_quality_value(save_file, 131138, 'Level'))
        self.ui.lineEdit_Modifier_Hearts.setText(jh.get_quality_value(save_file, 131138, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_Hearts.setText(jh.get_quality_value(save_file, 131138))
        # Iron
        self.ui.lineEdit_Lvl_Iron.setText(jh.get_quality_value(save_file, 131139, 'Level'))
        self.ui.lineEdit_Modifier_Iron.setText(jh.get_quality_value(save_file, 131139, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_Iron.setText(jh.get_quality_value(save_file, 131139))
        # Veils
        self.ui.lineEdit_Lvl_Veils.setText(jh.get_quality_value(save_file, 131140, 'Level'))
        self.ui.lineEdit_Modifier_Veils.setText(jh.get_quality_value(save_file, 131140, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_Veils.setText(jh.get_quality_value(save_file, 131140))
        # Mirrors
        self.ui.lineEdit_Lvl_Mirrors.setText(jh.get_quality_value(save_file, 131141, 'Level'))
        self.ui.lineEdit_Modifier_Mirrors.setText(jh.get_quality_value(save_file, 131141, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_Mirrors.setText(jh.get_quality_value(save_file, 131141))
        # Condition
        self.ui.lineEdit_Lvl_Condition.setText(jh.get_quality_value(save_file, 131221, 'Level'))
        self.ui.lineEdit_Effective_Condition.setText(jh.get_quality_value(save_file, 131221))
        # Terror
        self.ui.lineEdit_Lvl_Terror.setText(jh.get_quality_value(save_file, 131232, 'Level'))
        self.ui.lineEdit_Effective_Terror.setText(jh.get_quality_value(save_file, 131232))
        # Character Level
        self.ui.lineEdit_Lvl_CharLvl.setText(jh.get_quality_value(save_file, 131233, 'Level'))
        self.ui.lineEdit_Effective_CharLvl.setText(jh.get_quality_value(save_file, 131233))
        # Experience
        self.ui.lineEdit_Lvl_Exp.setText(jh.get_quality_value(save_file, 131234, 'Level'))
        self.ui.lineEdit_Effective_Exp.setText(jh.get_quality_value(save_file, 131234))
        # Crew
        self.ui.lineEdit_Lvl_Crew.setText(jh.get_quality_value(save_file, 131235, 'Level'))
        self.ui.lineEdit_Effective_Crew.setText(jh.get_quality_value(save_file, 131235))
        # Hull
        self.ui.lineEdit_Lvl_Hull.setText(jh.get_quality_value(save_file, 131237, 'Level'))
        self.ui.lineEdit_Modifier_Hull.setText(jh.get_quality_value(save_file, 131237, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_Hull.setText(jh.get_quality_value(save_file, 131237))
        # Date
        self.ui.lineEdit_Lvl_Date.setText(jh.get_quality_value(save_file, 132055, 'Level'))
        self.ui.lineEdit_Effective_Date.setText(jh.get_quality_value(save_file, 132055))
        # Hold
        self.ui.lineEdit_Lvl_Hold.setText(jh.get_quality_value(save_file, 132788, 'Level'))
        self.ui.lineEdit_Modifier_Hold.setText(jh.get_quality_value(save_file, 132788, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_Hold.setText(jh.get_quality_value(save_file, 132788))
        # Character Points
        self.ui.lineEdit_Lvl_CharPts.setText(jh.get_quality_value(save_file, 132996, 'Level'))
        self.ui.lineEdit_Effective_CharPts.setText(jh.get_quality_value(save_file, 132996))
        # Secret Compartments
        self.ui.lineEdit_Lvl_SecretComp.setText(jh.get_quality_value(save_file, 139041, 'Level'))
        self.ui.lineEdit_Modifier_SecretComp.setText(jh.get_quality_value(save_file, 139041, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_SecretComp.setText(jh.get_quality_value(save_file, 139041))

    def append_map(self, save_file):
        # Teleportation
        self.ui.comboBox_Region.addItems(['The Reach', 'Albion', 'Eleutheria', 'The Blue Kingdom'])
        self.ui.comboBox_Region.setCurrentText(jh.get_current_region_name(save_file))
        self.ui.comboBox_Port.setCurrentText(jh.get_current_port_name(save_file))

        # Fog of War
        self.ui.checkBox_FoW_Reach.setCheckState(jh.get_fow_state(save_file, 'The Reach'))
        self.ui.checkBox_FoW_Albion.setCheckState(jh.get_fow_state(save_file, 'Albion'))
        self.ui.checkBox_FoW_Eleutheria.setCheckState(jh.get_fow_state(save_file, 'Eleutheria'))
        self.ui.checkBox_FoW_BlueKingdom.setCheckState(jh.get_fow_state(save_file, 'The Blue Kingdom'))

    def append_possessions(self, save_file):
        # Academe
        self.ui.lineEdit_Poss_Academe_Specimen.setText(jh.get_quality_value(save_file, 131123))
        self.ui.lineEdit_Poss_Academe_Artifact.setText(jh.get_quality_value(save_file, 131124))
        self.ui.lineEdit_Poss_Academe_Experiment.setText(jh.get_quality_value(save_file, 131125))
        self.ui.lineEdit_Poss_Academe_Enigma.setText(jh.get_quality_value(save_file, 131126))
        # Bohemia
        self.ui.lineEdit_Poss_Bohemia_SkyStory.setText(jh.get_quality_value(save_file, 131115))
        self.ui.lineEdit_Poss_Bohemia_Vision.setText(jh.get_quality_value(save_file, 131116))
        self.ui.lineEdit_Poss_Bohemia_Moment.setText(jh.get_quality_value(save_file, 131117))
        self.ui.lineEdit_Poss_Bohemia_Treasure.setText(jh.get_quality_value(save_file, 131118))
        # Establishment
        self.ui.lineEdit_Poss_Estab_Gossip.setText(jh.get_quality_value(save_file, 131127))
        self.ui.lineEdit_Poss_Estab_Permit.setText(jh.get_quality_value(save_file, 131128))
        self.ui.lineEdit_Poss_Estab_Benefactor.setText(jh.get_quality_value(save_file, 131129))
        self.ui.lineEdit_Poss_Estab_Dispensation.setText(jh.get_quality_value(save_file, 131130))
        # Villainy
        self.ui.lineEdit_Poss_Villainy_Tale.setText(jh.get_quality_value(save_file, 131119))
        self.ui.lineEdit_Poss_Villainy_Secret.setText(jh.get_quality_value(save_file, 131120))
        self.ui.lineEdit_Poss_Villainy_Chart.setText(jh.get_quality_value(save_file, 131121))
        self.ui.lineEdit_Poss_Villainy_Promise.setText(jh.get_quality_value(save_file, 131122))
        # Gratitudes
        self.ui.lineEdit_Poss_Gratitudes_Windward.setText(jh.get_quality_value(save_file, 132085))
        self.ui.lineEdit_Poss_Gratitude_Tacketies.setText(jh.get_quality_value(save_file, 132124))
        self.ui.lineEdit_Poss_Gratitude_Ministry.setText(jh.get_quality_value(save_file, 135546))
        self.ui.lineEdit_Poss_Gratitude_NSL.setText(jh.get_quality_value(save_file, 135547))
        self.ui.lineEdit_Poss_Gratitude_Embassy.setText(jh.get_quality_value(save_file, 139092))
        self.ui.lineEdit_Poss_Gratitude_Society.setText(jh.get_quality_value(save_file, 135399))
        # Miscellaneous
        self.ui.lineEdit_Poss_Misc_Guests.setText(jh.get_quality_value(save_file, 139064))
        # Port Reports
        self.ui.checkBox_Poss_Reports.setCheckState(jh.get_port_reports(save_file))
        # Heirlooms
        self.ui.checkBox_Poss_Heirloom_Song.setChecked(jh.get_heirloom(save_file, 137375))
        self.ui.checkBox_Poss_Heirloom_Wealth.setChecked(jh.get_heirloom(save_file, 137376))
        self.ui.checkBox_Poss_Heirloom_Cup.setChecked(jh.get_heirloom(save_file, 139484))
        self.ui.checkBox_Poss_Heirloom_Secret.setChecked(jh.get_heirloom(save_file, 139160))
        # Reach
        self.ui.lineEdit_Poss_ReachMisc_Circus.setText(jh.get_quality_value(save_file, 137036))
        self.ui.lineEdit_Poss_ReachMisc_StovepipePlate.setText(jh.get_quality_value(save_file, 133455))
        self.ui.lineEdit_Poss_ReachMisc_Shard.setText(jh.get_quality_value(save_file, 133439))
        self.ui.lineEdit_Poss_ReachMisc_TacketyPlate.setText(jh.get_quality_value(save_file, 132976))
        # Albion
        self.ui.lineEdit_Poss_AlbionMisc_Mods.setText(jh.get_quality_value(save_file, 135357))
        self.ui.lineEdit_Poss_AlbionMisc_Invites.setText(jh.get_quality_value(save_file, 134274))
        # Eleutheria
        self.ui.lineEdit_Poss_EleuMisc_EmpyreanPlate.setText(jh.get_quality_value(save_file, 137409))
        self.ui.lineEdit_Poss_EleuMisc_DouserPlate.setText(jh.get_quality_value(save_file, 137621))
        self.ui.lineEdit_Poss_EleuMisc_Mystery.setText(jh.get_quality_value(save_file, 137370))
        self.ui.lineEdit_Poss_EleuMisc_Scrap.setText(jh.get_quality_value(save_file, 137371))
        self.ui.lineEdit_Poss_EleuMisc_Green.setText(jh.get_quality_value(save_file, 135123))
        self.ui.lineEdit_Poss_EleuMisc_Golden.setText(jh.get_quality_value(save_file, 135124))
        self.ui.lineEdit_Poss_EleuMisc_Red.setText(jh.get_quality_value(save_file, 135125))
        self.ui.lineEdit_Poss_EleuMisc_Blue.setText(jh.get_quality_value(save_file, 135126))
        self.ui.lineEdit_Poss_EleuMisc_Soft.setText(jh.get_quality_value(save_file, 135134))
        # The Blue Kingdom
        self.ui.lineEdit_Poss_TBKMisc_Indulgence.setText(jh.get_quality_value(save_file, 138080))
        self.ui.lineEdit_Poss_TBKMisc_Roses.setText(jh.get_quality_value(save_file, 138072))
        self.ui.lineEdit_Poss_TBKMisc_Salt.setText(jh.get_quality_value(save_file, 138073))
        self.ui.lineEdit_Poss_TBKMisc_Flowers.setText(jh.get_quality_value(save_file, 138074))
        self.ui.lineEdit_Poss_TBKMisc_Volumes.setText(jh.get_quality_value(save_file, 139095))
        self.ui.lineEdit_Poss_TBKMisc_Incarnadine.setText(jh.get_quality_value(save_file, 138934))
        self.ui.lineEdit_Poss_TBKMisc_Verdance.setText(jh.get_quality_value(save_file, 138935))
        self.ui.lineEdit_Poss_TBKMisc_Hourglass.setText(jh.get_quality_value(save_file, 138937))
        self.ui.lineEdit_Poss_TBKMisc_Dominion.setText(jh.get_quality_value(save_file, 138938))

    def update_stats(self, level, effective_level, selection, val_id, modifier=None):
        if not INITIALIZATION:
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
                SAVE_FILE = jh.write_stats(SAVE_FILE, val1, val2, val_id)

                ERRORS = False

            except ValueError:
                selection.setStyleSheet('color: rgb(255,0,0)')
                effective_level.setStyleSheet('color: rgb(255,0,0)')

                ERRORS = True

    def update_possessions(self, quality, val_id):
        if not INITIALIZATION:
            global ERRORS, SAVE_FILE

            value = quality.text()

            try:
                value = int(value)
                quality.setStyleSheet('color: rgb(0,0,0)')

                SAVE_FILE = jh.write_possessions(SAVE_FILE, value, val_id)

                ERRORS = False
            except ValueError:
                quality.setStyleSheet('color: rgb(255,0,0)')
                ERRORS = True

    def update_current_port(self, port):
        if not INITIALIZATION:

            global SAVE_FILE
            SAVE_FILE = jh.write_current_port(SAVE_FILE, port, CACHED_SAVEFILE)

    def update_fow_state(self, state, region):
        if not INITIALIZATION:

            global SAVE_FILE
            SAVE_FILE = jh.write_fow_values(SAVE_FILE, state, region)

    def generate_port_list(self, region):
        region = region.currentText()
        self.ui.comboBox_Port.clear()
        self.ui.comboBox_Port.addItems(jh.get_port_list(SAVE_FILE, region))

class AboutWindow(QDialog, Ui_AboutDialog):
    def __init__(self):
        super(QDialog, self).__init__()

        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

        self.ui.label_Version.setText('Sunless Skies Save Editor ' + VERSION)
        self.ui.label_About_License.setOpenExternalLinks(True)

        self.ui.pushButton_About_Close.clicked.connect(self.close)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
