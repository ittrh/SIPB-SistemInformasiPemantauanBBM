# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dispensing_tab.ui'
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_DispensingTab(object):
    def setupUi(self, DispensingTab):
        if not DispensingTab.objectName():
            DispensingTab.setObjectName(u"DispensingTab")
        DispensingTab.resize(809, 602)
        self.horizontalLayout_8 = QHBoxLayout(DispensingTab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(DispensingTab)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)

        self.verticalLayout_4.addWidget(self.label_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(DispensingTab)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.editCariSumberTangki = QLineEdit(DispensingTab)
        self.editCariSumberTangki.setObjectName(u"editCariSumberTangki")

        self.horizontalLayout.addWidget(self.editCariSumberTangki)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tableSumberTangki = QTableView(DispensingTab)
        self.tableSumberTangki.setObjectName(u"tableSumberTangki")

        self.verticalLayout_2.addWidget(self.tableSumberTangki)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(DispensingTab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.editCariIdentitasAsset = QLineEdit(DispensingTab)
        self.editCariIdentitasAsset.setObjectName(u"editCariIdentitasAsset")

        self.horizontalLayout_2.addWidget(self.editCariIdentitasAsset)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableIdentitasAsset = QTableView(DispensingTab)
        self.tableIdentitasAsset.setObjectName(u"tableIdentitasAsset")

        self.verticalLayout.addWidget(self.tableIdentitasAsset)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(DispensingTab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.editOdometer = QLineEdit(DispensingTab)
        self.editOdometer.setObjectName(u"editOdometer")

        self.horizontalLayout_4.addWidget(self.editOdometer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(DispensingTab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.editVolumeKeluar = QLineEdit(DispensingTab)
        self.editVolumeKeluar.setObjectName(u"editVolumeKeluar")

        self.horizontalLayout_3.addWidget(self.editVolumeKeluar)

        self.label_7 = QLabel(DispensingTab)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(DispensingTab)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.editPetugasPengisi = QLineEdit(DispensingTab)
        self.editPetugasPengisi.setObjectName(u"editPetugasPengisi")

        self.horizontalLayout_5.addWidget(self.editPetugasPengisi)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.btnSimpan = QPushButton(DispensingTab)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.horizontalLayout_6.addWidget(self.btnSimpan)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(DispensingTab)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.dateFilterStart = QDateTimeEdit(DispensingTab)
        self.dateFilterStart.setObjectName(u"dateFilterStart")

        self.horizontalLayout_9.addWidget(self.dateFilterStart)

        self.label_9 = QLabel(DispensingTab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.dateFilterEnd = QDateTimeEdit(DispensingTab)
        self.dateFilterEnd.setObjectName(u"dateFilterEnd")

        self.horizontalLayout_9.addWidget(self.dateFilterEnd)

        self.btnFilter = QPushButton(DispensingTab)
        self.btnFilter.setObjectName(u"btnFilter")

        self.horizontalLayout_9.addWidget(self.btnFilter)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(DispensingTab)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.editCariRiwayat = QLineEdit(DispensingTab)
        self.editCariRiwayat.setObjectName(u"editCariRiwayat")

        self.horizontalLayout_7.addWidget(self.editCariRiwayat)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.tableRiwayat = QTableView(DispensingTab)
        self.tableRiwayat.setObjectName(u"tableRiwayat")

        self.verticalLayout_5.addWidget(self.tableRiwayat)


        self.horizontalLayout_8.addLayout(self.verticalLayout_5)


        self.retranslateUi(DispensingTab)

        QMetaObject.connectSlotsByName(DispensingTab)
    # setupUi

    def retranslateUi(self, DispensingTab):
        DispensingTab.setWindowTitle(QCoreApplication.translate("DispensingTab", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("DispensingTab", u"Form Pengisian BBM ke Kendaraan :", None))
        self.label.setText(QCoreApplication.translate("DispensingTab", u"Sumber Tangki :", None))
        self.editCariSumberTangki.setPlaceholderText(QCoreApplication.translate("DispensingTab", u"Cari ...", None))
        self.label_2.setText(QCoreApplication.translate("DispensingTab", u"Identitas Asset :", None))
        self.editCariIdentitasAsset.setPlaceholderText(QCoreApplication.translate("DispensingTab", u"Cari ...", None))
        self.label_4.setText(QCoreApplication.translate("DispensingTab", u"Odometer/Hourmeter :", None))
        self.label_3.setText(QCoreApplication.translate("DispensingTab", u"Volume Keluar :", None))
        self.label_7.setText(QCoreApplication.translate("DispensingTab", u"(L)", None))
        self.label_5.setText(QCoreApplication.translate("DispensingTab", u"Petugas Pengisi :", None))
        self.btnSimpan.setText(QCoreApplication.translate("DispensingTab", u"Simpan", None))
        self.label_10.setText(QCoreApplication.translate("DispensingTab", u"Filter dari Tanggal:", None))
        self.label_9.setText(QCoreApplication.translate("DispensingTab", u"-", None))
        self.btnFilter.setText(QCoreApplication.translate("DispensingTab", u"Filter", None))
        self.label_8.setText(QCoreApplication.translate("DispensingTab", u"Riwayat Pengisian BBM :", None))
        self.editCariRiwayat.setPlaceholderText(QCoreApplication.translate("DispensingTab", u"Cari ...", None))
    # retranslateUi

