# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Youssef\Desktop\task3\Part A\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 731)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_image1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_image1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_image1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_image1.setLineWidth(1)
        self.frame_image1.setObjectName("frame_image1")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_image1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.Img1comboBox = QtWidgets.QComboBox(self.frame_image1)
        self.Img1comboBox.setMinimumSize(QtCore.QSize(270, 0))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        self.Img1comboBox.setFont(font)
        self.Img1comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Img1comboBox.setAutoFillBackground(False)
        self.Img1comboBox.setObjectName("Img1comboBox")
        self.Img1comboBox.addItem("")
        self.Img1comboBox.addItem("")
        self.Img1comboBox.addItem("")
        self.Img1comboBox.addItem("")
        self.gridLayout_9.addWidget(self.Img1comboBox, 0, 2, 1, 1)
        self.Img1Label = QtWidgets.QLabel(self.frame_image1)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Img1Label.setFont(font)
        self.Img1Label.setObjectName("Img1Label")
        self.gridLayout_9.addWidget(self.Img1Label, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ImgComp_1 = ImageView(self.frame_image1)
        self.ImgComp_1.setObjectName("ImgComp_1")
        self.gridLayout_3.addWidget(self.ImgComp_1, 0, 1, 1, 1)
        self.image_1 = ImageView(self.frame_image1)
        self.image_1.setObjectName("image_1")
        self.gridLayout_3.addWidget(self.image_1, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_3, 1, 0, 1, 3)
        self.Button1 = QtWidgets.QPushButton(self.frame_image1)
        self.Button1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Button1.setObjectName("Button1")
        self.gridLayout_9.addWidget(self.Button1, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_image1, 0, 0, 2, 2)
        self.frame_image2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_image2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_image2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_image2.setLineWidth(1)
        self.frame_image2.setObjectName("frame_image2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_image2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Img2Label = QtWidgets.QLabel(self.frame_image2)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Img2Label.setFont(font)
        self.Img2Label.setObjectName("Img2Label")
        self.gridLayout_8.addWidget(self.Img2Label, 0, 0, 1, 1)
        self.Button2 = QtWidgets.QPushButton(self.frame_image2)
        self.Button2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Button2.setObjectName("Button2")
        self.gridLayout_8.addWidget(self.Button2, 0, 1, 1, 1)
        self.Img2comboBox = QtWidgets.QComboBox(self.frame_image2)
        self.Img2comboBox.setMinimumSize(QtCore.QSize(270, 0))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        self.Img2comboBox.setFont(font)
        self.Img2comboBox.setObjectName("Img2comboBox")
        self.Img2comboBox.addItem("")
        self.Img2comboBox.addItem("")
        self.Img2comboBox.addItem("")
        self.Img2comboBox.addItem("")
        self.gridLayout_8.addWidget(self.Img2comboBox, 0, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.image_2 = ImageView(self.frame_image2)
        self.image_2.setObjectName("image_2")
        self.gridLayout_4.addWidget(self.image_2, 0, 0, 1, 1)
        self.ImgComp_2 = ImageView(self.frame_image2)
        self.ImgComp_2.setObjectName("ImgComp_2")
        self.gridLayout_4.addWidget(self.ImgComp_2, 0, 1, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_4, 1, 0, 1, 3)
        self.gridLayout_2.addWidget(self.frame_image2, 2, 0, 2, 2)
        self.frame_output = QtWidgets.QFrame(self.centralwidget)
        self.frame_output.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_output.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_output.setLineWidth(1)
        self.frame_output.setObjectName("frame_output")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_output)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.Output1Label = QtWidgets.QLabel(self.frame_output)
        self.Output1Label.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Output1Label.setFont(font)
        self.Output1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Output1Label.setObjectName("Output1Label")
        self.gridLayout_10.addWidget(self.Output1Label, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setHorizontalSpacing(20)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Output_1 = ImageView(self.frame_output)
        self.Output_1.setObjectName("Output_1")
        self.gridLayout_6.addWidget(self.Output_1, 0, 0, 1, 1)
        self.Output_2 = ImageView(self.frame_output)
        self.Output_2.setObjectName("Output_2")
        self.gridLayout_6.addWidget(self.Output_2, 0, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_6, 1, 0, 1, 2)
        self.Output2Label = QtWidgets.QLabel(self.frame_output)
        self.Output2Label.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Output2Label.setFont(font)
        self.Output2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Output2Label.setObjectName("Output2Label")
        self.gridLayout_10.addWidget(self.Output2Label, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_output, 2, 2, 2, 2)
        self.frame_mixer = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        self.frame_mixer.setFont(font)
        self.frame_mixer.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_mixer.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_mixer.setObjectName("frame_mixer")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_mixer)
        self.gridLayout.setObjectName("gridLayout")
        self.Select_image_2 = QtWidgets.QComboBox(self.frame_mixer)
        self.Select_image_2.setObjectName("Select_image_2")
        self.Select_image_2.addItem("")
        self.Select_image_2.addItem("")
        self.gridLayout.addWidget(self.Select_image_2, 3, 1, 1, 1)
        self.Comp1Label = QtWidgets.QLabel(self.frame_mixer)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Comp1Label.setFont(font)
        self.Comp1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Comp1Label.setObjectName("Comp1Label")
        self.gridLayout.addWidget(self.Comp1Label, 1, 0, 1, 1)
        self.Comp2Label = QtWidgets.QLabel(self.frame_mixer)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Comp2Label.setFont(font)
        self.Comp2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Comp2Label.setObjectName("Comp2Label")
        self.gridLayout.addWidget(self.Comp2Label, 3, 0, 1, 1)
        self.Select_Comp_1 = QtWidgets.QComboBox(self.frame_mixer)
        self.Select_Comp_1.setObjectName("Select_Comp_1")
        self.Select_Comp_1.addItem("")
        self.Select_Comp_1.addItem("")
        self.gridLayout.addWidget(self.Select_Comp_1, 1, 1, 1, 1)
        self.MixerLabel = QtWidgets.QLabel(self.frame_mixer)
        font = QtGui.QFont()
        font.setFamily("Kristen ITC")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.MixerLabel.setFont(font)
        self.MixerLabel.setObjectName("MixerLabel")
        self.gridLayout.addWidget(self.MixerLabel, 0, 0, 1, 1)
        self.Comp2_type = QtWidgets.QComboBox(self.frame_mixer)
        self.Comp2_type.setObjectName("Comp2_type")
        self.Comp2_type.addItem("")
        self.Comp2_type.addItem("")
        self.Comp2_type.addItem("")
        self.Comp2_type.addItem("")
        self.Comp2_type.addItem("")
        self.Comp2_type.addItem("")
        self.gridLayout.addWidget(self.Comp2_type, 4, 1, 1, 4)
        self.Comp1_type = QtWidgets.QComboBox(self.frame_mixer)
        self.Comp1_type.setObjectName("Comp1_type")
        self.Comp1_type.addItem("")
        self.Comp1_type.addItem("")
        self.Comp1_type.addItem("")
        self.Comp1_type.addItem("")
        self.Comp1_type.addItem("")
        self.Comp1_type.addItem("")
        self.gridLayout.addWidget(self.Comp1_type, 2, 1, 1, 4)
        self.Select_output = QtWidgets.QComboBox(self.frame_mixer)
        self.Select_output.setObjectName("Select_output")
        self.Select_output.addItem("")
        self.Select_output.addItem("")
        self.gridLayout.addWidget(self.Select_output, 0, 1, 1, 4)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.frame_mixer)
        self.horizontalSlider_2.setMinimumSize(QtCore.QSize(200, 0))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_2.setTickInterval(10)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout.addWidget(self.horizontalSlider_2, 3, 2, 1, 1)
        self.Percentage2 = QtWidgets.QLabel(self.frame_mixer)
        self.Percentage2.setAlignment(QtCore.Qt.AlignCenter)
        self.Percentage2.setObjectName("Percentage2")
        self.gridLayout.addWidget(self.Percentage2, 3, 3, 1, 2)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.frame_mixer)
        self.horizontalSlider_3.setMinimumSize(QtCore.QSize(200, 0))
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider_3.setTickInterval(10)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout.addWidget(self.horizontalSlider_3, 1, 2, 1, 1)
        self.Percentage1 = QtWidgets.QLabel(self.frame_mixer)
        self.Percentage1.setMinimumSize(QtCore.QSize(32, 0))
        self.Percentage1.setAlignment(QtCore.Qt.AlignCenter)
        self.Percentage1.setObjectName("Percentage1")
        self.gridLayout.addWidget(self.Percentage1, 1, 3, 1, 2, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame_mixer, 0, 2, 2, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Img1comboBox.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Img1comboBox.setItemText(1, _translate("MainWindow", "Phase"))
        self.Img1comboBox.setItemText(2, _translate("MainWindow", "Real"))
        self.Img1comboBox.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.Img1Label.setText(_translate("MainWindow", "Image 1"))
        self.Button1.setText(_translate("MainWindow", "Open"))
        self.Img2Label.setText(_translate("MainWindow", "Image 2"))
        self.Button2.setText(_translate("MainWindow", "Open"))
        self.Img2comboBox.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Img2comboBox.setItemText(1, _translate("MainWindow", "Phase"))
        self.Img2comboBox.setItemText(2, _translate("MainWindow", "Real"))
        self.Img2comboBox.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.Output1Label.setText(_translate("MainWindow", "Output 1"))
        self.Output2Label.setText(_translate("MainWindow", "Output 2"))
        self.Select_image_2.setItemText(0, _translate("MainWindow", "Image 1"))
        self.Select_image_2.setItemText(1, _translate("MainWindow", "Image 2"))
        self.Comp1Label.setText(_translate("MainWindow", "Component 1      "))
        self.Comp2Label.setText(_translate("MainWindow", "Component 2       "))
        self.Select_Comp_1.setItemText(0, _translate("MainWindow", "Image 1"))
        self.Select_Comp_1.setItemText(1, _translate("MainWindow", "Image 2"))
        self.MixerLabel.setText(_translate("MainWindow", "Mixer Output"))
        self.Comp2_type.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Comp2_type.setItemText(1, _translate("MainWindow", "Phase"))
        self.Comp2_type.setItemText(2, _translate("MainWindow", "Real"))
        self.Comp2_type.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.Comp2_type.setItemText(4, _translate("MainWindow", "Uni Magnitude"))
        self.Comp2_type.setItemText(5, _translate("MainWindow", "Uni Phase"))
        self.Comp1_type.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.Comp1_type.setItemText(1, _translate("MainWindow", "Phase"))
        self.Comp1_type.setItemText(2, _translate("MainWindow", "Real"))
        self.Comp1_type.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.Comp1_type.setItemText(4, _translate("MainWindow", "Uni Magnitude"))
        self.Comp1_type.setItemText(5, _translate("MainWindow", "Uni Phase"))
        self.Select_output.setItemText(0, _translate("MainWindow", "Output 1"))
        self.Select_output.setItemText(1, _translate("MainWindow", "Output 2"))
        self.Percentage2.setText(_translate("MainWindow", "%"))
        self.Percentage1.setText(_translate("MainWindow", "%"))
from pyqtgraph import ImageView
