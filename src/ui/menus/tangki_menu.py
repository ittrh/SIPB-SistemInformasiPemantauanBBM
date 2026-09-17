# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tangki_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_TangkiMenu(object):
    def setupUi(self, TangkiMenu):
        if not TangkiMenu.objectName():
            TangkiMenu.setObjectName(u"TangkiMenu")
        TangkiMenu.resize(745, 650)
        self.horizontalLayout_3 = QHBoxLayout(TangkiMenu)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(TangkiMenu)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)

        self.verticalLayout_4.addWidget(self.label_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(TangkiMenu)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.editCariLokasiTangki = QLineEdit(TangkiMenu)
        self.editCariLokasiTangki.setObjectName(u"editCariLokasiTangki")

        self.horizontalLayout_2.addWidget(self.editCariLokasiTangki)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tableLokasiTangki = QTableView(TangkiMenu)
        self.tableLokasiTangki.setObjectName(u"tableLokasiTangki")

        self.verticalLayout_3.addWidget(self.tableLokasiTangki)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(TangkiMenu)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.editCariTipeBBM = QLineEdit(TangkiMenu)
        self.editCariTipeBBM.setObjectName(u"editCariTipeBBM")

        self.horizontalLayout.addWidget(self.editCariTipeBBM)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableTipeBBM = QTableView(TangkiMenu)
        self.tableTipeBBM.setObjectName(u"tableTipeBBM")

        self.verticalLayout.addWidget(self.tableTipeBBM)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(TangkiMenu)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.editNamaTangki = QLineEdit(TangkiMenu)
        self.editNamaTangki.setObjectName(u"editNamaTangki")

        self.horizontalLayout_8.addWidget(self.editNamaTangki)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(TangkiMenu)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.editKapasitas = QLineEdit(TangkiMenu)
        self.editKapasitas.setObjectName(u"editKapasitas")

        self.horizontalLayout_4.addWidget(self.editKapasitas)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.btnSimpan = QPushButton(TangkiMenu)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.horizontalLayout_6.addWidget(self.btnSimpan)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.line = QFrame(TangkiMenu)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(TangkiMenu)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.editCariDataTangki = QLineEdit(TangkiMenu)
        self.editCariDataTangki.setObjectName(u"editCariDataTangki")

        self.horizontalLayout_7.addWidget(self.editCariDataTangki)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.tableDataTangki = QTableView(TangkiMenu)
        self.tableDataTangki.setObjectName(u"tableDataTangki")

        self.verticalLayout_5.addWidget(self.tableDataTangki)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.retranslateUi(TangkiMenu)

        QMetaObject.connectSlotsByName(TangkiMenu)
    # setupUi

    def retranslateUi(self, TangkiMenu):
        TangkiMenu.setWindowTitle(QCoreApplication.translate("TangkiMenu", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("TangkiMenu", u"Form Master Tangki dan Data Tangki :", None))
        self.label_3.setText(QCoreApplication.translate("TangkiMenu", u"Lokasi Tangki :", None))
        self.editCariLokasiTangki.setPlaceholderText(QCoreApplication.translate("TangkiMenu", u"Cari ...", None))
        self.label_2.setText(QCoreApplication.translate("TangkiMenu", u"Tipe BBM :", None))
        self.editCariTipeBBM.setPlaceholderText(QCoreApplication.translate("TangkiMenu", u"Cari ...", None))
        self.label_8.setText(QCoreApplication.translate("TangkiMenu", u"Nama Tangki :", None))
        self.label_4.setText(QCoreApplication.translate("TangkiMenu", u"Kapasitas :", None))
        self.btnSimpan.setText(QCoreApplication.translate("TangkiMenu", u"Simpan", None))
        self.label_7.setText(QCoreApplication.translate("TangkiMenu", u"Data Tangki :", None))
        self.editCariDataTangki.setPlaceholderText(QCoreApplication.translate("TangkiMenu", u"Cari ...", None))
    # retranslateUi

