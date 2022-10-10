# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(343, 280)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar_CPU = QProgressBar(self.frame)
        self.progressBar_CPU.setObjectName(u"progressBar_CPU")
        self.progressBar_CPU.setMaximumSize(QSize(150, 16777215))
        self.progressBar_CPU.setValue(24)
        self.progressBar_CPU.setOrientation(Qt.Vertical)
        self.progressBar_CPU.setInvertedAppearance(False)
        self.progressBar_CPU.setTextDirection(QProgressBar.BottomToTop)

        self.horizontalLayout.addWidget(self.progressBar_CPU)

        self.progressBar_RAM = QProgressBar(self.frame)
        self.progressBar_RAM.setObjectName(u"progressBar_RAM")
        self.progressBar_RAM.setMaximumSize(QSize(150, 16777215))
        self.progressBar_RAM.setValue(24)
        self.progressBar_RAM.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.progressBar_RAM)

        self.progressBar_NETWORK = QProgressBar(self.frame)
        self.progressBar_NETWORK.setObjectName(u"progressBar_NETWORK")
        self.progressBar_NETWORK.setMaximumSize(QSize(150, 16777215))
        self.progressBar_NETWORK.setValue(24)
        self.progressBar_NETWORK.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.progressBar_NETWORK)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(12, 12))

        self.gridLayout_3.addWidget(self.pushButton, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText("")
    # retranslateUi

