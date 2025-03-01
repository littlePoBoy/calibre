# Form implementation generated from reading ui file 'D:\pyprojects\calibre\src\calibre\gui2\dialogs\catalog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(674, 645)
        icon = QtGui.QIcon.ic("lt.png")
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.count = QtWidgets.QLabel(parent=Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.count.setFont(font)
        self.count.setObjectName("count")
        self.verticalLayout.addWidget(self.count)
        self.tabs = QtWidgets.QTabWidget(parent=Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabs.sizePolicy().hasHeightForWidth())
        self.tabs.setSizePolicy(sizePolicy)
        self.tabs.setObjectName("tabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(parent=self.tab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.format = QtWidgets.QComboBox(parent=self.tab)
        self.format.setObjectName("format")
        self.gridLayout_2.addWidget(self.format, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.tab)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.title = QtWidgets.QLineEdit(parent=self.tab)
        self.title.setObjectName("title")
        self.gridLayout_2.addWidget(self.title, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 1, 1, 1)
        self.sync = QtWidgets.QCheckBox(parent=self.tab)
        self.sync.setObjectName("sync")
        self.gridLayout_2.addWidget(self.sync, 2, 0, 1, 2)
        self.add_to_library = QtWidgets.QCheckBox(parent=self.tab)
        self.add_to_library.setObjectName("add_to_library")
        self.gridLayout_2.addWidget(self.add_to_library, 3, 0, 1, 3)
        self.tabs.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabs)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Apply|QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Help|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.format)
        self.label_2.setBuddy(self.title)

        self.retranslateUi(Dialog)
        self.tabs.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(_("Generate catalog"))
        self.count.setText(_("Generate catalog for {0} books"))
        self.label.setText(_("Catalo&g format:"))
        self.label_2.setText(_("Catalog &title (existing catalog with the same title will be replaced):"))
        self.sync.setText(_("&Send catalog to device automatically"))
        self.add_to_library.setToolTip(_("Add the catalog to your calibre library after it is generated.\n"
"Note that if you disable adding of the catalog to the library\n"
"automatic sending of the catalog to the device will not work."))
        self.add_to_library.setText(_("&Add catalog to library"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), _("Catalog options"))
