# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Demo_v4.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1857, 1037)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1851, 1021))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setMinimumSize(QtCore.QSize(0, 0))
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1854, 991))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.middle = QtWidgets.QGridLayout()
        self.middle.setContentsMargins(2, 2, 2, 2)
        self.middle.setSpacing(2)
        self.middle.setObjectName("middle")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.far_demo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.far_demo.setMinimumSize(QtCore.QSize(476, 270))
        self.far_demo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.far_demo.setAlignment(QtCore.Qt.AlignCenter)
        self.far_demo.setOpenExternalLinks(False)
        self.far_demo.setObjectName("far_demo")
        self.horizontalLayout_2.addWidget(self.far_demo)
        self.blood = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.blood.setMinimumSize(QtCore.QSize(320, 270))
        self.blood.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.blood.setAlignment(QtCore.Qt.AlignCenter)
        self.blood.setObjectName("blood")
        self.horizontalLayout_2.addWidget(self.blood)
        self.hero_demo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.hero_demo.setMinimumSize(QtCore.QSize(320, 270))
        self.hero_demo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hero_demo.setAlignment(QtCore.Qt.AlignCenter)
        self.hero_demo.setObjectName("hero_demo")
        self.horizontalLayout_2.addWidget(self.hero_demo)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.middle.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.left_demo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.left_demo.setMinimumSize(QtCore.QSize(146, 693))
        self.left_demo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_demo.setAlignment(QtCore.Qt.AlignCenter)
        self.left_demo.setObjectName("left_demo")
        self.horizontalLayout_4.addWidget(self.left_demo)
        self.main_demo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.main_demo.setMinimumSize(QtCore.QSize(1170, 693))
        self.main_demo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_demo.setAlignment(QtCore.Qt.AlignCenter)
        self.main_demo.setObjectName("main_demo")
        self.horizontalLayout_4.addWidget(self.main_demo)
        self.right_demo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.right_demo.setMinimumSize(QtCore.QSize(146, 693))
        self.right_demo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_demo.setAlignment(QtCore.Qt.AlignCenter)
        self.right_demo.setObjectName("right_demo")
        self.horizontalLayout_4.addWidget(self.right_demo)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 8)
        self.horizontalLayout_4.setStretch(2, 1)
        self.middle.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.middle.setRowStretch(0, 7)
        self.horizontalLayout.addLayout(self.middle)
        self.right = QtWidgets.QVBoxLayout()
        self.right.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.right.setContentsMargins(5, 5, 5, 5)
        self.right.setSpacing(5)
        self.right.setObjectName("right")
        self.map = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.map.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.map.sizePolicy().hasHeightForWidth())
        self.map.setSizePolicy(sizePolicy)
        self.map.setMinimumSize(QtCore.QSize(320, 718))
        self.map.setMaximumSize(QtCore.QSize(320, 16777215))
        self.map.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.map.setAlignment(QtCore.Qt.AlignCenter)
        self.map.setObjectName("map")
        self.right.addWidget(self.map, 0, QtCore.Qt.AlignHCenter)
        self.condition = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.condition.setMinimumSize(QtCore.QSize(355, 73))
        self.condition.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.condition.setAlignment(QtCore.Qt.AlignCenter)
        self.condition.setObjectName("condition")
        self.right.addWidget(self.condition)
        self.ChangeView = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ChangeView.setMinimumSize(QtCore.QSize(115, 30))
        self.ChangeView.setObjectName("ChangeView")
        self.right.addWidget(self.ChangeView)
        self.ShowLidar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ShowLidar.setMinimumSize(QtCore.QSize(115, 30))
        self.ShowLidar.setObjectName("ShowLidar")
        self.right.addWidget(self.ShowLidar)
        self.record = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.record.setMinimumSize(QtCore.QSize(115, 30))
        self.record.setObjectName("record")
        self.right.addWidget(self.record)
        self.ShutDown = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ShutDown.setMinimumSize(QtCore.QSize(115, 30))
        self.ShutDown.setObjectName("ShutDown")
        self.right.addWidget(self.ShutDown)
        self.right.setStretch(0, 1)
        self.right.setStretch(1, 1)
        self.right.setStretch(2, 1)
        self.right.setStretch(3, 1)
        self.right.setStretch(4, 1)
        self.right.setStretch(5, 1)
        self.horizontalLayout.addLayout(self.right)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 1841, 971))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.epnp_begin = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.epnp_begin.setMinimumSize(QtCore.QSize(0, 35))
        self.epnp_begin.setObjectName("epnp_begin")
        self.verticalLayout.addWidget(self.epnp_begin)
        self.epnp_clear = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.epnp_clear.setMinimumSize(QtCore.QSize(0, 35))
        self.epnp_clear.setObjectName("epnp_clear")
        self.verticalLayout.addWidget(self.epnp_clear)
        self.epnp_back = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.epnp_back.setMinimumSize(QtCore.QSize(0, 35))
        self.epnp_back.setObjectName("epnp_back")
        self.verticalLayout.addWidget(self.epnp_back)
        self.epnp_next = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.epnp_next.setMinimumSize(QtCore.QSize(0, 35))
        self.epnp_next.setObjectName("epnp_next")
        self.verticalLayout.addWidget(self.epnp_next)
        self.pnp_condition = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.pnp_condition.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pnp_condition.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.pnp_condition.setObjectName("pnp_condition")
        self.verticalLayout.addWidget(self.pnp_condition)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.pnp_demo = QtWidgets.QGraphicsView(self.horizontalLayoutWidget_2)
        self.pnp_demo.setObjectName("pnp_demo")
        self.horizontalLayout_3.addWidget(self.pnp_demo)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.ChangeView.clicked.connect(MainWindow.ChangeView_on_clicked)
        self.epnp_begin.clicked.connect(MainWindow.epnp_calculate)
        self.epnp_back.clicked.connect(MainWindow.epnp_back_on_clicked)
        self.epnp_clear.clicked.connect(MainWindow.epnp_clear_on_clicked)
        self.epnp_next.clicked.connect(MainWindow.epnp_next_on_clicked)
        self.record.clicked.connect(MainWindow.record_on_clicked)
        self.ShowLidar.clicked.connect(MainWindow.showpc_on_clicked)
        self.ShutDown.clicked.connect(MainWindow.CloseProgram_on_clicked)
        self.pnp_demo.mousePressEvent = MainWindow.epnp_mouseEvent
        self.main_demo.mouseMoveEvent = MainWindow.pc_mouseEvent
        self.far_demo.mousePressEvent = MainWindow.eco_mouseEvent
        self.far_demo.keyPressEvent = MainWindow.eco_key_on_clicked
        self.condition.keyPressEvent = MainWindow.condition_key_on_clicked
        self.condition.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.far_demo.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tabWidget.currentChanged.connect(MainWindow.epnp_on_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.far_demo.setText(_translate("MainWindow", "敌方基地视角"))
        self.blood.setText(_translate("MainWindow", "血量显示界面"))
        self.hero_demo.setText(_translate("MainWindow", "三倍镜显示界面"))
        self.left_demo.setText(_translate("MainWindow", "left_demo"))
        self.main_demo.setText(_translate("MainWindow", "main_demo"))
        self.right_demo.setText(_translate("MainWindow", "right_demo"))
        self.map.setText(_translate("MainWindow", "小地图"))
        self.condition.setText(_translate("MainWindow", "雷达站运行状态"))
        self.ChangeView.setText(_translate("MainWindow", "ChangeView"))
        self.ShowLidar.setText(_translate("MainWindow", "ShowLidar"))
        self.record.setText(_translate("MainWindow", "record"))
        self.ShutDown.setText(_translate("MainWindow", "close"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "主页面"))
        self.epnp_begin.setText(_translate("MainWindow", "开始"))
        self.epnp_clear.setText(_translate("MainWindow", "清空"))
        self.epnp_back.setText(_translate("MainWindow", "back"))
        self.epnp_next.setText(_translate("MainWindow", "next"))
        self.pnp_condition.setText(_translate("MainWindow", "pnp_condion"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "EPNP"))
