# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'assets_menu.ui'
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

class Ui_AssetsMenu(object):
    def setupUi(self, AssetsMenu):
        if not AssetsMenu.objectName():
            AssetsMenu.setObjectName(u"AssetsMenu")
        AssetsMenu.resize(751, 648)
        self.horizontalLayout_8 = QHBoxLayout(AssetsMenu)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(AssetsMenu)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)

        self.verticalLayout_4.addWidget(self.label_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(AssetsMenu)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.editCariTipeBBM = QLineEdit(AssetsMenu)
        self.editCariTipeBBM.setObjectName(u"editCariTipeBBM")

        self.horizontalLayout_2.addWidget(self.editCariTipeBBM)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tableTipeBBM = QTableView(AssetsMenu)
        self.tableTipeBBM.setObjectName(u"tableTipeBBM")

        self.verticalLayout_3.addWidget(self.tableTipeBBM)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(AssetsMenu)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.editCariTipeKendaraan = QLineEdit(AssetsMenu)
        self.editCariTipeKendaraan.setObjectName(u"editCariTipeKendaraan")

        self.horizontalLayout.addWidget(self.editCariTipeKendaraan)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableTipeKendaraan = QTableView(AssetsMenu)
        self.tableTipeKendaraan.setObjectName(u"tableTipeKendaraan")

        self.verticalLayout.addWidget(self.tableTipeKendaraan)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(AssetsMenu)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.editCariLokasiKendaraan = QLineEdit(AssetsMenu)
        self.editCariLokasiKendaraan.setObjectName(u"editCariLokasiKendaraan")

        self.horizontalLayout_3.addWidget(self.editCariLokasiKendaraan)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.tableLokasiKendaraan = QTableView(AssetsMenu)
        self.tableLokasiKendaraan.setObjectName(u"tableLokasiKendaraan")

        self.verticalLayout_2.addWidget(self.tableLokasiKendaraan)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(AssetsMenu)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.editKodeAsset = QLineEdit(AssetsMenu)
        self.editKodeAsset.setObjectName(u"editKodeAsset")

        self.horizontalLayout_4.addWidget(self.editKodeAsset)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(AssetsMenu)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.editPlatNomor = QLineEdit(AssetsMenu)
        self.editPlatNomor.setObjectName(u"editPlatNomor")

        self.horizontalLayout_5.addWidget(self.editPlatNomor)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.btnSimpan = QPushButton(AssetsMenu)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.horizontalLayout_6.addWidget(self.btnSimpan)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.line = QFrame(AssetsMenu)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(AssetsMenu)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.editCariDataAsset = QLineEdit(AssetsMenu)
        self.editCariDataAsset.setObjectName(u"editCariDataAsset")

        self.horizontalLayout_7.addWidget(self.editCariDataAsset)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.tableDataAsset = QTableView(AssetsMenu)
        self.tableDataAsset.setObjectName(u"tableDataAsset")

        self.verticalLayout_5.addWidget(self.tableDataAsset)


        self.horizontalLayout_8.addLayout(self.verticalLayout_5)


        self.retranslateUi(AssetsMenu)

        QMetaObject.connectSlotsByName(AssetsMenu)
    # setupUi

    def retranslateUi(self, AssetsMenu):
        AssetsMenu.setWindowTitle(QCoreApplication.translate("AssetsMenu", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("AssetsMenu", u"Form Assets dan Data Assets :", None))
        self.label_3.setText(QCoreApplication.translate("AssetsMenu", u"Tipe BBM :", None))
        self.editCariTipeBBM.setPlaceholderText(QCoreApplication.translate("AssetsMenu", u"Cari ...", None))
        self.label_2.setText(QCoreApplication.translate("AssetsMenu", u"Tipe Kendaraan :", None))
        self.editCariTipeKendaraan.setPlaceholderText(QCoreApplication.translate("AssetsMenu", u"Cari ...", None))
        self.label.setText(QCoreApplication.translate("AssetsMenu", u"Lokasi Kendaraan :", None))
        self.editCariLokasiKendaraan.setPlaceholderText(QCoreApplication.translate("AssetsMenu", u"Cari ...", None))
        self.label_4.setText(QCoreApplication.translate("AssetsMenu", u"Kode Asset :", None))
        self.label_5.setText(QCoreApplication.translate("AssetsMenu", u"Plat Nomor :", None))
        self.btnSimpan.setText(QCoreApplication.translate("AssetsMenu", u"Simpan", None))
        self.label_7.setText(QCoreApplication.translate("AssetsMenu", u"Data Asset :", None))
        self.editCariDataAsset.setPlaceholderText(QCoreApplication.translate("AssetsMenu", u"Cari ...", None))
    # retranslateUi

