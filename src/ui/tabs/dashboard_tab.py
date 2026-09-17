# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)

class Ui_DashboardTab(object):
    def setupUi(self, DashboardTab):
        if not DashboardTab.objectName():
            DashboardTab.setObjectName(u"DashboardTab")
        DashboardTab.resize(723, 703)
        self.verticalLayout = QVBoxLayout(DashboardTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(DashboardTab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(DashboardTab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(DashboardTab)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(DashboardTab)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_8 = QLabel(DashboardTab)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(DashboardTab)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_6.addWidget(self.label_9)

        self.label_10 = QLabel(DashboardTab)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_6.addWidget(self.label_10)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_11 = QLabel(DashboardTab)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout.addWidget(self.label_11)

        self.editCariTangki = QLineEdit(DashboardTab)
        self.editCariTangki.setObjectName(u"editCariTangki")

        self.horizontalLayout.addWidget(self.editCariTangki)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.tableView = QTableView(DashboardTab)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_7.addWidget(self.tableView)


        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(DashboardTab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.tablePeringkatKonsumsiBBM = QTableView(DashboardTab)
        self.tablePeringkatKonsumsiBBM.setObjectName(u"tablePeringkatKonsumsiBBM")

        self.verticalLayout_2.addWidget(self.tablePeringkatKonsumsiBBM)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_12 = QLabel(DashboardTab)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_9.addWidget(self.label_12)

        self.tableRiwayatPengisianBBM = QTableView(DashboardTab)
        self.tableRiwayatPengisianBBM.setObjectName(u"tableRiwayatPengisianBBM")

        self.verticalLayout_9.addWidget(self.tableRiwayatPengisianBBM)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(DashboardTab)

        QMetaObject.connectSlotsByName(DashboardTab)
    # setupUi

    def retranslateUi(self, DashboardTab):
        DashboardTab.setWindowTitle(QCoreApplication.translate("DashboardTab", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("DashboardTab", u"Ringkasan Stok Hari Ini :", None))
        self.label_5.setText(QCoreApplication.translate("DashboardTab", u"Total Stok BBM", None))
        self.label_6.setText(QCoreApplication.translate("DashboardTab", u"0 Liter", None))
        self.label_7.setText(QCoreApplication.translate("DashboardTab", u"Total BBM Keluar", None))
        self.label_8.setText(QCoreApplication.translate("DashboardTab", u"0 Liter", None))
        self.label_9.setText(QCoreApplication.translate("DashboardTab", u"Total BBM Masuk", None))
        self.label_10.setText(QCoreApplication.translate("DashboardTab", u"0 Liter", None))
        self.label_11.setText(QCoreApplication.translate("DashboardTab", u"Status Tangki BBM :", None))
        self.editCariTangki.setPlaceholderText(QCoreApplication.translate("DashboardTab", u"Cari ...", None))
        self.label.setText(QCoreApplication.translate("DashboardTab", u"Peringkat Konsumsi Tertinggi :", None))
        self.label_12.setText(QCoreApplication.translate("DashboardTab", u"Pengisian Terakhir :", None))
    # retranslateUi

