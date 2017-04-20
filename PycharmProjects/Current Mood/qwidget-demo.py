"""summary section of pluralsight class. Examples for QLineEdit, Qlabel, QCheckbox
QCombobox"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import urllib.request


class QWidgetDemos(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidgets Demo")

        self.combobox = QComboBox()

        self.combobox.addItem("Item 1")
        self.combobox.addItem("Item 2")
        self.combobox.addItem("Item 3")
        #event called "Current Index Changed" fired when something is selected

        self.checkbox = QCheckBox()
        self.checkbox.setText("Check Me!")

        label = QLabel()
        label.setText("<b>Hello World</b>")
        line_edit = QLineEdit()

        line_edit.setText("Hello Pluralsight")
        #line_edit.setReadOnly(True) sets the line edit text box to read only
        #line_edit.setEchoMode(QLineEdit.Password) display text entered as dots like it's a password
        line_edit.selectAll()
        #line_edit.selectAll() selects all text in the field
        text = line_edit.text()
        print("You typed "  + text)


        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.combobox)
        layout.addWidget(line_edit)
        layout.addWidget(self.checkbox)
        layout.addWidget(close_button)
        self.setLayout(layout)

        self.setFocus()

        self.checkbox.stateChanged.connect(self.selected)

    def selected(self):
        if self.checkbox.isChecked():
            print("Yay")
        else:
            print("No :(")

    def selected(self):
        current_text = self.combobox.currentText()
        current_index = str(self.combobox.currentIndex())

        print(current_text + " at the index " + current_index)


app = QApplication(sys.argv)
dl = QWidgetDemos()
dl.show()
app.exec_()

