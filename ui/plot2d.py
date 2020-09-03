# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\plot2d.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(1057, 499)
        Dialog.setSizeGripEnabled(False)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = PlotWidget(Dialog)
        self.widget.setMinimumSize(QtCore.QSize(700, 0))
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayoutHist = QtWidgets.QVBoxLayout()
        self.verticalLayoutHist.setObjectName("verticalLayoutHist")
        self.histWidget = HistogramLUTWidget(Dialog)
        self.histWidget.setObjectName("histWidget")
        self.verticalLayoutHist.addWidget(self.histWidget)
        self.plot2dzLabel = QtWidgets.QLabel(Dialog)
        self.plot2dzLabel.setObjectName("plot2dzLabel")
        self.verticalLayoutHist.addWidget(self.plot2dzLabel)
        self.horizontalLayout.addLayout(self.verticalLayoutHist)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabInteraction = QtWidgets.QWidget()
        self.tabInteraction.setObjectName("tabInteraction")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabInteraction)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBoxDisplay = QtWidgets.QGroupBox(self.tabInteraction)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxDisplay.setFont(font)
        self.groupBoxDisplay.setObjectName("groupBoxDisplay")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxDisplay)
        self.verticalLayout.setContentsMargins(1, 5, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBoxDisplay)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.comboBoxcm = QtWidgets.QComboBox(self.groupBoxDisplay)
        self.comboBoxcm.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.comboBoxcm.setFont(font)
        self.comboBoxcm.setObjectName("comboBoxcm")
        self.horizontalLayout_4.addWidget(self.comboBoxcm)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.checkBoxInvert = QtWidgets.QCheckBox(self.groupBoxDisplay)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxInvert.setFont(font)
        self.checkBoxInvert.setObjectName("checkBoxInvert")
        self.verticalLayout.addWidget(self.checkBoxInvert)
        self.checkBoxSwapxy = QtWidgets.QCheckBox(self.groupBoxDisplay)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxSwapxy.setFont(font)
        self.checkBoxSwapxy.setObjectName("checkBoxSwapxy")
        self.verticalLayout.addWidget(self.checkBoxSwapxy)
        self.checkBoxCrossHair = QtWidgets.QCheckBox(self.groupBoxDisplay)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxCrossHair.setFont(font)
        self.checkBoxCrossHair.setChecked(False)
        self.checkBoxCrossHair.setObjectName("checkBoxCrossHair")
        self.verticalLayout.addWidget(self.checkBoxCrossHair)
        self.verticalLayout_2.addWidget(self.groupBoxDisplay)
        self.groupBoxInteraction = QtWidgets.QGroupBox(self.tabInteraction)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxInteraction.setFont(font)
        self.groupBoxInteraction.setObjectName("groupBoxInteraction")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBoxInteraction)
        self.verticalLayout_5.setContentsMargins(1, 5, 1, 1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBoxDrawIsoCurve = QtWidgets.QCheckBox(self.groupBoxInteraction)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxDrawIsoCurve.setFont(font)
        self.checkBoxDrawIsoCurve.setObjectName("checkBoxDrawIsoCurve")
        self.verticalLayout_5.addWidget(self.checkBoxDrawIsoCurve)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBoxInteraction)
        self.label_7.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.checkBoxSubtractAverageX = QtWidgets.QCheckBox(self.groupBoxInteraction)
        self.checkBoxSubtractAverageX.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxSubtractAverageX.setFont(font)
        self.checkBoxSubtractAverageX.setObjectName("checkBoxSubtractAverageX")
        self.horizontalLayout_6.addWidget(self.checkBoxSubtractAverageX)
        self.checkBoxSubtractAverageY = QtWidgets.QCheckBox(self.groupBoxInteraction)
        self.checkBoxSubtractAverageY.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxSubtractAverageY.setFont(font)
        self.checkBoxSubtractAverageY.setObjectName("checkBoxSubtractAverageY")
        self.horizontalLayout_6.addWidget(self.checkBoxSubtractAverageY)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBoxInteraction)
        self.label_8.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBoxDerivativeX = QtWidgets.QCheckBox(self.groupBoxInteraction)
        self.checkBoxDerivativeX.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxDerivativeX.setFont(font)
        self.checkBoxDerivativeX.setObjectName("checkBoxDerivativeX")
        self.horizontalLayout_8.addWidget(self.checkBoxDerivativeX)
        self.checkBoxDerivativeY = QtWidgets.QCheckBox(self.groupBoxInteraction)
        self.checkBoxDerivativeY.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxDerivativeY.setFont(font)
        self.checkBoxDerivativeY.setObjectName("checkBoxDerivativeY")
        self.horizontalLayout_8.addWidget(self.checkBoxDerivativeY)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.checkBoxDerivativeXY = QtWidgets.QCheckBox(self.groupBoxInteraction)
        self.checkBoxDerivativeXY.setMaximumSize(QtCore.QSize(125, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxDerivativeXY.setFont(font)
        self.checkBoxDerivativeXY.setObjectName("checkBoxDerivativeXY")
        self.verticalLayout_3.addWidget(self.checkBoxDerivativeXY)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.groupBoxInteraction)
        self.groupBoxSlicing = QtWidgets.QGroupBox(self.tabInteraction)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxSlicing.setFont(font)
        self.groupBoxSlicing.setObjectName("groupBoxSlicing")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBoxSlicing)
        self.verticalLayout_6.setContentsMargins(1, 5, 1, 1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.groupBoxSlicing)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButtonSliceHorizontal = QtWidgets.QRadioButton(self.groupBoxSlicing)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.radioButtonSliceHorizontal.setFont(font)
        self.radioButtonSliceHorizontal.setChecked(False)
        self.radioButtonSliceHorizontal.setObjectName("radioButtonSliceHorizontal")
        self.horizontalLayout_5.addWidget(self.radioButtonSliceHorizontal)
        self.radioButtonSliceVertical = QtWidgets.QRadioButton(self.groupBoxSlicing)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.radioButtonSliceVertical.setFont(font)
        self.radioButtonSliceVertical.setChecked(True)
        self.radioButtonSliceVertical.setObjectName("radioButtonSliceVertical")
        self.horizontalLayout_5.addWidget(self.radioButtonSliceVertical)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.groupBoxSlicing)
        self.groupBoxExtraction = QtWidgets.QGroupBox(self.tabInteraction)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxExtraction.setFont(font)
        self.groupBoxExtraction.setObjectName("groupBoxExtraction")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBoxExtraction)
        self.verticalLayout_7.setContentsMargins(1, 5, 1, 1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBoxMinimum = QtWidgets.QCheckBox(self.groupBoxExtraction)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxMinimum.setFont(font)
        self.checkBoxMinimum.setObjectName("checkBoxMinimum")
        self.horizontalLayout_3.addWidget(self.checkBoxMinimum)
        self.checkBoxMaximum = QtWidgets.QCheckBox(self.groupBoxExtraction)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxMaximum.setFont(font)
        self.checkBoxMaximum.setObjectName("checkBoxMaximum")
        self.horizontalLayout_3.addWidget(self.checkBoxMaximum)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBoxExtraction)
        self.groupBoxFit = QtWidgets.QGroupBox(self.tabInteraction)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxFit.setFont(font)
        self.groupBoxFit.setObjectName("groupBoxFit")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBoxFit)
        self.verticalLayout_8.setContentsMargins(1, 5, 1, 1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelFit = QtWidgets.QLabel(self.groupBoxFit)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.labelFit.setFont(font)
        self.labelFit.setObjectName("labelFit")
        self.verticalLayout_8.addWidget(self.labelFit)
        self.verticalLayoutFitModel = QtWidgets.QVBoxLayout()
        self.verticalLayoutFitModel.setObjectName("verticalLayoutFitModel")
        self.verticalLayout_8.addLayout(self.verticalLayoutFitModel)
        self.verticalLayout_2.addWidget(self.groupBoxFit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.labelCoordinate = QtWidgets.QLabel(self.tabInteraction)
        self.labelCoordinate.setMinimumSize(QtCore.QSize(190, 0))
        self.labelCoordinate.setText("")
        self.labelCoordinate.setObjectName("labelCoordinate")
        self.verticalLayout_2.addWidget(self.labelCoordinate)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tabInteraction, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.plot2dzLabel.setText(_translate("Dialog", "TextLabel"))
        self.groupBoxDisplay.setTitle(_translate("Dialog", "Display"))
        self.label.setText(_translate("Dialog", "colormap"))
        self.checkBoxInvert.setText(_translate("Dialog", "Invert colormap"))
        self.checkBoxSwapxy.setText(_translate("Dialog", "Swap x/y"))
        self.checkBoxCrossHair.setText(_translate("Dialog", "cross hair (fastest without)"))
        self.groupBoxInteraction.setTitle(_translate("Dialog", "Map interaction"))
        self.checkBoxDrawIsoCurve.setText(_translate("Dialog", "Draw isocurve"))
        self.label_7.setText(_translate("Dialog", "Subtract average:"))
        self.checkBoxSubtractAverageX.setText(_translate("Dialog", "x"))
        self.checkBoxSubtractAverageY.setText(_translate("Dialog", "y"))
        self.label_8.setText(_translate("Dialog", "Derivative:"))
        self.checkBoxDerivativeX.setText(_translate("Dialog", "dx"))
        self.checkBoxDerivativeY.setText(_translate("Dialog", "dy"))
        self.checkBoxDerivativeXY.setText(_translate("Dialog", "sqrt(dx^2+dy^2)"))
        self.groupBoxSlicing.setTitle(_translate("Dialog", "Data slicing"))
        self.label_5.setText(_translate("Dialog", "(double click)"))
        self.radioButtonSliceHorizontal.setText(_translate("Dialog", "horizontal"))
        self.radioButtonSliceVertical.setText(_translate("Dialog", "vertical"))
        self.groupBoxExtraction.setTitle(_translate("Dialog", "Extraction"))
        self.checkBoxMinimum.setText(_translate("Dialog", "minimum"))
        self.checkBoxMaximum.setText(_translate("Dialog", "maximum"))
        self.groupBoxFit.setTitle(_translate("Dialog", "Fit"))
        self.labelFit.setText(_translate("Dialog", "fit model"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInteraction), _translate("Dialog", "Interaction"))

from histogram_lut_widget import HistogramLUTWidget
from plot_widget import PlotWidget
