# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 448)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(9999, 9999))
        font = QFont()
        font.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.dev_github = QAction(MainWindow)
        self.dev_github.setObjectName(u"dev_github")
        font1 = QFont()
        font1.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font1.setBold(True)
        self.dev_github.setFont(font1)
        self.support = QAction(MainWindow)
        self.support.setObjectName(u"support")
        self.actionccc = QAction(MainWindow)
        self.actionccc.setObjectName(u"actionccc")
        self.usage = QAction(MainWindow)
        self.usage.setObjectName(u"usage")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(99999, 99999))
        self.cb_char_name = QComboBox(self.centralwidget)
        self.cb_char_name.setObjectName(u"cb_char_name")
        self.cb_char_name.setGeometry(QRect(15, 49, 361, 71))
        font2 = QFont()
        font2.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font2.setPointSize(13)
        font2.setBold(True)
        self.cb_char_name.setFont(font2)
        self.cb_lang_name = QComboBox(self.centralwidget)
        self.cb_lang_name.setObjectName(u"cb_lang_name")
        self.cb_lang_name.setGeometry(QRect(15, 126, 361, 31))
        self.cb_lang_name.setFont(font2)
        self.text_edit = QPlainTextEdit(self.centralwidget)
        self.text_edit.setObjectName(u"text_edit")
        self.text_edit.setGeometry(QRect(15, 206, 451, 151))
        self.text_edit.setFont(font2)
        self.text_edit.setFrameShape(QFrame.Box)
        self.text_edit.setFrameShadow(QFrame.Sunken)
        self.text_edit.setCenterOnScroll(True)
        self.btn_run_tts = QPushButton(self.centralwidget)
        self.btn_run_tts.setObjectName(u"btn_run_tts")
        self.btn_run_tts.setGeometry(QRect(15, 360, 451, 31))
        self.btn_run_tts.setFont(font2)
        self.vs_sound = QSlider(self.centralwidget)
        self.vs_sound.setObjectName(u"vs_sound")
        self.vs_sound.setGeometry(QRect(398, 46, 20, 111))
        self.vs_sound.setFont(font)
        self.vs_sound.setMaximum(100)
        self.vs_sound.setValue(50)
        self.vs_sound.setOrientation(Qt.Vertical)
        self.label_sound = QLabel(self.centralwidget)
        self.label_sound.setObjectName(u"label_sound")
        self.label_sound.setGeometry(QRect(395, 19, 31, 21))
        self.label_sound.setFont(font)
        self.label_sound.setLayoutDirection(Qt.LeftToRight)
        self.vs_speed = QSlider(self.centralwidget)
        self.vs_speed.setObjectName(u"vs_speed")
        self.vs_speed.setGeometry(QRect(438, 46, 20, 111))
        self.vs_speed.setMinimum(0)
        self.vs_speed.setMaximum(20)
        self.vs_speed.setSingleStep(1)
        self.vs_speed.setPageStep(1)
        self.vs_speed.setValue(10)
        self.vs_speed.setOrientation(Qt.Vertical)
        self.label_speed = QLabel(self.centralwidget)
        self.label_speed.setObjectName(u"label_speed")
        self.label_speed.setGeometry(QRect(435, 19, 31, 21))
        self.label_speed.setFont(font)
        self.label_speed.setLayoutDirection(Qt.LeftToRight)
        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(16, 18, 61, 21))
        self.status_label.setFont(font2)
        self.label_current_status = QLabel(self.centralwidget)
        self.label_current_status.setObjectName(u"label_current_status")
        self.label_current_status.setGeometry(QRect(80, 19, 281, 21))
        self.label_current_status.setFont(font2)
        self.check_is_translate = QCheckBox(self.centralwidget)
        self.check_is_translate.setObjectName(u"check_is_translate")
        self.check_is_translate.setGeometry(QRect(16, 180, 91, 20))
        self.check_is_translate.setFont(font)
        self.check_is_sr = QCheckBox(self.centralwidget)
        self.check_is_sr.setObjectName(u"check_is_sr")
        self.check_is_sr.setGeometry(QRect(120, 180, 121, 20))
        self.check_is_sr.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setFont(font)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.dev_github)
        self.menu.addAction(self.support)
        self.menu.addAction(self.usage)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"KDR TTS", None))
        self.dev_github.setText(QCoreApplication.translate("MainWindow", u"\uac1c\ubc1c\uc790 Github", None))
        self.support.setText(QCoreApplication.translate("MainWindow", u"\ud6c4\uc6d0", None))
        self.actionccc.setText("")
        self.usage.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\ubc95", None))
        self.text_edit.setPlainText(QCoreApplication.translate("MainWindow", u"\uc548\ub155\ud558\uc138\uc694.", None))
        self.btn_run_tts.setText(QCoreApplication.translate("MainWindow", u"TTS\ub85c \uc77d\uae30", None))
        self.label_sound.setText(QCoreApplication.translate("MainWindow", u"\uc18c\ub9ac", None))
        self.label_speed.setText(QCoreApplication.translate("MainWindow", u"\uc18d\ub3c4", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.label_current_status.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.check_is_translate.setText(QCoreApplication.translate("MainWindow", u"\ubc88\uc5ed \ud65c\uc131\ud654", None))
        self.check_is_sr.setText(QCoreApplication.translate("MainWindow", u"\uc74c\uc131\uc778\uc2dd \ud65c\uc131\ud654", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\uba54\ub274", None))
    # retranslateUi

