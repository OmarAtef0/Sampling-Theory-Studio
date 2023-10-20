# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(987, 797)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 5, 981, 731))
        self.tabWidget.setStyleSheet("QLabel#Header {\n"
"    font-size: 40px; \n"
"}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 630, 961, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.CSV_file_2 = QtWidgets.QFontComboBox(self.gridLayoutWidget)
        self.CSV_file_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.CSV_file_2.setDuplicatesEnabled(False)
        self.CSV_file_2.setFrame(True)
        self.CSV_file_2.setObjectName("CSV_file_2")
        self.gridLayout_2.addWidget(self.CSV_file_2, 1, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 560, 961, 65))
        self.layoutWidget.setStyleSheet("QPushButton#Add_FPA{\n"
"    background-color: DodgerBlue;\n"
"    color:White\n"
"}\n"
"")
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.Frequency = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.Frequency.setObjectName("Frequency")
        self.gridLayout.addWidget(self.Frequency, 0, 2, 1, 1)
        self.Amplitude = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.Amplitude.setObjectName("Amplitude")
        self.gridLayout.addWidget(self.Amplitude, 0, 4, 1, 1)
        self.CSV_file = QtWidgets.QFontComboBox(self.layoutWidget)
        self.CSV_file.setCurrentText("")
        self.CSV_file.setObjectName("CSV_file")
        self.gridLayout.addWidget(self.CSV_file, 0, 0, 1, 1)
        self.Add_FPA = QtWidgets.QPushButton(self.layoutWidget)
        self.Add_FPA.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Add_FPA.setStyleSheet("QPushButton#Add_FPA{\n"
"    background-color: DodgerBlue;\n"
"    color:White\n"
"}\n"
"")
        self.Add_FPA.setObjectName("Add_FPA")
        self.gridLayout.addWidget(self.Add_FPA, 0, 7, 1, 1)
        self.Delete_FPA = QtWidgets.QPushButton(self.layoutWidget)
        self.Delete_FPA.setStyleSheet("QPushButton#Delete_FPA {\n"
"    background-color: red;\n"
"    color: white;\n"
"}\n"
"")
        self.Delete_FPA.setObjectName("Delete_FPA")
        self.gridLayout.addWidget(self.Delete_FPA, 1, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 5, 1, 1)
        self.Phase = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.Phase.setObjectName("Phase")
        self.gridLayout.addWidget(self.Phase, 0, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 961, 531))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.layoutWidget_2)
        self.openGLWidget.setObjectName("openGLWidget")
        self.verticalLayout_2.addWidget(self.openGLWidget)
        self.openGLWidget_2 = QtWidgets.QOpenGLWidget(self.layoutWidget_2)
        self.openGLWidget_2.setObjectName("openGLWidget_2")
        self.verticalLayout_2.addWidget(self.openGLWidget_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.Graph_3 = QtWidgets.QOpenGLWidget(self.tab_3)
        self.Graph_3.setGeometry(QtCore.QRect(10, 40, 791, 581))
        self.Graph_3.setObjectName("Graph_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(810, 90, 111, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_3.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_3.addWidget(self.checkBox_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(810, 320, 160, 61))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider_2.setTickInterval(15)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_4.addWidget(self.horizontalSlider_2)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(810, 220, 160, 52))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.SNR_Label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.SNR_Label.setObjectName("SNR_Label")
        self.verticalLayout_5.addWidget(self.SNR_Label)
        self.SNR_Slider = QtWidgets.QSlider(self.verticalLayoutWidget_5)
        self.SNR_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.SNR_Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.SNR_Slider.setTickInterval(15)
        self.SNR_Slider.setObjectName("SNR_Slider")
        self.verticalLayout_5.addWidget(self.SNR_Slider)
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 640, 791, 71))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSlider_3 = QtWidgets.QSlider(self.layoutWidget_3)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider_3.setTickInterval(0)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalLayout.addWidget(self.horizontalSlider_3)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(False)
        self.label_9.setOpenExternalLinks(False)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Sampling"))
        self.CSV_file_2.setCurrentText(_translate("MainWindow", "Test1"))
        self.label.setText(_translate("MainWindow", "Frequency"))
        self.Add_FPA.setText(_translate("MainWindow", "Add"))
        self.Delete_FPA.setText(_translate("MainWindow", "Delete"))
        self.label_3.setText(_translate("MainWindow", "Phase"))
        self.label_2.setText(_translate("MainWindow", "Amplitude"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Composer"))
        self.checkBox.setText(_translate("MainWindow", "Sampling"))
        self.checkBox_2.setText(_translate("MainWindow", "Add noise"))
        self.label_8.setText(_translate("MainWindow", "Sampling Frequency (Hz)"))
        self.SNR_Label.setText(_translate("MainWindow", "SNR   (dBW)"))
        self.label_10.setText(_translate("MainWindow", "1.0"))
        self.label_9.setText(_translate("MainWindow", "FMax"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Sampler"))