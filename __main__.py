from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog, QLineEdit, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
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

        # Possessions Tab spacing for macOS
        if sys.platform == 'darwin':
            self.ui.toolBox.layout().setSpacing(0)

        # Table formatting
        header = self.ui.tableWidget_Bank.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setDefaultAlignment(Qt.AlignLeft)

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
        self.ui.comboBox_Region.currentTextChanged.connect(lambda: self.generate_port_list())
        self.ui.comboBox_Port.currentTextChanged.connect(lambda: self.update_current_port())
        self.ui.checkBox_FoW_Reach.stateChanged.connect(lambda: self.update_fow_state('The Reach'))
        self.ui.checkBox_FoW_Albion.stateChanged.connect(lambda: self.update_fow_state('Albion'))
        self.ui.checkBox_FoW_Eleutheria.stateChanged.connect(lambda: self.update_fow_state('Eleutheria'))
        self.ui.checkBox_FoW_BlueKingdom.stateChanged.connect(lambda: self.update_fow_state('The Blue Kingdom'))

        # Possession Events
        # Academe
        self.ui.lineEdit_Poss_Academe_Specimen.textChanged.connect(lambda: self.update_possessions(131123))
        self.ui.lineEdit_Poss_Academe_Artifact.textChanged.connect(lambda: self.update_possessions(131124))
        self.ui.lineEdit_Poss_Academe_Experiment.textChanged.connect(lambda: self.update_possessions(131125))
        self.ui.lineEdit_Poss_Academe_Enigma.textChanged.connect(lambda: self.update_possessions(131126))
        # Bohemia
        self.ui.lineEdit_Poss_Bohemia_SkyStory.textChanged.connect(lambda: self.update_possessions(131115))
        self.ui.lineEdit_Poss_Bohemia_Vision.textChanged.connect(lambda: self.update_possessions(131116))
        self.ui.lineEdit_Poss_Bohemia_Moment.textChanged.connect(lambda: self.update_possessions(131117))
        self.ui.lineEdit_Poss_Bohemia_Treasure.textChanged.connect(lambda: self.update_possessions(131118))
        # Establishment
        self.ui.lineEdit_Poss_Estab_Gossip.textChanged.connect(lambda: self.update_possessions(131127))
        self.ui.lineEdit_Poss_Estab_Permit.textChanged.connect(lambda: self.update_possessions(131128))
        self.ui.lineEdit_Poss_Estab_Benefactor.textChanged.connect(lambda: self.update_possessions(131129))
        self.ui.lineEdit_Poss_Estab_Dispensation.textChanged.connect(lambda: self.update_possessions(131130))
        # Villainy
        self.ui.lineEdit_Poss_Villainy_Tale.textChanged.connect(lambda: self.update_possessions(131119))
        self.ui.lineEdit_Poss_Villainy_Secret.textChanged.connect(lambda: self.update_possessions(131120))
        self.ui.lineEdit_Poss_Villainy_Chart.textChanged.connect(lambda: self.update_possessions(131121))
        self.ui.lineEdit_Poss_Villainy_Promise.textChanged.connect(lambda: self.update_possessions(131122))
        # Gratitudes
        self.ui.lineEdit_Poss_Gratitudes_Windward.textChanged.connect(lambda: self.update_possessions(132085))
        self.ui.lineEdit_Poss_Gratitude_Tacketies.textChanged.connect(lambda: self.update_possessions(132124))
        self.ui.lineEdit_Poss_Gratitude_Ministry.textChanged.connect(lambda: self.update_possessions(135546))
        self.ui.lineEdit_Poss_Gratitude_NSL.textChanged.connect(lambda: self.update_possessions(135547))
        self.ui.lineEdit_Poss_Gratitude_Embassy.textChanged.connect(lambda: self.update_possessions(139092))
        self.ui.lineEdit_Poss_Gratitude_Society.textChanged.connect(lambda: self.update_possessions(135399))
        # Miscellaneous
        self.ui.lineEdit_Poss_Misc_Guests.textChanged.connect(lambda: self.update_possessions(139064))
        # Port Reports
        self.ui.checkBox_Poss_Reports_Reach.stateChanged.connect(lambda: self.update_port_reports('The Reach'))
        self.ui.checkBox_Poss_Reports_Albion.stateChanged.connect(lambda: self.update_port_reports('Albion'))
        self.ui.checkBox_Poss_Reports_Eleutheria.stateChanged.connect(lambda: self.update_port_reports('Eleutheria'))
        self.ui.checkBox_Poss_Reports_TBK.stateChanged.connect(lambda: self.update_port_reports('The Blue Kingdom'))
        # Heirlooms
        self.ui.checkBox_Poss_Heirloom_Song.stateChanged.connect(lambda: self.update_heirlooms(137375))
        self.ui.checkBox_Poss_Heirloom_Wealth.stateChanged.connect(lambda: self.update_heirlooms(137376))
        self.ui.checkBox_Poss_Heirloom_Cup.stateChanged.connect(lambda: self.update_heirlooms(139484))
        self.ui.checkBox_Poss_Heirloom_Secret.stateChanged.connect(lambda: self.update_heirlooms(139160))
        # Reach
        self.ui.lineEdit_Poss_ReachMisc_Circus.textChanged.connect(lambda: self.update_possessions(137036))
        self.ui.lineEdit_Poss_ReachMisc_StovepipePlate.textChanged.connect(lambda: self.update_possessions(133455))
        self.ui.lineEdit_Poss_ReachMisc_Shard.textChanged.connect(lambda: self.update_possessions(133439))
        self.ui.lineEdit_Poss_ReachMisc_TacketyPlate.textChanged.connect(lambda: self.update_possessions(132976))
        # Albion
        self.ui.lineEdit_Poss_AlbionMisc_Mods.textChanged.connect(lambda: self.update_possessions(135357))
        self.ui.lineEdit_Poss_AlbionMisc_Invites.textChanged.connect(lambda: self.update_possessions(134274))
        # Eleutheria
        self.ui.lineEdit_Poss_EleuMisc_EmpyreanPlate.textChanged.connect(lambda: self.update_possessions(137409))
        self.ui.lineEdit_Poss_EleuMisc_DouserPlate.textChanged.connect(lambda: self.update_possessions(137621))
        self.ui.lineEdit_Poss_EleuMisc_Mystery.textChanged.connect(lambda: self.update_possessions(137370))
        self.ui.lineEdit_Poss_EleuMisc_Scrap.textChanged.connect(lambda: self.update_possessions(137371))
        self.ui.lineEdit_Poss_EleuMisc_Green.textChanged.connect(lambda: self.update_possessions(135123))
        self.ui.lineEdit_Poss_EleuMisc_Golden.textChanged.connect(lambda: self.update_possessions(135124))
        self.ui.lineEdit_Poss_EleuMisc_Red.textChanged.connect(lambda: self.update_possessions(135125))
        self.ui.lineEdit_Poss_EleuMisc_Blue.textChanged.connect(lambda: self.update_possessions(135126))
        self.ui.lineEdit_Poss_EleuMisc_Soft.textChanged.connect(lambda: self.update_possessions(135134))
        # The Blue Kingdom
        self.ui.lineEdit_Poss_TBKMisc_Indulgence.textChanged.connect(lambda: self.update_possessions(138080))
        self.ui.lineEdit_Poss_TBKMisc_Roses.textChanged.connect(lambda: self.update_possessions(138072))
        self.ui.lineEdit_Poss_TBKMisc_Salt.textChanged.connect(lambda: self.update_possessions(138073))
        self.ui.lineEdit_Poss_TBKMisc_Flowers.textChanged.connect(lambda: self.update_possessions(138074))
        self.ui.lineEdit_Poss_TBKMisc_Volumes.textChanged.connect(lambda: self.update_possessions(139095))
        self.ui.lineEdit_Poss_TBKMisc_Incarnadine.textChanged.connect(lambda: self.update_possessions(138934))
        self.ui.lineEdit_Poss_TBKMisc_Verdance.textChanged.connect(lambda: self.update_possessions(138935))
        self.ui.lineEdit_Poss_TBKMisc_Hourglass.textChanged.connect(lambda: self.update_possessions(138937))
        self.ui.lineEdit_Poss_TBKMisc_Dominion.textChanged.connect(lambda: self.update_possessions(138938))

        self.show()

    def open_file_dialog(self):
        global SAVEFILE_PATH, SAVE_FILE, INITIALIZATION, CACHED_SAVEFILE, ERRORS
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
            # reset stylesheet
            tuple(map(self.reset_stylesheet, self.findChildren(QLineEdit)))

            self.ui.label_LoadedFileName.setText(wh.get_display_name(file_name))
            SAVE_FILE = jh.open_json_file(file_name)
            CACHED_SAVEFILE = SAVE_FILE
            self.initialize_values(SAVE_FILE)
            ERRORS = False
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
        self.append_bank(save_file)

    def reset_stylesheet(self, element):
        element.setProperty('valid', True)
        element.setStyle(element.style())

    def append_stats(self, save_file):
        # Sovereigns
        self.ui.lineEdit_Lvl_Sovereigns.setText(jh.get_quality_value(save_file, 131137))
        self.ui.lineEdit_Effective_Sovereigns.setText(jh.get_quality_value(save_file, 131137, 'EffectiveLevel'))
        # Hearts
        self.ui.lineEdit_Lvl_Hearts.setText(jh.get_quality_value(save_file, 131138))
        self.ui.lineEdit_Modifier_Hearts.setText(jh.get_quality_value(save_file, 131138, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_Hearts.setText(jh.get_quality_value(save_file, 131138, 'EffectiveLevel'))
        # Iron
        self.ui.lineEdit_Lvl_Iron.setText(jh.get_quality_value(save_file, 131139))
        self.ui.lineEdit_Modifier_Iron.setText(jh.get_quality_value(save_file, 131139, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_Iron.setText(jh.get_quality_value(save_file, 131139, 'EffectiveLevel'))
        # Veils
        self.ui.lineEdit_Lvl_Veils.setText(jh.get_quality_value(save_file, 131140))
        self.ui.lineEdit_Modifier_Veils.setText(jh.get_quality_value(save_file, 131140, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_Veils.setText(jh.get_quality_value(save_file, 131140, 'EffectiveLevel'))
        # Mirrors
        self.ui.lineEdit_Lvl_Mirrors.setText(jh.get_quality_value(save_file, 131141))
        self.ui.lineEdit_Modifier_Mirrors.setText(jh.get_quality_value(save_file, 131141, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_Mirrors.setText(jh.get_quality_value(save_file, 131141, 'EffectiveLevel'))
        # Condition
        self.ui.lineEdit_Lvl_Condition.setText(jh.get_quality_value(save_file, 131221))
        self.ui.lineEdit_Effective_Condition.setText(jh.get_quality_value(save_file, 131221, 'EffectiveLevel'))
        # Terror
        self.ui.lineEdit_Lvl_Terror.setText(jh.get_quality_value(save_file, 131232))
        self.ui.lineEdit_Effective_Terror.setText(jh.get_quality_value(save_file, 131232, 'EffectiveLevel'))
        # Character Level
        self.ui.lineEdit_Lvl_CharLvl.setText(jh.get_quality_value(save_file, 131233))
        self.ui.lineEdit_Effective_CharLvl.setText(jh.get_quality_value(save_file, 131233, 'EffectiveLevel'))
        # Experience
        self.ui.lineEdit_Lvl_Exp.setText(jh.get_quality_value(save_file, 131234))
        self.ui.lineEdit_Effective_Exp.setText(jh.get_quality_value(save_file, 131234, 'EffectiveLevel'))
        # Crew
        self.ui.lineEdit_Lvl_Crew.setText(jh.get_quality_value(save_file, 131235))
        self.ui.lineEdit_Effective_Crew.setText(jh.get_quality_value(save_file, 131235, 'EffectiveLevel'))
        # Hull
        self.ui.lineEdit_Lvl_Hull.setText(jh.get_quality_value(save_file, 131237))
        self.ui.lineEdit_Modifier_Hull.setText(jh.get_quality_value(save_file, 131237, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_Hull.setText(jh.get_quality_value(save_file, 131237, 'EffectiveLevel'))
        # Date
        self.ui.lineEdit_Lvl_Date.setText(jh.get_quality_value(save_file, 132055))
        self.ui.lineEdit_Effective_Date.setText(jh.get_quality_value(save_file, 132055, 'EffectiveLevel'))
        # Hold
        self.ui.lineEdit_Lvl_Hold.setText(jh.get_quality_value(save_file, 132788))
        self.ui.lineEdit_Modifier_Hold.setText(jh.get_quality_value(save_file, 132788, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_Hold.setText(jh.get_quality_value(save_file, 132788, 'EffectiveLevel'))
        # Character Points
        self.ui.lineEdit_Lvl_CharPts.setText(jh.get_quality_value(save_file, 132996))
        self.ui.lineEdit_Effective_CharPts.setText(jh.get_quality_value(save_file, 132996, 'EffectiveLevel'))
        # Secret Compartments
        self.ui.lineEdit_Lvl_SecretComp.setText(jh.get_quality_value(save_file, 139041))
        self.ui.lineEdit_Modifier_SecretComp.setText(jh.get_quality_value(save_file, 139041, 'EffectiveLevelModifier'))
        self.ui.lineEdit_Effective_SecretComp.setText(jh.get_quality_value(save_file, 139041, 'EffectiveLevel'))

    def append_map(self, save_file):
        # Teleportation
        self.ui.comboBox_Region.clear()
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
        self.ui.checkBox_Poss_Reports_Reach.setCheckState(jh.get_port_reports(save_file, 'The Reach'))
        self.ui.checkBox_Poss_Reports_Albion.setCheckState(jh.get_port_reports(save_file, 'Albion'))
        self.ui.checkBox_Poss_Reports_Eleutheria.setCheckState(jh.get_port_reports(save_file, 'Eleutheria'))
        self.ui.checkBox_Poss_Reports_TBK.setCheckState(jh.get_port_reports(save_file, 'The Blue Kingdom'))
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

    def append_bank(self, save_file):
        saved_bank_items = save_file['SavedBankItems']
        self.ui.tableWidget_Bank.setRowCount(len(save_file['SavedBankItems']))
        for index, cargo_id in enumerate(saved_bank_items):
            name, amount = jh.get_cargo(save_file, cargo_id)

            cargo_name = QTableWidgetItem()
            cargo_name.setText(name)
            cargo_amount = QTableWidgetItem()
            cargo_amount.setText(amount)

            self.ui.tableWidget_Bank.setItem(index, 0, cargo_name)
            self.ui.tableWidget_Bank.setItem(index, 1, cargo_amount)

    def update_stats(self, level, effective_level, selection, val_id, modifier=None):
        if not INITIALIZATION:
            global ERRORS, SAVE_FILE

            objects = [level, effective_level]
            if modifier:
                objects.append(modifier)

            if any(sender.text() == '' for sender in objects):
                for sender in objects:
                    sender.setText('0')
                    sender.setProperty('valid', True)
                    sender.setStyle(self.style())

            val_level = level.text()
            val_modifier = modifier.text() if modifier else '0'

            try:
                val1 = int(val_level)
                val2 = int(val_modifier)

                if val1 < 0:
                    for sender in [level, effective_level]:
                        sender.setProperty('valid', False)
                        sender.setStyle(self.style())
                    ERRORS = True
                elif val2 < 0:
                    for sender in [modifier, effective_level]:
                        sender.setProperty('valid', False)
                        sender.setStyle(self.style())
                    ERRORS = True
                else:
                    elements = [level, effective_level]
                    if modifier:
                        elements.append(modifier)

                    for sender in elements:
                        sender.setProperty('valid', True)
                        sender.setStyle(self.style())

                    effective_level.setText(str(val1 + val2))
                    SAVE_FILE = jh.write_stats(SAVE_FILE, val1, val2, val_id)

                    ERRORS = False
            except ValueError:
                for sender in [selection, effective_level]:
                    sender.setProperty('valid', False)
                    sender.setStyle(self.style())

                ERRORS = True

    def update_current_port(self):
        if not INITIALIZATION:

            global SAVE_FILE
            SAVE_FILE = jh.write_current_port(SAVE_FILE, self.sender().currentText(), CACHED_SAVEFILE)

    def update_fow_state(self, region):
        if not INITIALIZATION:
            global SAVE_FILE
            SAVE_FILE = jh.write_fow_values(SAVE_FILE, self.sender().checkState(), region)

    def update_possessions(self, val_id):
        if not INITIALIZATION:
            global ERRORS, SAVE_FILE
            value = self.sender().text()
            if value == '':
                self.sender().setText('0')
            else:
                try:
                    value = int(value)
                    if value >= 0:
                        self.sender().setStyleSheet('color: rgb(0,0,0)')
                        SAVE_FILE = jh.write_possessions(SAVE_FILE, value, val_id)
                        ERRORS = False
                    else:
                        self.sender().setStyleSheet('color: rgb(255,0,0)')
                        ERRORS = True
                except ValueError:
                    self.sender().setStyleSheet('color: rgb(255,0,0)')
                    ERRORS = True

    def update_port_reports(self, region_name):
        if not INITIALIZATION:
            global SAVE_FILE
            jh.write_port_reports(SAVE_FILE, self.sender().checkState(), region_name)

    def update_heirlooms(self, val_id):
        if not INITIALIZATION:
            global SAVE_FILE
            jh.write_heirlooms(SAVE_FILE, self.sender().isChecked(), val_id)

    def generate_port_list(self):
        region = self.sender().currentText()
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
