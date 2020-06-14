import sys

from PyQt5 import QtWidgets
# from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtCore import QSettings

from utils.data_handler import DataHandler
from utils.util import *
from utils.messages import *
from ui.ui import Ui_dialog

ORGANIZATION_NAME = 'leefilll'
ORGANIZATION_DOMAIN = 'none.com'
APPLICATION_NAME = 'Rating Extractor'
DEFAULT_USER_NAME = "이지원"
DEFAULT_USER_TEAM = "편성운영팀"


class MainWindow(QtWidgets.QDialog, Ui_dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.file_name = None
        self.user_name = DEFAULT_USER_NAME
        self.user_team = DEFAULT_USER_TEAM
        self.default_broadcaster = "TV CHOSUN"
        self.default_order = ["JTBC", "MBN", "채널A"]
        self.default_main = ["TV조선뉴스9", "JTBC뉴스룸", "MBN종합뉴스", "뉴스A"]

        # Connect widgets to functions
        self.checkbox.toggled.connect(self.check_default_setting)

        # Set disabled to all the widgets
        self.basic_name.setEnabled(False)
        self.basic_team.setEnabled(False)
        self.bc_default.setEnabled(False)
        self.bc_list.setEnabled(False)
        self.bc_main.setEnabled(False)
        self.btn_save.setEnabled(False)
        self.btn_cancel.setEnabled(False)

    @pyqtSlot()
    def file_browser(self):
        filter = "xls(*.xls *.xlsx)"
        self.file_name = QtWidgets.QFileDialog.getOpenFileName(self, filter=filter)[
            0]
        self.textBrowser.setText("")
        if self.file_name:
            self.print_messages()

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
        self.basic_name.setPlainText("")
        self.basic_team.setPlainText("")
        self.basic_name.setPlaceholderText(DEFAULT_USER_NAME)
        self.basic_team.setPlaceholderText(DEFAULT_USER_TEAM)
        self.basic_name.setEnabled(False)
        self.basic_team.setEnabled(False)

    def use_custom_setting(self):
        self.basic_name.setEnabled(True)
        self.basic_team.setEnabled(True)

    # TODO: ! Settings for other users
    # def save_settings(self):
    #     if self.basic_name.toPlainText() == "":
    #         self.alert("실패", "이름을 입력해주세요", "", "inform")
    #         self.checkbox.setChecked(False)
    #         return
    #
    #     # self.basic_team.toPlainText()
    #     if self.basic_team.toPlainText() == "":
    #         self.alert("실패", "팀 이름을 입력해주세요", "", "inform")
    #         self.checkbox.setChecked(False)
    #         return
    #
    #     settings = QSettings()
    #     for i, t in enumerate(self.text_widget_list):
    #         settings.setValue(self.setting_trail[i], t.toPlainText())
    #
    #     msg = QtWidgets.QMessageBox()
    #     # msg.setIcon(QtWidgets.QMessageBox.Information)
    #     msg.setText("정보가 저장되었습니다.")
    #     msg.setInformativeText("입력하신 정보가 기본값으로 설정됩니다.")
    #     msg.setWindowTitle("기본값 설정")
    #     # msg.setDetailedText("The details are as follows:")
    #     msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    #     msg.exec_()
    #
    #     # Get default setting about basic information
    #     self.user_name = settings.value("basic/name")
    #     self.user_team = settings.value("basic/team")
    #
    #     # Get default setting about broadcasters
    #     self.my_bc = settings.value("bc/default")
    #     self.other_bcs = settings.value("bc/list")
    #     self.main_pg = settings.value("bc/main")
    #
    #     self.checkbox.setChecked(True)
    #
    #     for t in self.text_widget_list:
    #         t.setPlainText("")
    #
    #     self.use_default_setting()
    #
    # def cancel_setting(self):
    #     for t in self.text_widget_list:
    #         t.setPlainText("")

    def print_messages(self):
        name = self.basic_name.toPlainText()
        team = self.basic_team.toPlainText()
        if name == "":
            name = DEFAULT_USER_NAME
        if team == "":
            team = DEFAULT_USER_TEAM

        data_handler = DataHandler(self.file_name)
        bc_list = data_handler.broadcasters
        is_weekend = any(
            day in data_handler.date_str for day in ["(토)", "(일)"])
        chosun_news_name = ""

        if is_weekend:
            chosun_news_name = "TV조선뉴스7"
        else:
            chosun_news_name = "TV조선뉴스9"

        news_names = [chosun_news_name, "JTBC뉴스룸", "MBN종합뉴스", "뉴스A"]

        matrix = get_matrix_programs(
            bc_list, news_names)

        # Print Basic Information
        self.textBrowser.append(print_name(
            team, name, data_handler.date_str))
        # self.textBrowser.append("\n")
        self.textBrowser.append("\n수도권 일일 가구 {}".format(
            print_capital_summary(bc_list, data_handler.d_matrix[2])))
        self.textBrowser.append("수도권 프라임 가구 {}".format(
            print_capital_summary(bc_list, data_handler.p_matrix[2])))
        # self.textBrowser.append("\n")
        self.textBrowser.append("\n1. 채널 시청률")
        self.textBrowser.append("○ 일일 시청률")
        self.textBrowser.append(print_summary(bc_list, data_handler.d_matrix))
        self.textBrowser.append("○ 프라임 타임 기준")
        self.textBrowser.append(print_summary(bc_list, data_handler.p_matrix))
        self.textBrowser.append("2. 주요 프로그램 시청률 (수도권 기준)")
        self.textBrowser.append("")
        self.textBrowser.append("○ 메인뉴스 시청률")
        self.textBrowser.append(print_main_programs(
            bc_list, matrix, news_names))


if __name__ == '__main__':
    QCoreApplication.setApplicationName(ORGANIZATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QCoreApplication.setApplicationName(APPLICATION_NAME)
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
