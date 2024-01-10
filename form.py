# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 606)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("OCR A Becker RUS-LAT")
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.prokat = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prokat.sizePolicy().hasHeightForWidth())
        self.prokat.setSizePolicy(sizePolicy)
        self.prokat.setObjectName("prokat")
        self.gridLayout = QtWidgets.QGridLayout(self.prokat)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.prokat)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.passport_prokat_label = QtWidgets.QLabel(self.prokat)
        font = QtGui.QFont()
        font.setFamily("OCR A Becker RUS-LAT")
        font.setPointSize(14)
        self.passport_prokat_label.setFont(font)
        self.passport_prokat_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passport_prokat_label.setObjectName("passport_prokat_label")
        self.gridLayout.addWidget(self.passport_prokat_label, 2, 0, 1, 2)
        self.name_label = QtWidgets.QLabel(self.prokat)
        font = QtGui.QFont()
        font.setFamily("OCR A Becker RUS-LAT")
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name_label.setObjectName("name_label")
        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 2)
        self.tableView = QtWidgets.QTableView(self.prokat)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 4, 4, 1)
        self.velo_prokat_label = QtWidgets.QLabel(self.prokat)
        font = QtGui.QFont()
        font.setFamily("OCR A Becker RUS-LAT")
        font.setPointSize(14)
        self.velo_prokat_label.setFont(font)
        self.velo_prokat_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.velo_prokat_label.setObjectName("velo_prokat_label")
        self.gridLayout.addWidget(self.velo_prokat_label, 1, 0, 1, 2)
        self.velo_prokat = QtWidgets.QComboBox(self.prokat)
        self.velo_prokat.setObjectName("velo_prokat")
        self.gridLayout.addWidget(self.velo_prokat, 1, 2, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.prokat)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 3, 1, 1)
        self.passport_prokat = QtWidgets.QLineEdit(self.prokat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passport_prokat.sizePolicy().hasHeightForWidth())
        self.passport_prokat.setSizePolicy(sizePolicy)
        self.passport_prokat.setToolTip("")
        self.passport_prokat.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.passport_prokat.setObjectName("passport_prokat")
        self.gridLayout.addWidget(self.passport_prokat, 2, 2, 1, 2)
        self.passport_prokat_2 = QtWidgets.QLineEdit(self.prokat)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passport_prokat_2.sizePolicy().hasHeightForWidth())
        self.passport_prokat_2.setSizePolicy(sizePolicy)
        self.passport_prokat_2.setToolTip("")
        self.passport_prokat_2.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.passport_prokat_2.setObjectName("passport_prokat_2")
        self.gridLayout.addWidget(self.passport_prokat_2, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.prokat)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 2)
        icon = QtGui.QIcon.fromTheme("pda")
        self.tabWidget.addTab(self.prokat, icon, "")
        self.velos = QtWidgets.QWidget()
        self.velos.setObjectName("velos")
        self.tabWidget.addTab(self.velos, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.passport_prokat_label.setText(_translate("MainWindow", "ФИО:"))
        self.name_label.setText(_translate("MainWindow", "Имя:"))
        self.velo_prokat_label.setText(_translate("MainWindow", "Велосипед:"))
        self.pushButton_3.setText(_translate("MainWindow", "Завершить"))
        self.pushButton_2.setText(_translate("MainWindow", "Изменить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.prokat), _translate("MainWindow", "Прокат"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.velos), _translate("MainWindow", "Велосипеды"))
