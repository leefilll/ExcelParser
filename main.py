import sys

from PyQt5 import QtWidgets
# from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QSettings

from utils.data_handler import DataHandler
from utils.util import *
from utils.messages import *
from ui.ui import Ui_dialog

ORGANIZATION_NAME = 'poleewer'
ORGANIZATION_DOMAIN = 'none.com'
APPLICATION_NAME = 'Rating Extractor'

class MainWindow(QtWidgets.QDialog, Ui_dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.file_name = None

        # Get settings
        settings = QSettings()

        # Widget List
        self.text_widget_list = [
            self.basic_name,
            self.basic_team,
            self.bc_default,
            self.bc_list,
            self.bc_main,
        ]

        # Value List
        self.user_name = ""
        self.user_team = ""
        self.my_bc = ""
        self.other_bcs = ""
        self.main_pg = ""

        # Setting Trail List
        self.setting_trail = [
            "basic/name",
            "basic/team",
            "bc/default",
            "bc/list",
            "bc/main"
        ]

        # Connect widgets to functions
        # self.checkbox.toggled.connect(self.check_default_setting)
        self.btn_save.clicked.connect(self.save_settings)
        self.btn_cancel.clicked.connect(self.cancel_setting)
        self.user_name = "이지원"
        self.user_team = "편성운영팀"
        self.basic_name.setPlaceholderText("이지원")
        self.basic_team.setPlaceholderText("편성운영팀")
        self.checkbox.setEnabled(False)
        self.btn_save.setEnabled(False)
        self.btn_cancel.setEnabled(False)
        for widget in self.text_widget_list:
            widget.setEnabled(False)


    @pyqtSlot()
    def file_browser(self):
        settings = QSettings()
        # if not settings.value("basic/name"):
        #     self.alert("실패", "저장된 정보가 없습니다.", "정보를 저장 후 실행해주세요", "infor")
        #     return

        filter = "xls(*.xls *.xlsx)"
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(self, filter=filter)[0]
        self.textBrowser.setText("")
        if self.file_name:
            self.print_messages()

    def init_setting(self):
        """ Settings for first time to use """
        pass

    def alert(self, title, message, detail_msg, icon=None):
        msg = QtWidgets.QMessageBox()
        if icon:
            msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(message)
        msg.setInformativeText(detail_msg)
        msg.setWindowTitle(title)
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def check_default_setting(self):
        if self.checkbox.isChecked():
            self.use_default_setting()
        else:
            self.use_custom_setting()

    def use_default_setting(self):
        # make input area unable
        settings = QSettings()

        # Get default setting about basic information
        self.user_name = settings.value(self.setting_trail[0])
        self.user_team = settings.value(self.setting_trail[1])
        self.my_bc = settings.value(self.setting_trail[2])
        self.other_bcs = settings.value(self.setting_trail[3])
        self.main_pg = settings.value(self.setting_trail[4])

        # Fill the text edit with default values
        self.basic_name.setPlaceholderText(self.user_name)
        self.basic_team.setPlaceholderText(self.user_team)
        self.bc_default.setPlaceholderText(self.my_bc)
        self.bc_list.setPlaceholderText(self.other_bcs)
        self.bc_main.setPlaceholderText(self.main_pg)

        for t in self.text_widget_list:
            t.setEnabled(False)
        # self.basic_date.setEnabled(False)
        self.btn_save.setEnabled(False)
        self.btn_cancel.setEnabled(False)
        # self.basic_date.setPlaceholderText(placeholderText)

    def use_custom_setting(self):
        # make input areas enable
        for t in self.text_widget_list:
            t.setEnabled(True)
            t.setPlaceholderText("")
        # self.basic_date.setEnabled(True)
        self.btn_save.setEnabled(True)
        self.btn_cancel.setEnabled(True)

    def save_settings(self):
        if self.basic_name.toPlainText() == "":
            self.alert("실패", "이름을 입력해주세요", "", "inform")
            self.checkbox.setChecked(False)
            return

        # self.basic_team.toPlainText()
        if self.basic_team.toPlainText() == "":
            self.alert("실패", "팀 이름을 입력해주세요", "", "inform")
            self.checkbox.setChecked(False)
            return

        settings = QSettings()
        for i, t in enumerate(self.text_widget_list):
            settings.setValue(self.setting_trail[i], t.toPlainText())

        msg = QtWidgets.QMessageBox()
        # msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("정보가 저장되었습니다.")
        msg.setInformativeText("입력하신 정보가 기본값으로 설정됩니다.")
        msg.setWindowTitle("기본값 설정")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

        # Get default setting about basic information
        self.user_name = settings.value("basic/name")
        self.user_team = settings.value("basic/team")

        # Get default setting about broadcasters
        self.my_bc = settings.value("bc/default")
        self.other_bcs = settings.value("bc/list")
        self.main_pg = settings.value("bc/main")

        self.checkbox.setChecked(True)

        for t in self.text_widget_list:
            t.setPlainText("")

        self.use_default_setting()


    def cancel_setting(self):
        for t in self.text_widget_list:
            t.setPlainText("")

    def print_messages(self):
        data_handler = DataHandler(self.file_name)
        bc_list = data_handler.broadcasters

        test = get_matrix_programs(bc_list, ["TV조선뉴스9", "JTBC뉴스룸", "MBN종합뉴스", "뉴스A"])

        # Print Basic Information
        self.textBrowser.append(print_name(self.user_team, self.user_name, data_handler.date_str))
        # self.textBrowser.append("\n")
        self.textBrowser.append("\n수도권 일일 가구 {}".format(print_capital_summary(bc_list, data_handler.d_matrix[2])) )
        self.textBrowser.append("수도권 프라임 가구 {}".format(print_capital_summary(bc_list, data_handler.p_matrix[2])))
        # self.textBrowser.append("\n")
        self.textBrowser.append("\n1. 채널 시청률")
        self.textBrowser.append("○ 일일 시청률")
        self.textBrowser.append(print_summary(bc_list, data_handler.d_matrix))
        self.textBrowser.append("○ 프라임 타임 기준")
        self.textBrowser.append(print_summary(bc_list, data_handler.p_matrix))
        self.textBrowser.append("2. 주요 프로그램 시청률 (수도권 기준)")
        self.textBrowser.append("")
        self.textBrowser.append("○ 메인뉴스 시청률")
        self.textBrowser.append(print_main_programs(bc_list, test, ["TV조선뉴스9", "JTBC뉴스룸", "MBN종합뉴스", "뉴스A"]))

if __name__ == '__main__':
    QCoreApplication.setApplicationName(ORGANIZATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QCoreApplication.setApplicationName(APPLICATION_NAME)
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
