# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supplier_menu.ui'
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

class Ui_SupplierMenu(object):
    def setupUi(self, SupplierMenu):
        if not SupplierMenu.objectName():
            SupplierMenu.setObjectName(u"SupplierMenu")
        SupplierMenu.resize(739, 652)
        self.horizontalLayout = QHBoxLayout(SupplierMenu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_6 = QLabel(SupplierMenu)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)

        self.verticalLayout_4.addWidget(self.label_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(SupplierMenu)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.editNamaSupplier = QLineEdit(SupplierMenu)
        self.editNamaSupplier.setObjectName(u"editNamaSupplier")

        self.horizontalLayout_8.addWidget(self.editNamaSupplier)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(SupplierMenu)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.editAlamat = QLineEdit(SupplierMenu)
        self.editAlamat.setObjectName(u"editAlamat")

        self.horizontalLayout_4.addWidget(self.editAlamat)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.btnSimpan = QPushButton(SupplierMenu)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.horizontalLayout_6.addWidget(self.btnSimpan)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.line = QFrame(SupplierMenu)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(SupplierMenu)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.editCariDataSupplier = QLineEdit(SupplierMenu)
        self.editCariDataSupplier.setObjectName(u"editCariDataSupplier")

        self.horizontalLayout_7.addWidget(self.editCariDataSupplier)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.tableDataSupplier = QTableView(SupplierMenu)
        self.tableDataSupplier.setObjectName(u"tableDataSupplier")

        self.verticalLayout_5.addWidget(self.tableDataSupplier)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.retranslateUi(SupplierMenu)

        QMetaObject.connectSlotsByName(SupplierMenu)
    # setupUi

    def retranslateUi(self, SupplierMenu):
        SupplierMenu.setWindowTitle(QCoreApplication.translate("SupplierMenu", u"Form", None))
        self.label_6.setText(QCoreApplication.translate("SupplierMenu", u"Form Master Supplier danData Supplier :", None))
        self.label_8.setText(QCoreApplication.translate("SupplierMenu", u"Nama Supplier :", None))
        self.label_4.setText(QCoreApplication.translate("SupplierMenu", u"Alamat :", None))
        self.btnSimpan.setText(QCoreApplication.translate("SupplierMenu", u"Simpan", None))
        self.label_7.setText(QCoreApplication.translate("SupplierMenu", u"Data Supplier :", None))
        self.editCariDataSupplier.setPlaceholderText(QCoreApplication.translate("SupplierMenu", u"Cari ...", None))
    # retranslateUi

