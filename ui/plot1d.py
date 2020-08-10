# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\plot1d.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(987, 389)
        Dialog.setSizeGripEnabled(False)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = PlotWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tabInteraction = QtWidgets.QWidget()
        self.tabInteraction.setMinimumSize(QtCore.QSize(0, 0))
        self.tabInteraction.setObjectName("tabInteraction")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabInteraction)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutInteraction = QtWidgets.QVBoxLayout()
        self.verticalLayoutInteraction.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayoutInteraction.setObjectName("verticalLayoutInteraction")
        self.groupBoxDisplay = QtWidgets.QGroupBox(self.tabInteraction)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxDisplay.setFont(font)
        self.groupBoxDisplay.setObjectName("groupBoxDisplay")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBoxDisplay)
        self.verticalLayout_4.setContentsMargins(1, 5, 1, 1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayoutLog = QtWidgets.QHBoxLayout()
        self.horizontalLayoutLog.setObjectName("horizontalLayoutLog")
        self.checkBoxLogX = QtWidgets.QCheckBox(self.groupBoxDisplay)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxLogX.setFont(font)
        self.checkBoxLogX.setObjectName("checkBoxLogX")
        self.horizontalLayoutLog.addWidget(self.checkBoxLogX)
        self.checkBoxLogY = QtWidgets.QCheckBox(self.groupBoxDisplay)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxLogY.setFont(font)
        self.checkBoxLogY.setObjectName("checkBoxLogY")
        self.horizontalLayoutLog.addWidget(self.checkBoxLogY)
        self.verticalLayout_4.addLayout(self.horizontalLayoutLog)
        self.checkBoxSymbol = QtWidgets.QCheckBox(self.groupBoxDisplay)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxSymbol.setFont(font)
        self.checkBoxSymbol.setObjectName("checkBoxSymbol")
        self.verticalLayout_4.addWidget(self.checkBoxSymbol)
        self.checkBoxCrossHair = QtWidgets.QCheckBox(self.groupBoxDisplay)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxCrossHair.setFont(font)
        self.checkBoxCrossHair.setChecked(False)
        self.checkBoxCrossHair.setObjectName("checkBoxCrossHair")
        self.verticalLayout_4.addWidget(self.checkBoxCrossHair)
        self.verticalLayoutInteraction.addWidget(self.groupBoxDisplay)
        self.groupBoxPlotDataItem = QtWidgets.QGroupBox(self.tabInteraction)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxPlotDataItem.setFont(font)
        self.groupBoxPlotDataItem.setObjectName("groupBoxPlotDataItem")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxPlotDataItem)
        self.verticalLayout_3.setContentsMargins(1, 5, 1, 1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutPlotDataItem = QtWidgets.QVBoxLayout()
        self.verticalLayoutPlotDataItem.setObjectName("verticalLayoutPlotDataItem")
        self.radioButtonFitNone = QtWidgets.QRadioButton(self.groupBoxPlotDataItem)
        self.radioButtonFitNone.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.radioButtonFitNone.setFont(font)
        self.radioButtonFitNone.setChecked(True)
        self.radioButtonFitNone.setObjectName("radioButtonFitNone")
        self.verticalLayoutPlotDataItem.addWidget(self.radioButtonFitNone)
        self.verticalLayout_3.addLayout(self.verticalLayoutPlotDataItem)
        self.verticalLayoutInteraction.addWidget(self.groupBoxPlotDataItem)
        self.groupBoxCurveInteraction = QtWidgets.QGroupBox(self.tabInteraction)
        self.groupBoxCurveInteraction.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxCurveInteraction.setFont(font)
        self.groupBoxCurveInteraction.setObjectName("groupBoxCurveInteraction")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxCurveInteraction)
        self.verticalLayout_2.setContentsMargins(1, 5, 1, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBoxFFT = QtWidgets.QGroupBox(self.groupBoxCurveInteraction)
        self.groupBoxFFT.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxFFT.setFont(font)
        self.groupBoxFFT.setObjectName("groupBoxFFT")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBoxFFT)
        self.horizontalLayout_4.setContentsMargins(1, 5, 1, 1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButtonFFT = QtWidgets.QRadioButton(self.groupBoxFFT)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.radioButtonFFT.setFont(font)
        self.radioButtonFFT.setObjectName("radioButtonFFT")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButtonFFT)
        self.horizontalLayout_4.addWidget(self.radioButtonFFT)
        self.radioButtonFFTnoDC = QtWidgets.QRadioButton(self.groupBoxFFT)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.radioButtonFFTnoDC.setFont(font)
        self.radioButtonFFTnoDC.setObjectName("radioButtonFFTnoDC")
        self.buttonGroup.addButton(self.radioButtonFFTnoDC)
        self.horizontalLayout_4.addWidget(self.radioButtonFFTnoDC)
        self.radioButtonIFFT = QtWidgets.QRadioButton(self.groupBoxFFT)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.radioButtonIFFT.setFont(font)
        self.radioButtonIFFT.setObjectName("radioButtonIFFT")
        self.buttonGroup.addButton(self.radioButtonIFFT)
        self.horizontalLayout_4.addWidget(self.radioButtonIFFT)
        self.verticalLayout_2.addWidget(self.groupBoxFFT)
        self.groupBoxFit = QtWidgets.QGroupBox(self.groupBoxCurveInteraction)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxFit.setFont(font)
        self.groupBoxFit.setObjectName("groupBoxFit")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBoxFit)
        self.verticalLayout_5.setContentsMargins(1, 5, 1, 1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayoutFitModel = QtWidgets.QVBoxLayout()
        self.verticalLayoutFitModel.setObjectName("verticalLayoutFitModel")
        self.verticalLayout_5.addLayout(self.verticalLayoutFitModel)
        self.verticalLayout_2.addWidget(self.groupBoxFit)
        self.verticalLayoutInteraction.addWidget(self.groupBoxCurveInteraction)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutInteraction.addItem(spacerItem)
        self.labelCoordinate = QtWidgets.QLabel(self.tabInteraction)
        self.labelCoordinate.setMinimumSize(QtCore.QSize(125, 0))
        self.labelCoordinate.setText("")
        self.labelCoordinate.setObjectName("labelCoordinate")
        self.verticalLayoutInteraction.addWidget(self.labelCoordinate)
        self.verticalLayout.addLayout(self.verticalLayoutInteraction)
        self.tabWidget.addTab(self.tabInteraction, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBoxDisplay.setTitle(_translate("Dialog", "Display"))
        self.checkBoxLogX.setText(_translate("Dialog", "log x"))
        self.checkBoxLogY.setText(_translate("Dialog", "log y"))
        self.checkBoxSymbol.setText(_translate("Dialog", "symbol (fastest without)"))
        self.checkBoxCrossHair.setText(_translate("Dialog", "cross hair (fastest without)"))
        self.groupBoxPlotDataItem.setTitle(_translate("Dialog", "Select curve"))
        self.radioButtonFitNone.setText(_translate("Dialog", "None"))
        self.groupBoxCurveInteraction.setTitle(_translate("Dialog", "Curve interaction"))
        self.groupBoxFFT.setTitle(_translate("Dialog", "FFT"))
        self.radioButtonFFT.setText(_translate("Dialog", "FFT"))
        self.radioButtonFFTnoDC.setText(_translate("Dialog", "FFT (no DC)"))
        self.radioButtonIFFT.setText(_translate("Dialog", "IFFT"))
        self.groupBoxFit.setTitle(_translate("Dialog", "Fit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInteraction), _translate("Dialog", "Interaction"))

from plot_widget import PlotWidget
