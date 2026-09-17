# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(797, 713)
        self.actionAsset = QAction(MainWindow)
        self.actionAsset.setObjectName(u"actionAsset")
        self.actionTangki = QAction(MainWindow)
        self.actionTangki.setObjectName(u"actionTangki")
        self.actionEdit_Password = QAction(MainWindow)
        self.actionEdit_Password.setObjectName(u"actionEdit_Password")
        self.actionDonate = QAction(MainWindow)
        self.actionDonate.setObjectName(u"actionDonate")
        self.actionReports = QAction(MainWindow)
        self.actionReports.setObjectName(u"actionReports")
        self.actionSupplier = QAction(MainWindow)
        self.actionSupplier.setObjectName(u"actionSupplier")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.verticalLayout_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.tabWidgetPage1.setEnabled(True)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.tabWidgetPage2.setEnabled(True)
        self.tabWidget.addTab(self.tabWidgetPage2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 797, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTemplate = QMenu(self.menubar)
        self.menuTemplate.setObjectName(u"menuTemplate")
        self.menuForm = QMenu(self.menubar)
        self.menuForm.setObjectName(u"menuForm")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTemplate.menuAction())
        self.menubar.addAction(self.menuForm.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionReports)
        self.menuTemplate.addAction(self.actionEdit_Password)
        self.menuForm.addAction(self.actionAsset)
        self.menuForm.addAction(self.actionTangki)
        self.menuForm.addAction(self.actionSupplier)
        self.menuAbout.addAction(self.actionDonate)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAsset.setText(QCoreApplication.translate("MainWindow", u"Assets", None))
        self.actionTangki.setText(QCoreApplication.translate("MainWindow", u"Tangki", None))
        self.actionEdit_Password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.actionDonate.setText(QCoreApplication.translate("MainWindow", u"Donate", None))
        self.actionReports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.actionSupplier.setText(QCoreApplication.translate("MainWindow", u"Supplier", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SIPB", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sistem Informasi Pemantuan BBM", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PT. Tanjung Redeb Hutani", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), "")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTemplate.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuForm.setTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

