# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 563)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.TopHorizontalLayout = QtWidgets.QHBoxLayout()
        self.TopHorizontalLayout.setObjectName("TopHorizontalLayout")
        self.pushButtonOpenFolder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpenFolder.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonOpenFolder.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButtonOpenFolder.setObjectName("pushButtonOpenFolder")
        self.TopHorizontalLayout.addWidget(self.pushButtonOpenFolder)
        self.labelPath = QtWidgets.QHBoxLayout()
        self.labelPath.setObjectName("labelPath")
        self.TopHorizontalLayout.addLayout(self.labelPath)
        self.LivePlot = QtWidgets.QHBoxLayout()
        self.LivePlot.setSpacing(6)
        self.LivePlot.setObjectName("LivePlot")
        self.checkBoxLivePlot = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxLivePlot.setEnabled(False)
        self.checkBoxLivePlot.setMaximumSize(QtCore.QSize(65, 30))
        self.checkBoxLivePlot.setObjectName("checkBoxLivePlot")
        self.LivePlot.addWidget(self.checkBoxLivePlot)
        self.labelLivePlotDataBase = QtWidgets.QLabel(self.centralwidget)
        self.labelLivePlotDataBase.setEnabled(False)
        self.labelLivePlotDataBase.setMaximumSize(QtCore.QSize(60, 30))
        self.labelLivePlotDataBase.setText("")
        self.labelLivePlotDataBase.setObjectName("labelLivePlotDataBase")
        self.LivePlot.addWidget(self.labelLivePlotDataBase)
        self.labelLivePlot2 = QtWidgets.QLabel(self.centralwidget)
        self.labelLivePlot2.setEnabled(False)
        self.labelLivePlot2.setMaximumSize(QtCore.QSize(60, 30))
        self.labelLivePlot2.setObjectName("labelLivePlot2")
        self.LivePlot.addWidget(self.labelLivePlot2)
        self.spinBoxLivePlot = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxLivePlot.setEnabled(False)
        self.spinBoxLivePlot.setMinimumSize(QtCore.QSize(25, 0))
        self.spinBoxLivePlot.setMaximumSize(QtCore.QSize(40, 30))
        self.spinBoxLivePlot.setObjectName("spinBoxLivePlot")
        self.LivePlot.addWidget(self.spinBoxLivePlot)
        self.labelLivePlot = QtWidgets.QLabel(self.centralwidget)
        self.labelLivePlot.setEnabled(False)
        self.labelLivePlot.setMaximumSize(QtCore.QSize(10, 30))
        self.labelLivePlot.setObjectName("labelLivePlot")
        self.LivePlot.addWidget(self.labelLivePlot)
        self.TopHorizontalLayout.addLayout(self.LivePlot)
        self.verticalLayout_3.addLayout(self.TopHorizontalLayout)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setMinimumSize(QtCore.QSize(0, 482))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_2.setMinimumSize(QtCore.QSize(0, 0))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelFolder = QtWidgets.QLabel(self.layoutWidget_2)
        self.labelFolder.setObjectName("labelFolder")
        self.verticalLayout_5.addWidget(self.labelFolder)
        self.tableWidgetFolder = QtWidgets.QTableWidget(self.layoutWidget_2)
        self.tableWidgetFolder.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidgetFolder.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidgetFolder.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetFolder.setAlternatingRowColors(True)
        self.tableWidgetFolder.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetFolder.setObjectName("tableWidgetFolder")
        self.tableWidgetFolder.setColumnCount(2)
        self.tableWidgetFolder.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidgetFolder.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidgetFolder.setHorizontalHeaderItem(1, item)
        self.tableWidgetFolder.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetFolder.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetFolder.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetFolder.verticalHeader().setVisible(True)
        self.verticalLayout_5.addWidget(self.tableWidgetFolder)
        self.layoutWidget_3 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelDataBase = QtWidgets.QLabel(self.layoutWidget_3)
        self.labelDataBase.setMaximumSize(QtCore.QSize(110, 16777215))
        self.labelDataBase.setObjectName("labelDataBase")
        self.horizontalLayout.addWidget(self.labelDataBase)
        self.labelCurrentDataBase = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelCurrentDataBase.setFont(font)
        self.labelCurrentDataBase.setStyleSheet("color: green;")
        self.labelCurrentDataBase.setText("")
        self.labelCurrentDataBase.setObjectName("labelCurrentDataBase")
        self.horizontalLayout.addWidget(self.labelCurrentDataBase)
        self.checkBoxHidden = QtWidgets.QCheckBox(self.layoutWidget_3)
        self.checkBoxHidden.setEnabled(False)
        self.checkBoxHidden.setMaximumSize(QtCore.QSize(90, 16777215))
        self.checkBoxHidden.setObjectName("checkBoxHidden")
        self.horizontalLayout.addWidget(self.checkBoxHidden)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.tableWidgetDataBase = QTableWidgetKey(self.layoutWidget_3)
        self.tableWidgetDataBase.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidgetDataBase.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetDataBase.setAlternatingRowColors(True)
        self.tableWidgetDataBase.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetDataBase.setColumnCount(8)
        self.tableWidgetDataBase.setObjectName("tableWidgetDataBase")
        self.tableWidgetDataBase.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDataBase.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDataBase.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDataBase.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDataBase.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDataBase.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDataBase.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDataBase.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDataBase.setHorizontalHeaderItem(7, item)
        self.tableWidgetDataBase.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidgetDataBase.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidgetDataBase.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetDataBase.verticalHeader().setVisible(True)
        self.verticalLayout_11.addWidget(self.tableWidgetDataBase)
        self.verticalLayout.addWidget(self.splitter_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_3 = QtWidgets.QSplitter(self.layoutWidget1)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter_3)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelRun = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelRun.setMinimumSize(QtCore.QSize(1, 0))
        self.labelRun.setMaximumSize(QtCore.QSize(150, 16777215))
        self.labelRun.setObjectName("labelRun")
        self.horizontalLayout_2.addWidget(self.labelRun)
        self.labelCurrentRun = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelCurrentRun.setFont(font)
        self.labelCurrentRun.setText("")
        self.labelCurrentRun.setObjectName("labelCurrentRun")
        self.horizontalLayout_2.addWidget(self.labelCurrentRun)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.tableWidgetParameters = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidgetParameters.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetParameters.setAlternatingRowColors(True)
        self.tableWidgetParameters.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetParameters.setObjectName("tableWidgetParameters")
        self.tableWidgetParameters.setColumnCount(6)
        self.tableWidgetParameters.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetParameters.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetParameters.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetParameters.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetParameters.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetParameters.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetParameters.setHorizontalHeaderItem(5, item)
        self.tableWidgetParameters.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_6.addWidget(self.tableWidgetParameters)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter_3)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelMetadata = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelMetadata.setMaximumSize(QtCore.QSize(140, 16777215))
        self.labelMetadata.setObjectName("labelMetadata")
        self.horizontalLayout_3.addWidget(self.labelMetadata)
        self.labelCurrentMetadata = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelCurrentMetadata.setFont(font)
        self.labelCurrentMetadata.setText("")
        self.labelCurrentMetadata.setObjectName("labelCurrentMetadata")
        self.horizontalLayout_3.addWidget(self.labelCurrentMetadata)
        self.labelFilter = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.labelFilter.setEnabled(False)
        self.labelFilter.setMaximumSize(QtCore.QSize(40, 16777215))
        self.labelFilter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelFilter.setObjectName("labelFilter")
        self.horizontalLayout_3.addWidget(self.labelFilter)
        self.lineEditFilter = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditFilter.setEnabled(False)
        self.lineEditFilter.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEditFilter.setFont(font)
        self.lineEditFilter.setText("")
        self.lineEditFilter.setObjectName("lineEditFilter")
        self.horizontalLayout_3.addWidget(self.lineEditFilter)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.textEditMetadata = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEditMetadata.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEditMetadata.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEditMetadata.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEditMetadata.setReadOnly(True)
        self.textEditMetadata.setObjectName("textEditMetadata")
        self.verticalLayout_7.addWidget(self.textEditMetadata)
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.verticalLayout_3.addWidget(self.splitter)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setMinimumSize(QtCore.QSize(0, 30))
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plotter"))
        self.pushButtonOpenFolder.setText(_translate("MainWindow", "Open folder"))
        self.checkBoxLivePlot.setText(_translate("MainWindow", "LivePlot:"))
        self.labelLivePlot2.setText(_translate("MainWindow", " every"))
        self.labelLivePlot.setText(_translate("MainWindow", "s"))
        self.labelFolder.setText(_translate("MainWindow", "Browse folder:"))
        self.tableWidgetFolder.setSortingEnabled(True)
        item = self.tableWidgetFolder.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "item"))
        item = self.tableWidgetFolder.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "size"))
        self.labelDataBase.setText(_translate("MainWindow", "Browse database:"))
        self.checkBoxHidden.setText(_translate("MainWindow", "Show hidden"))
        self.tableWidgetDataBase.setSortingEnabled(True)
        item = self.tableWidgetDataBase.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "run id"))
        item = self.tableWidgetDataBase.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "dim"))
        item = self.tableWidgetDataBase.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "experiment"))
        item = self.tableWidgetDataBase.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "sample"))
        item = self.tableWidgetDataBase.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "run name"))
        item = self.tableWidgetDataBase.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "started"))
        item = self.tableWidgetDataBase.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "completed"))
        item = self.tableWidgetDataBase.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "records"))
        self.labelRun.setText(_translate("MainWindow", "Browse parameters run:"))
        self.tableWidgetParameters.setSortingEnabled(True)
        item = self.tableWidgetParameters.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "run id"))
        item = self.tableWidgetParameters.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "experiment name"))
        item = self.tableWidgetParameters.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "plotted"))
        item = self.tableWidgetParameters.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "axis"))
        item = self.tableWidgetParameters.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "unit"))
        item = self.tableWidgetParameters.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "swept parameters"))
        self.labelMetadata.setText(_translate("MainWindow", "Browse metadata run:"))
        self.labelFilter.setText(_translate("MainWindow", "Filter:"))

from ..ui.qtablewidgetkey import QTableWidgetKey
