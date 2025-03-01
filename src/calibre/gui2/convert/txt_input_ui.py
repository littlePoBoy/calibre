# Form implementation generated from reading ui file 'D:\pyprojects\calibre\src\calibre\gui2\convert\txt_input.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(588, 399)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.opt_paragraph_type = QtWidgets.QComboBox(parent=self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opt_paragraph_type.sizePolicy().hasHeightForWidth())
        self.opt_paragraph_type.setSizePolicy(sizePolicy)
        self.opt_paragraph_type.setObjectName("opt_paragraph_type")
        self.gridLayout.addWidget(self.opt_paragraph_type, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.opt_formatting_type = QtWidgets.QComboBox(parent=self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opt_formatting_type.sizePolicy().hasHeightForWidth())
        self.opt_formatting_type.setSizePolicy(sizePolicy)
        self.opt_formatting_type.setObjectName("opt_formatting_type")
        self.gridLayout.addWidget(self.opt_formatting_type, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.opt_preserve_spaces = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.opt_preserve_spaces.setObjectName("opt_preserve_spaces")
        self.verticalLayout_2.addWidget(self.opt_preserve_spaces)
        self.opt_txt_in_remove_indents = QtWidgets.QCheckBox(parent=self.groupBox_2)
        self.opt_txt_in_remove_indents.setObjectName("opt_txt_in_remove_indents")
        self.verticalLayout_2.addWidget(self.opt_txt_in_remove_indents)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.markdown_box = QtWidgets.QGroupBox(parent=Form)
        self.markdown_box.setObjectName("markdown_box")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.markdown_box)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.markdown_box)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(parent=self.markdown_box)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.opt_markdown_extensions = QtWidgets.QListWidget(parent=self.markdown_box)
        self.opt_markdown_extensions.setObjectName("opt_markdown_extensions")
        self.verticalLayout.addWidget(self.opt_markdown_extensions)
        self.label_5 = QtWidgets.QLabel(parent=self.markdown_box)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayout_3.addWidget(self.markdown_box)
        self.label_2.setBuddy(self.opt_paragraph_type)
        self.label_3.setBuddy(self.opt_formatting_type)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.groupBox_3.setTitle(_("Structure"))
        self.label_2.setText(_("&Paragraph style:"))
        self.label_3.setText(_("&Formatting style:"))
        self.groupBox_2.setTitle(_("Common"))
        self.opt_preserve_spaces.setText(_("Preserve &spaces"))
        self.opt_txt_in_remove_indents.setText(_("Remove &indents at the beginning of lines"))
        self.markdown_box.setTitle(_("Markdown"))
        self.label.setText(_("<p>Markdown is a simple markup language for text files, that allows for advanced formatting. To learn more visit <a href=\"https://daringfireball.net/projects/markdown\">Markdown</a>."))
        self.label_4.setText(_("You can optionally enable various extensions to the base Markdown syntax, below."))
        self.label_5.setText(_("More information on <a href=\"https://python-markdown.github.io/extensions/\">Markdown extensions</a>"))
