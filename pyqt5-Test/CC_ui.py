# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CC_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ComputerControll(object):
    def setupUi(self, ComputerControll):
        ComputerControll.setObjectName("ComputerControll")
        ComputerControll.resize(430, 284)
        self.verticalLayout = QtWidgets.QVBoxLayout(ComputerControll)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widgetStack = QtWidgets.QStackedWidget(ComputerControll)
        self.widgetStack.setObjectName("widgetStack")
        self.mainSeite = QtWidgets.QWidget()
        self.mainSeite.setObjectName("mainSeite")
        self.gridLayout = QtWidgets.QGridLayout(self.mainSeite)
        self.gridLayout.setObjectName("gridLayout")
        self.knopf5 = QtWidgets.QPushButton(self.mainSeite)
        self.knopf5.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */")
        self.knopf5.setObjectName("knopf5")
        self.gridLayout.addWidget(self.knopf5, 1, 1, 1, 1)
        self.knopf8 = QtWidgets.QPushButton(self.mainSeite)
        self.knopf8.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */")
        self.knopf8.setObjectName("knopf8")
        self.gridLayout.addWidget(self.knopf8, 2, 1, 1, 1)
        self.knopf2 = QtWidgets.QPushButton(self.mainSeite)
        self.knopf2.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */")
        self.knopf2.setObjectName("knopf2")
        self.gridLayout.addWidget(self.knopf2, 0, 1, 1, 1)
        self.knopf4 = QtWidgets.QPushButton(self.mainSeite)
        self.knopf4.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */")
        self.knopf4.setObjectName("knopf4")
        self.gridLayout.addWidget(self.knopf4, 1, 0, 1, 1)
        self.knopf1 = QtWidgets.QPushButton(self.mainSeite)
        self.knopf1.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */")
        self.knopf1.setObjectName("knopf1")
        self.gridLayout.addWidget(self.knopf1, 0, 0, 1, 1)
        self.knopf7 = QtWidgets.QPushButton(self.mainSeite)
        self.knopf7.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */")
        self.knopf7.setObjectName("knopf7")
        self.gridLayout.addWidget(self.knopf7, 2, 0, 1, 1)
        self.knopf3 = QtWidgets.QPushButton(self.mainSeite)
        self.knopf3.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */")
        self.knopf3.setObjectName("knopf3")
        self.gridLayout.addWidget(self.knopf3, 0, 2, 1, 1)
        self.knopf6 = QtWidgets.QPushButton(self.mainSeite)
        self.knopf6.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */\n"
"")
        self.knopf6.setObjectName("knopf6")
        self.gridLayout.addWidget(self.knopf6, 1, 2, 1, 1)
        self.knopf9 = QtWidgets.QPushButton(self.mainSeite)
        self.knopf9.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */")
        self.knopf9.setObjectName("knopf9")
        self.gridLayout.addWidget(self.knopf9, 2, 2, 1, 1)
        self.widgetStack.addWidget(self.mainSeite)
        self.Lautstaerke = QtWidgets.QWidget()
        self.Lautstaerke.setObjectName("Lautstaerke")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Lautstaerke)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.Lautstaerke)
        self.frame.setMinimumSize(QtCore.QSize(412, 63))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 5px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout.addWidget(self.pushButton_12)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"font: 8pt \"Arial\";\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout.addWidget(self.pushButton_13)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.Lautstaerke)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setStyleSheet("border-radius: 5px;\n"
"background-color: rgb(47, 47, 53);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid #F62A53;\n"
"  padding: 10px 20px; /* Innenabstand (oben/unten links/rechts) */\n"
"font: 4pt \"Arial\";\n"
"\n"
"")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setSliderPosition(50)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.horizontalSlider)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.widgetStack.addWidget(self.Lautstaerke)
        self.verticalLayout.addWidget(self.widgetStack)

        self.retranslateUi(ComputerControll)
        self.widgetStack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ComputerControll)

    def retranslateUi(self, ComputerControll):
        _translate = QtCore.QCoreApplication.translate
        ComputerControll.setWindowTitle(_translate("ComputerControll", "Form"))
        self.knopf5.setText(_translate("ComputerControll", "unused"))
        self.knopf8.setText(_translate("ComputerControll", "Paint"))
        self.knopf2.setText(_translate("ComputerControll", "Lautstärke"))
        self.knopf4.setText(_translate("ComputerControll", "Apex"))
        self.knopf1.setText(_translate("ComputerControll", "Hellichkeit"))
        self.knopf7.setText(_translate("ComputerControll", "Discord"))
        self.knopf3.setText(_translate("ComputerControll", "Dc mute"))
        self.knopf6.setText(_translate("ComputerControll", "bestimmter ordner"))
        self.knopf9.setText(_translate("ComputerControll", "MC"))
        self.pushButton_10.setText(_translate("ComputerControll", "Gesamt"))
        self.pushButton_12.setText(_translate("ComputerControll", "Browser"))
        self.pushButton_11.setText(_translate("ComputerControll", "Games"))
        self.pushButton_13.setText(_translate("ComputerControll", "Unknown"))
