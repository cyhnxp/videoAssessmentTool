# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assessmentTool.ui'
#
# Created: Sun Jul 29 11:18:14 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import random
import sys
from PyQt4 import QtCore, QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_main(QtGui.QFrame):
    def __init__(self):
        super(Ui_main,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, main):
        main.setObjectName(_fromUtf8("main"))
        main.setWindowModality(QtCore.Qt.NonModal)
        main.resize(1123, 820)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        main.setLayoutDirection(QtCore.Qt.LeftToRight)
        main.setFrameShape(QtGui.QFrame.StyledPanel)
        main.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.top = QtGui.QFrame(main)
        self.top.setAutoFillBackground(False)
        self.top.setStyleSheet(_fromUtf8(""))
        self.top.setFrameShape(QtGui.QFrame.StyledPanel)
        self.top.setFrameShadow(QtGui.QFrame.Raised)
        self.top.setObjectName(_fromUtf8("top"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.top)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.title = QtGui.QLabel(self.top)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.horizontalLayout.addWidget(self.title)
        self.verticalLayout.addWidget(self.top)
        self.bottom = QtGui.QFrame(main)
        self.bottom.setAutoFillBackground(False)
        self.bottom.setStyleSheet(_fromUtf8(""))
        self.bottom.setFrameShape(QtGui.QFrame.StyledPanel)
        self.bottom.setFrameShadow(QtGui.QFrame.Raised)
        self.bottom.setObjectName(_fromUtf8("bottom"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.bottom)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.left = QtGui.QFrame(self.bottom)
        self.left.setStyleSheet(_fromUtf8(""))
        self.left.setFrameShape(QtGui.QFrame.StyledPanel)
        self.left.setFrameShadow(QtGui.QFrame.Raised)
        self.left.setObjectName(_fromUtf8("left"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.left)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.button_frame = QtGui.QFrame(self.left)
        self.button_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.button_frame.setObjectName(_fromUtf8("button_frame"))
        self.import_button = QtGui.QPushButton(self.button_frame)
        self.import_button.setGeometry(QtCore.QRect(30, 10, 111, 41))
        self.import_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.import_button.setAutoDefault(False)
        self.import_button.setDefault(False)
        self.import_button.setFlat(False)
        self.import_button.setObjectName(_fromUtf8("import_button"))
        self.check_button = QtGui.QPushButton(self.button_frame)
        self.check_button.setGeometry(QtCore.QRect(160, 10, 111, 41))
        self.check_button.setObjectName(_fromUtf8("check_button"))
        self.estimate_button = QtGui.QPushButton(self.button_frame)
        self.estimate_button.setGeometry(QtCore.QRect(290, 10, 111, 41))
        self.estimate_button.setObjectName(_fromUtf8("estimate_button"))


        self.verticalLayout_2.addWidget(self.button_frame)
        self.table_frame = QtGui.QFrame(self.left)
        self.table_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.table_frame.setObjectName(_fromUtf8("table_frame"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.table_frame)
        self.verticalLayout_7.setContentsMargins(30, 0, 20, 20)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.table_frame_1 = QtGui.QFrame(self.table_frame)
        self.table_frame_1.setStyleSheet(_fromUtf8("background-color:rgb(231, 196, 255)"))
        self.table_frame_1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.table_frame_1.setFrameShadow(QtGui.QFrame.Raised)
        self.table_frame_1.setObjectName(_fromUtf8("table_frame_1"))
        self.verticalLayout_7.addWidget(self.table_frame_1)
        self.verticalLayout_2.addWidget(self.table_frame)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 12)
        self.horizontalLayout_5.addWidget(self.left)
        self.right = QtGui.QFrame(self.bottom)
        self.right.setStyleSheet(_fromUtf8(""))
        self.right.setFrameShape(QtGui.QFrame.StyledPanel)
        self.right.setFrameShadow(QtGui.QFrame.Raised)
        self.right.setObjectName(_fromUtf8("right"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.right)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.right_top = QtGui.QFrame(self.right)
        self.right_top.setFrameShape(QtGui.QFrame.StyledPanel)
        self.right_top.setFrameShadow(QtGui.QFrame.Raised)
        self.right_top.setObjectName(_fromUtf8("right_top"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.right_top)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.point_frame = QtGui.QFrame(self.right_top)
        self.point_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.point_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.point_frame.setObjectName(_fromUtf8("point_frame"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.point_frame)
        self.verticalLayout_5.setContentsMargins(40, 115, 34, 10)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.point_table = QtGui.QTableWidget(self.point_frame)
        self.point_table.setFrameShape(QtGui.QFrame.StyledPanel)
        self.point_table.setFrameShadow(QtGui.QFrame.Sunken)
        self.point_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.point_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.point_table.setAutoScroll(True)
        self.point_table.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
        self.point_table.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.point_table.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.point_table.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.point_table.setRowCount(2)
        self.point_table.setColumnCount(5)
        self.point_table.setObjectName(_fromUtf8("point_table"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.point_table.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.point_table.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.point_table.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.point_table.setItem(1, 2, item)
        self.point_table.horizontalHeader().setVisible(False)
        self.point_table.horizontalHeader().setDefaultSectionSize(89)
        self.point_table.verticalHeader().setVisible(False)
        self.point_table.verticalHeader().setDefaultSectionSize(49)
        self.verticalLayout_5.addWidget(self.point_table)
        self.verticalLayout_4.addWidget(self.point_frame)
        self.tps_frame = QtGui.QFrame(self.right_top)
        self.tps_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tps_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.tps_frame.setObjectName(_fromUtf8("tps_frame"))
        self.max_tps = QtGui.QTableWidget(self.tps_frame)
        self.max_tps.setGeometry(QtCore.QRect(41, 0, 222, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max_tps.sizePolicy().hasHeightForWidth())
        self.max_tps.setSizePolicy(sizePolicy)
        self.max_tps.setFrameShape(QtGui.QFrame.StyledPanel)
        self.max_tps.setFrameShadow(QtGui.QFrame.Sunken)
        self.max_tps.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.max_tps.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.max_tps.setAutoScroll(True)
        self.max_tps.setAutoScrollMargin(0)
        self.max_tps.setEditTriggers(QtGui.QAbstractItemView.SelectedClicked)
        self.max_tps.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.max_tps.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.max_tps.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.max_tps.setRowCount(1)
        self.max_tps.setColumnCount(2)
        self.max_tps.setObjectName(_fromUtf8("max_tps"))
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.max_tps.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.max_tps.setItem(0, 1, item)
        self.max_tps.horizontalHeader().setVisible(False)
        self.max_tps.horizontalHeader().setDefaultSectionSize(110)
        self.max_tps.horizontalHeader().setMinimumSectionSize(0)
        self.max_tps.verticalHeader().setVisible(False)
        self.max_tps.verticalHeader().setDefaultSectionSize(44)
        self.max_tps.verticalHeader().setMinimumSectionSize(0)
        self.verticalLayout_4.addWidget(self.tps_frame)
        self.verticalLayout_4.setStretch(0, 3)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.right_top)
        self.right_bottom = QtGui.QFrame(self.right)
        self.right_bottom.setFrameShape(QtGui.QFrame.StyledPanel)
        self.right_bottom.setFrameShadow(QtGui.QFrame.Raised)
        self.right_bottom.setObjectName(_fromUtf8("right_bottom"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.right_bottom)

        self.verticalLayout_6.setContentsMargins(20, 0, 20, 60)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.line_chart_frame = QtGui.QFrame(self.right_bottom)
        self.line_chart_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.line_chart_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.line_chart_frame.setObjectName(_fromUtf8("line_chart_frame"))


        #图表
        self.figure = plt.figure(facecolor='#F0F0FF')
        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)



        layout = QtGui.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)
        self.line_chart_frame.setLayout(layout)
        self.estimate_button.clicked.connect(self.plot)

        self.verticalLayout_6.addWidget(self.line_chart_frame)
        self.verticalLayout_3.addWidget(self.right_bottom)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 3)
        self.horizontalLayout_5.addWidget(self.right)
        self.horizontalLayout_5.setStretch(0, 9)
        self.horizontalLayout_5.setStretch(1, 9)
        self.verticalLayout.addWidget(self.bottom)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 15)


        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)
        main.setTabOrder(self.check_button, self.estimate_button)
        main.setTabOrder(self.estimate_button, self.import_button)

    def retranslateUi(self, main):
        main.setWindowTitle(_translate("main", "混合业务性能评估工具", None))
        self.title.setText(_translate("main", "混合业务性能评估工具", None))
        self.import_button.setText(_translate("main", "导入比例", None))
        self.check_button.setText(_translate("main", "检验比例", None))
        self.estimate_button.setText(_translate("main", "预估模型", None))
        __sortingEnabled = self.point_table.isSortingEnabled()
        self.point_table.setSortingEnabled(False)
        item = self.point_table.item(0, 0)
        item.setText(_translate("main", "TPS", None))
        item = self.point_table.item(1, 0)
        item.setText(_translate("main", "CPU占用率", None))
        self.point_table.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.max_tps.isSortingEnabled()
        self.max_tps.setSortingEnabled(False)
        item = self.max_tps.item(0, 0)
        item.setText(_translate("main", "最大TPS", None))
        self.max_tps.setSortingEnabled(__sortingEnabled)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        data = [random.random()*100 for i in range(7)]

        group_labels = ['0', '50','100','150','200','250','300']
        # create an axis
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.hold(False)

        # plot data
        ax.plot(data, '*-')
        ax.set_xticklabels(group_labels)
        ax.set_title(_translate("main", "CPU占用率", None),{'fontname':'STKaiti'})
        ax.set_xlabel(_translate("main", "TPS", None),{'fontname':'STKaiti'})
        ax.set_ylabel(_translate("main", "占用率(%)", None),{'fontname':'STKaiti'})
        # refresh canvas
        ax.grid()
        self.canvas.draw()



if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    reload(sys)
    sys.setdefaultencoding('utf8')
    win=Ui_main()
    win.show()
    sys.exit(app.exec_())