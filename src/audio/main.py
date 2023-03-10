# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 743)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(778, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 3, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(213, 249, 255);")
        self.widget.setObjectName("widget")
        self.gridLayout_4.addWidget(self.widget, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(0, 172, 140);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.spinBox_downsample = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_downsample.setMinimum(1)
        self.spinBox_downsample.setProperty("value", 1)
        self.spinBox_downsample.setObjectName("spinBox_downsample")
        self.gridLayout.addWidget(self.spinBox_downsample, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.spinBox_updateInterval = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_updateInterval.setMinimum(1)
        self.spinBox_updateInterval.setMaximum(100)
        self.spinBox_updateInterval.setProperty("value", 30)
        self.spinBox_updateInterval.setObjectName("spinBox_updateInterval")
        self.gridLayout.addWidget(self.spinBox_updateInterval, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setStyleSheet("#pushButton {\n"
"    background-color: rgb(92, 186, 102);\n"
"    color: white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setStyleSheet("#pushButton_2 {\n"
"    background-color: rgb(255, 75, 85);\n"
"    color: white;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 3, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_13.addWidget(self.label_18, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")
        self.gridLayout_13.addWidget(self.label_17, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_13)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 3, 3, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setObjectName("label_12")
        self.gridLayout_10.addWidget(self.label_12, 0, 0, 1, 1)
        self.doubleSpinBox_yrangemax = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_yrangemax.setDecimals(1)
        self.doubleSpinBox_yrangemax.setMaximum(1.0)
        self.doubleSpinBox_yrangemax.setSingleStep(0.1)
        self.doubleSpinBox_yrangemax.setProperty("value", 0.5)
        self.doubleSpinBox_yrangemax.setObjectName("doubleSpinBox_yrangemax")
        self.gridLayout_10.addWidget(self.doubleSpinBox_yrangemax, 0, 2, 1, 1)
        self.doubleSpinBox_yrangemin = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_yrangemin.setDecimals(1)
        self.doubleSpinBox_yrangemin.setMinimum(-1.0)
        self.doubleSpinBox_yrangemin.setMaximum(0.0)
        self.doubleSpinBox_yrangemin.setSingleStep(0.1)
        self.doubleSpinBox_yrangemin.setProperty("value", -0.5)
        self.doubleSpinBox_yrangemin.setObjectName("doubleSpinBox_yrangemin")
        self.gridLayout_10.addWidget(self.doubleSpinBox_yrangemin, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_10, 2, 3, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 4, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VoicePlotter"))
        self.label.setText(_translate("MainWindow", "<strong>Earth Inversion</strong><br> Voice Plotter"))
        self.groupBox.setTitle(_translate("MainWindow", "Set Parameters"))
        self.label_3.setText(_translate("MainWindow", "Window Length (>28)"))
        self.lineEdit_2.setText(_translate("MainWindow", "44100"))
        self.label_2.setText(_translate("MainWindow", "Audio Device"))
        self.lineEdit.setText(_translate("MainWindow", "1000"))
        self.label_4.setText(_translate("MainWindow", "Sampling Rate (>1000 Hz)"))
        self.label_5.setText(_translate("MainWindow", " Down Sample (>0)"))
        self.label_6.setText(_translate("MainWindow", " Update Interval"))
        self.pushButton.setText(_translate("MainWindow", "Start Plot"))
        self.pushButton_2.setText(_translate("MainWindow", "Stop Plot"))
        self.label_18.setText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "Active Threads"))
        self.label_12.setText(_translate("MainWindow", "YRange"))
        self.pushButton_3.setText(_translate("MainWindow", "Upload\n"
"Video"))
        self.pushButton_4.setText(_translate("MainWindow", "Open\n"
"Camera"))
