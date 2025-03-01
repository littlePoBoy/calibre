# Form implementation generated from reading ui file 'D:\pyprojects\calibre\src\calibre\gui2\dialogs\quickview.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Quickview(object):
    def setupUi(self, Quickview):
        Quickview.setObjectName("Quickview")
        Quickview.resize(768, 342)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Quickview.sizePolicy().hasHeightForWidth())
        Quickview.setSizePolicy(sizePolicy)
        self.main_grid_layout = QtWidgets.QGridLayout(Quickview)
        self.main_grid_layout.setObjectName("main_grid_layout")
        self.items_label = QtWidgets.QLabel(parent=Quickview)
        self.items_label.setObjectName("items_label")
        self.main_grid_layout.addWidget(self.items_label, 0, 0, 1, 1)
        self.items = QtWidgets.QListWidget(parent=Quickview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.items.sizePolicy().hasHeightForWidth())
        self.items.setSizePolicy(sizePolicy)
        self.items.setObjectName("items")
        self.main_grid_layout.addWidget(self.items, 1, 0, 1, 1)
        self.books_label = QtWidgets.QLabel(parent=Quickview)
        self.books_label.setObjectName("books_label")
        self.main_grid_layout.addWidget(self.books_label, 0, 1, 1, 1)
        self.books_table = QtWidgets.QTableWidget(parent=Quickview)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.books_table.sizePolicy().hasHeightForWidth())
        self.books_table.setSizePolicy(sizePolicy)
        self.books_table.setColumnCount(0)
        self.books_table.setRowCount(0)
        self.books_table.setObjectName("books_table")
        self.main_grid_layout.addWidget(self.books_table, 1, 1, 1, 1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        spacerItem = QtWidgets.QSpacerItem(200, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.apply_vls = QtWidgets.QCheckBox(parent=Quickview)
        self.apply_vls.setObjectName("apply_vls")
        self.hboxlayout.addWidget(self.apply_vls)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.lock_qv = QtWidgets.QCheckBox(parent=Quickview)
        self.lock_qv.setObjectName("lock_qv")
        self.hboxlayout.addWidget(self.lock_qv)
        self.refresh_button = QtWidgets.QPushButton(parent=Quickview)
        self.refresh_button.setAutoDefault(False)
        self.refresh_button.setObjectName("refresh_button")
        self.hboxlayout.addWidget(self.refresh_button)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hboxlayout.addItem(spacerItem2)
        self.dock_button = QtWidgets.QPushButton(parent=Quickview)
        self.dock_button.setAutoDefault(False)
        self.dock_button.setObjectName("dock_button")
        self.hboxlayout.addWidget(self.dock_button)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hboxlayout.addItem(spacerItem3)
        self.close_button = QtWidgets.QPushButton(parent=Quickview)
        self.close_button.setAutoDefault(False)
        self.close_button.setObjectName("close_button")
        self.hboxlayout.addWidget(self.close_button)
        spacerItem4 = QtWidgets.QSpacerItem(200, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.hboxlayout.addItem(spacerItem4)
        self.main_grid_layout.addLayout(self.hboxlayout, 3, 0, 1, 2)
        self.items_label.setBuddy(self.items)
        self.books_label.setBuddy(self.books_table)

        self.retranslateUi(Quickview)

    def retranslateUi(self, Quickview):

        Quickview.setWindowTitle(_("Quickview"))
        self.apply_vls.setText(_("&Apply Virtual libraries"))
        self.apply_vls.setToolTip(_("<p>Select to make Quickview show only books in the current\n"
"        Virtual library</p>"))
        self.lock_qv.setText(_("&Lock Quickview contents"))
        self.lock_qv.setToolTip(_("<p>Select to prevent Quickview from changing content when the\n"
"        selection on the library view is changed</p>"))
        self.refresh_button.setText(_("&Refresh"))
        self.refresh_button.setToolTip(_("When Quickview is locked, refresh the window using the last selected book and that book\'s value in the last selected column."))
        self.dock_button.setText(_("&Dock"))
        self.close_button.setText(_("&Close"))
