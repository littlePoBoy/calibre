# Form implementation generated from reading ui file 'D:\pyprojects\calibre\src\calibre\gui2\convert\regex_builder.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_RegexBuilder(object):
    def setupUi(self, RegexBuilder):
        RegexBuilder.setObjectName("RegexBuilder")
        RegexBuilder.resize(882, 605)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(RegexBuilder)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(parent=RegexBuilder)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.regex = QtWidgets.QLineEdit(parent=RegexBuilder)
        self.regex.setClearButtonEnabled(True)
        self.regex.setObjectName("regex")
        self.horizontalLayout.addWidget(self.regex)
        self.test = QtWidgets.QPushButton(parent=RegexBuilder)
        self.test.setObjectName("test")
        self.horizontalLayout.addWidget(self.test)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=RegexBuilder)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.occurrences = QtWidgets.QLabel(parent=RegexBuilder)
        self.occurrences.setObjectName("occurrences")
        self.horizontalLayout_5.addWidget(self.occurrences)
        spacerItem = QtWidgets.QSpacerItem(298, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=RegexBuilder)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.previous = QtWidgets.QPushButton(parent=RegexBuilder)
        self.previous.setEnabled(False)
        self.previous.setObjectName("previous")
        self.horizontalLayout_3.addWidget(self.previous)
        self.next = QtWidgets.QPushButton(parent=RegexBuilder)
        self.next.setEnabled(False)
        self.next.setObjectName("next")
        self.horizontalLayout_3.addWidget(self.next)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.groupBox = QtWidgets.QGroupBox(parent=RegexBuilder)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.preview = QtWidgets.QPlainTextEdit(parent=self.groupBox)
        self.preview.setUndoRedoEnabled(False)
        self.preview.setReadOnly(True)
        self.preview.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.preview.setObjectName("preview")
        self.verticalLayout.addWidget(self.preview)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(328, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.button_box = QtWidgets.QDialogButtonBox(parent=RegexBuilder)
        self.button_box.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.button_box.setObjectName("button_box")
        self.horizontalLayout_4.addWidget(self.button_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(RegexBuilder)
        self.button_box.rejected.connect(RegexBuilder.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(RegexBuilder)

    def retranslateUi(self, RegexBuilder):

        RegexBuilder.setWindowTitle(_("Regex builder"))
        self.label.setText(_("Regex:"))
        self.test.setText(_("&Test"))
        self.label_3.setText(_("Occurrences:"))
        self.occurrences.setText(_("0"))
        self.label_2.setText(_("Goto:"))
        self.previous.setText(_("&Previous"))
        self.next.setText(_("&Next"))
        self.groupBox.setTitle(_("Preview"))
