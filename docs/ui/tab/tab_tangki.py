# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_tangki.ui'
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

class Ui_TangkiTab(object):
    def setupUi(self, TangkiTab):
        if not TangkiTab.objectName():
            TangkiTab.setObjectName(u"TangkiTab")
        TangkiTab.resize(790, 688)
        self.verticalLayout_3 = QVBoxLayout(TangkiTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(TangkiTab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(TangkiTab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.dateFilterEnd = QDateTimeEdit(TangkiTab)
        self.dateFilterEnd.setObjectName(u"dateFilterEnd")

        self.horizontalLayout_3.addWidget(self.dateFilterEnd)

        self.label_5 = QLabel(TangkiTab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.dateFilterStart = QDateTimeEdit(TangkiTab)
        self.dateFilterStart.setObjectName(u"dateFilterStart")

        self.horizontalLayout_3.addWidget(self.dateFilterStart)

        self.btnFilter = QPushButton(TangkiTab)
        self.btnFilter.setObjectName(u"btnFilter")

        self.horizontalLayout_3.addWidget(self.btnFilter)

        self.btnClearFilter = QPushButton(TangkiTab)
        self.btnClearFilter.setObjectName(u"btnClearFilter")

        self.horizontalLayout_3.addWidget(self.btnClearFilter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(TangkiTab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.editCariTransfer = QLineEdit(TangkiTab)
        self.editCariTransfer.setObjectName(u"editCariTransfer")

        self.horizontalLayout.addWidget(self.editCariTransfer)

        self.btnTransfer = QPushButton(TangkiTab)
        self.btnTransfer.setObjectName(u"btnTransfer")

        self.horizontalLayout.addWidget(self.btnTransfer)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.tableDataTransfer = QTableView(TangkiTab)
        self.tableDataTransfer.setObjectName(u"tableDataTransfer")

        self.verticalLayout_5.addWidget(self.tableDataTransfer)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(TangkiTab)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.editCariIsiUlang = QLineEdit(TangkiTab)
        self.editCariIsiUlang.setObjectName(u"editCariIsiUlang")

        self.horizontalLayout_6.addWidget(self.editCariIsiUlang)

        self.btnIsiUlang = QPushButton(TangkiTab)
        self.btnIsiUlang.setObjectName(u"btnIsiUlang")

        self.horizontalLayout_6.addWidget(self.btnIsiUlang)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.tableDataIsiUlang = QTableView(TangkiTab)
        self.tableDataIsiUlang.setObjectName(u"tableDataIsiUlang")

        self.verticalLayout_7.addWidget(self.tableDataIsiUlang)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(TangkiTab)

        QMetaObject.connectSlotsByName(TangkiTab)
    # setupUi

    def retranslateUi(self, TangkiTab):
        TangkiTab.setWindowTitle(QCoreApplication.translate("TangkiTab", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("TangkiTab", u"Data Transaksi Tangki :", None))
        self.label_4.setText(QCoreApplication.translate("TangkiTab", u"Filter :", None))
        self.label_5.setText(QCoreApplication.translate("TangkiTab", u"-", None))
        self.btnFilter.setText(QCoreApplication.translate("TangkiTab", u"Filter", None))
        self.btnClearFilter.setText(QCoreApplication.translate("TangkiTab", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("TangkiTab", u"Transfer :", None))
        self.editCariTransfer.setPlaceholderText(QCoreApplication.translate("TangkiTab", u"Cari ...", None))
        self.btnTransfer.setText(QCoreApplication.translate("TangkiTab", u"Transfer Stok", None))
        self.label_6.setText(QCoreApplication.translate("TangkiTab", u"Pengisian Ulang :", None))
        self.editCariIsiUlang.setPlaceholderText(QCoreApplication.translate("TangkiTab", u"Cari ...", None))
        self.btnIsiUlang.setText(QCoreApplication.translate("TangkiTab", u"Isi Ulang", None))
    # retranslateUi

