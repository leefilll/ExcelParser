# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(1063, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog.sizePolicy().hasHeightForWidth())
        dialog.setSizePolicy(sizePolicy)
        dialog.setMinimumSize(QtCore.QSize(900, 500))
        self.groupBox = QtWidgets.QGroupBox(dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 42, 241, 111))
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 28, 221, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(40)
        self.formLayout.setObjectName("formLayout")
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_15.setFont(font)
        self.label_15.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_15.setTextFormat(QtCore.Qt.RichText)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.basic_name = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.basic_name.setEnabled(True)
        self.basic_name.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.basic_name.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.basic_name.setAcceptDrops(True)
        self.basic_name.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.basic_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.basic_name.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.basic_name.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.basic_name.setTabChangesFocus(True)
        self.basic_name.setBackgroundVisible(False)
        self.basic_name.setObjectName("basic_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.basic_name)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_16.setFont(font)
        self.label_16.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_16.setTextFormat(QtCore.Qt.RichText)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.basic_team = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.basic_team.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.basic_team.setInputMethodHints(QtCore.Qt.ImhNone)
        self.basic_team.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.basic_team.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.basic_team.setTabChangesFocus(True)
        self.basic_team.setObjectName("basic_team")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.basic_team)
        self.checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.checkbox.setEnabled(True)
        self.checkbox.setGeometry(QtCore.QRect(166, -1, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkbox.setFont(font)
        self.checkbox.setChecked(True)
        self.checkbox.setTristate(False)
        self.checkbox.setObjectName("checkbox")
        self.groupBox_2 = QtWidgets.QGroupBox(dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 162, 241, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 31, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_4.setFont(font)
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 78, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_6.setFont(font)
        self.label_6.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 135, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_7.setFont(font)
        self.label_7.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_7.setTextFormat(QtCore.Qt.RichText)
        self.label_7.setObjectName("label_7")
        self.bc_default = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.bc_default.setGeometry(QtCore.QRect(70, 33, 161, 21))
        self.bc_default.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.bc_default.setInputMethodHints(QtCore.Qt.ImhNone)
        self.bc_default.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bc_default.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bc_default.setTabChangesFocus(True)
        self.bc_default.setObjectName("bc_default")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QtCore.QRect(70, 51, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setObjectName("label_8")
        self.bc_list = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.bc_list.setGeometry(QtCore.QRect(70, 80, 161, 21))
        self.bc_list.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.bc_list.setInputMethodHints(QtCore.Qt.ImhNone)
        self.bc_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bc_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.bc_list.setTabChangesFocus(True)
        self.bc_list.setObjectName("bc_list")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setEnabled(False)
        self.label_9.setGeometry(QtCore.QRect(70, 99, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_9.setTextFormat(QtCore.Qt.RichText)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 151, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_10.setFont(font)
        self.label_10.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_10.setTextFormat(QtCore.Qt.RichText)
        self.label_10.setObjectName("label_10")
        self.bc_main = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.bc_main.setGeometry(QtCore.QRect(70, 138, 161, 21))
        self.bc_main.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.bc_main.setInputMethodHints(QtCore.Qt.ImhNone)
        self.bc_main.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.bc_main.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.bc_main.setTabChangesFocus(True)
        self.bc_main.setObjectName("bc_main")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setEnabled(False)
        self.label_11.setGeometry(QtCore.QRect(70, 157, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_11.setTextFormat(QtCore.Qt.RichText)
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setEnabled(False)
        self.label_13.setGeometry(QtCore.QRect(69, 111, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_13.setTextFormat(QtCore.Qt.RichText)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setEnabled(False)
        self.label_14.setGeometry(QtCore.QRect(69, 169, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_14.setTextFormat(QtCore.Qt.RichText)
        self.label_14.setObjectName("label_14")
        self.textBrowser = QtWidgets.QTextBrowser(dialog)
        self.textBrowser.setGeometry(QtCore.QRect(270, 60, 771, 391))
        self.textBrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textBrowser.setObjectName("textBrowser")
        self.label_12 = QtWidgets.QLabel(dialog)
        self.label_12.setEnabled(False)
        self.label_12.setGeometry(QtCore.QRect(990, 452, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_12.setTextFormat(QtCore.Qt.RichText)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.toolButton = QtWidgets.QToolButton(dialog)
        self.toolButton.setGeometry(QtCore.QRect(19, 410, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.toolButton.setFont(font)
        self.toolButton.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(13, 366, 251, 44))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_cancel.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.btn_cancel.setAutoDefault(False)
        self.btn_cancel.setDefault(False)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.btn_save = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_save.setEnabled(True)
        self.btn_save.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.btn_save.setCheckable(False)
        self.btn_save.setAutoDefault(False)
        self.btn_save.setDefault(False)
        self.btn_save.setFlat(False)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.label_18 = QtWidgets.QLabel(dialog)
        self.label_18.setEnabled(False)
        self.label_18.setGeometry(QtCore.QRect(271, 39, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_18.setFont(font)
        self.label_18.setLocale(QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea))
        self.label_18.setTextFormat(QtCore.Qt.RichText)
        self.label_18.setObjectName("label_18")
        self.textBrowser.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.label_12.raise_()
        self.toolButton.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_18.raise_()

        self.retranslateUi(dialog)
        self.toolButton.clicked.connect(dialog.file_browser)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Rating Extractor"))
        self.groupBox.setTitle(_translate("dialog", "기본 설정"))
        self.label_15.setText(_translate("dialog", "이름"))
        self.basic_name.setPlaceholderText(_translate("dialog", "이지원"))
        self.label_16.setText(_translate("dialog", "팀"))
        self.basic_team.setPlaceholderText(_translate("dialog", "편성운영팀"))
        self.checkbox.setText(_translate("dialog", "기본값 사용 "))
        self.groupBox_2.setTitle(_translate("dialog", "방송사 설정"))
        self.label_4.setText(_translate("dialog", "기본"))
        self.label_6.setText(_translate("dialog", "비교 순서"))
        self.label_7.setText(_translate("dialog", "주요"))
        self.bc_default.setPlaceholderText(_translate("dialog", "TV CHOSUN"))
        self.label_8.setText(_translate("dialog", "기본값: TV CHOSUN"))
        self.bc_list.setPlaceholderText(_translate("dialog", "JTBC, MBN, 채널A"))
        self.label_9.setText(_translate("dialog", "기본값: JTBC, MBN, 채널A"))
        self.label_10.setText(_translate("dialog", "프로그램"))
        self.bc_main.setPlaceholderText(_translate("dialog", "TV조선뉴스9, JTBC뉴스룸, MBN종합뉴스, 뉴스A"))
        self.label_11.setText(_translate("dialog", "기본값: 메인 뉴스"))
        self.label_13.setText(_translate("dialog", "(쉼표로 구분)"))
        self.label_14.setText(_translate("dialog", "(쉼표로 구분)"))
        self.label_12.setText(_translate("dialog", "v1.0.0"))
        self.toolButton.setText(_translate("dialog", "파일 불러오기"))
        self.btn_cancel.setText(_translate("dialog", "초기화"))
        self.btn_save.setText(_translate("dialog", "확인(저장)"))
        self.label_18.setText(_translate("dialog", "콘솔"))
