# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sistema.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from src.recursos import *
from ios import Ui_Dialog_iOS
from android import Ui_Dialog_android

class Ui_Dialog_sistema(QDialog, object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(440, 262)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_sistema = QLabel(Dialog)
        self.label_sistema.setObjectName(u"label_sistema")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_sistema.setFont(font)
        self.label_sistema.setAlignment(Qt.AlignCenter)
        
        self.verticalLayout.addWidget(self.label_sistema)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_android = QPushButton(Dialog)
        self.btn_android.setObjectName(u"btn_android")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_android.sizePolicy().hasHeightForWidth())
        self.btn_android.setSizePolicy(sizePolicy)
        self.btn_android.setMinimumSize(QSize(150, 200))
        self.btn_android.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_android.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(189, 189, 189);\n"
"border: none;\n"
"border-radius: 5px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/logos/android.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_android.setIcon(icon)
        self.btn_android.clicked.connect(self.ventana_android)
        self.btn_android.setIconSize(QSize(200, 300))

        self.horizontalLayout.addWidget(self.btn_android)

        self.btn_ios = QPushButton(Dialog)
        self.btn_ios.setObjectName(u"btn_ios")
        sizePolicy.setHeightForWidth(self.btn_ios.sizePolicy().hasHeightForWidth())
        self.btn_ios.setSizePolicy(sizePolicy)
        self.btn_ios.setMinimumSize(QSize(200, 200))
        self.btn_ios.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ios.clicked.connect(self.ventana_ios)
        self.btn_ios.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(189, 189, 189);\n"
"border: none;\n"
"border-radius: 5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/logos/IOS.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ios.setIcon(icon1)
        self.btn_ios.setIconSize(QSize(150, 200))

        self.horizontalLayout.addWidget(self.btn_ios)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.polla = 'polla'

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Word Creator - Elegir Sistema", None))
        self.label_sistema.setText(QCoreApplication.translate("Dialog", u"Elija el sistema del tel\u00e9fono m\u00f3vil", None))
        self.btn_ios.setText("")
    # retranslateUi
    
    def ventana_ios(self):
        self.ventana_iOS = Ventana_iOS()
        self.ventana_iOS.show()
        self.accept()
        
    def ventana_android(self):
        self.ventana_Android = Ventana_Android()
        self.ventana_Android.show()
        self.accept()
        
class Ventana_iOS(Ui_Dialog_iOS, QDialog):
    def __init__(self):
        super(Ventana_iOS, self).__init__()
        self.setupUi(self)

class Ventana_Android(Ui_Dialog_android, QDialog):
    def __init__(self):
        super(Ventana_Android, self).__init__()
        self.setupUi(self)