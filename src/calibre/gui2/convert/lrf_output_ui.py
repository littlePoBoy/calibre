# Form implementation generated from reading ui file 'D:\pyprojects\calibre\src\calibre\gui2\convert\lrf_output.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(588, 481)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.opt_autorotation = QtWidgets.QCheckBox(parent=Form)
        self.opt_autorotation.setObjectName("opt_autorotation")
        self.verticalLayout.addWidget(self.opt_autorotation)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.opt_wordspace = QtWidgets.QDoubleSpinBox(parent=Form)
        self.opt_wordspace.setDecimals(1)
        self.opt_wordspace.setMinimum(1.0)
        self.opt_wordspace.setMaximum(20.0)
        self.opt_wordspace.setProperty("value", 2.5)
        self.opt_wordspace.setObjectName("opt_wordspace")
        self.horizontalLayout.addWidget(self.opt_wordspace)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.opt_minimum_indent = QtWidgets.QDoubleSpinBox(parent=Form)
        self.opt_minimum_indent.setDecimals(1)
        self.opt_minimum_indent.setObjectName("opt_minimum_indent")
        self.horizontalLayout.addWidget(self.opt_minimum_indent)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.opt_render_tables_as_images = QtWidgets.QCheckBox(parent=Form)
        self.opt_render_tables_as_images.setObjectName("opt_render_tables_as_images")
        self.verticalLayout.addWidget(self.opt_render_tables_as_images)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.opt_text_size_multiplier_for_rendered_tables = QtWidgets.QDoubleSpinBox(parent=Form)
        self.opt_text_size_multiplier_for_rendered_tables.setObjectName("opt_text_size_multiplier_for_rendered_tables")
        self.horizontalLayout_2.addWidget(self.opt_text_size_multiplier_for_rendered_tables)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.opt_header = QtWidgets.QCheckBox(parent=Form)
        self.opt_header.setObjectName("opt_header")
        self.gridLayout.addWidget(self.opt_header, 0, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 2)
        self.opt_header_separation = QtWidgets.QDoubleSpinBox(parent=Form)
        self.opt_header_separation.setDecimals(1)
        self.opt_header_separation.setObjectName("opt_header_separation")
        self.gridLayout.addWidget(self.opt_header_separation, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.opt_header_format = QtWidgets.QLineEdit(parent=Form)
        self.opt_header_format.setClearButtonEnabled(True)
        self.opt_header_format.setObjectName("opt_header_format")
        self.gridLayout.addWidget(self.opt_header_format, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.opt_serif_family = FontFamilyChooser(parent=self.groupBox)
        self.opt_serif_family.setObjectName("opt_serif_family")
        self.gridLayout_2.addWidget(self.opt_serif_family, 0, 1, 1, 1)
        self.opt_sans_family = FontFamilyChooser(parent=self.groupBox)
        self.opt_sans_family.setObjectName("opt_sans_family")
        self.gridLayout_2.addWidget(self.opt_sans_family, 1, 1, 1, 1)
        self.opt_mono_family = FontFamilyChooser(parent=self.groupBox)
        self.opt_mono_family.setObjectName("opt_mono_family")
        self.gridLayout_2.addWidget(self.opt_mono_family, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label.setBuddy(self.opt_wordspace)
        self.label_2.setBuddy(self.opt_minimum_indent)
        self.label_4.setBuddy(self.opt_header_separation)
        self.label_5.setBuddy(self.opt_header_format)
        self.label_6.setBuddy(self.opt_serif_family)
        self.label_7.setBuddy(self.opt_sans_family)
        self.label_8.setBuddy(self.opt_mono_family)

        self.retranslateUi(Form)
        self.opt_render_tables_as_images.toggled['bool'].connect(self.opt_text_size_multiplier_for_rendered_tables.setEnabled) # type: ignore
        self.opt_header.toggled['bool'].connect(self.opt_header_separation.setEnabled) # type: ignore
        self.opt_header.toggled['bool'].connect(self.opt_header_format.setEnabled) # type: ignore
        self.opt_render_tables_as_images.toggled['bool'].connect(self.label_3.setEnabled) # type: ignore
        self.opt_header.toggled['bool'].connect(self.label_4.setEnabled) # type: ignore
        self.opt_header.toggled['bool'].connect(self.label_5.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(_("Form"))
        self.opt_autorotation.setText(_("Enable &auto-rotation of wide images"))
        self.label.setText(_("&Wordspace:"))
        self.opt_wordspace.setSuffix(_(" pt"))
        self.label_2.setText(_("Minimum para. &indent:"))
        self.opt_minimum_indent.setSuffix(_(" pt"))
        self.opt_render_tables_as_images.setText(_("Render &tables as images"))
        self.label_3.setText(_("Text size multiplier for text in rendered tables:"))
        self.opt_header.setText(_("Add &header"))
        self.label_4.setText(_("Header &separation:"))
        self.opt_header_separation.setSuffix(_(" pt"))
        self.label_5.setText(_("Header &format:"))
        self.groupBox.setTitle(_("&Embed fonts"))
        self.label_6.setText(_("&Serif font family:"))
        self.label_7.setText(_("S&ans-serif font family:"))
        self.label_8.setText(_("&Monospace font family:"))
from calibre.gui2.font_family_chooser import FontFamilyChooser
