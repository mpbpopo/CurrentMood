"""summary section of pluralsight class. Examples for QLineEdit, Qlabel, QCheckbox
QCombobox"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import datetime
import sys

import urllib.request
import sqlite3
connection = sqlite3.connect("allthefeels.db")
#http://www.python-course.eu/sql_python.php

cursor = connection.cursor()

class QCurrentFeels(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidgets Demo")

        self.combobox = QComboBox()

        self.combobox.addItem(" ")
        self.combobox.addItem("No pain")
        self.combobox.addItem("Medium pain")
        self.combobox.addItem("Lots of pain")
        #event called "Current Index Changed" fired when something is selected


        label = QLabel()
        label.setText("<b>Current Mood?</b>")
        #line_edit = QLineEdit()


        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.combobox)
        #layout.addWidget(line_edit)
        #layout.addWidget(self.checkbox)
        layout.addWidget(close_button)
        self.setLayout(layout)

        self.setFocus()

        self.combobox.currentIndexChanged.connect(self.selected)

    def selected(self):
        current_text = self.combobox.currentText()
        current_index = str(self.combobox.currentIndex())

        print(current_text + " at the index " + current_index)


    def selected(self):
        text_file = open('CurrentFeelsLog.txt', 'a')

        text_file.write("\n" "Mood at " + str(datetime.datetime.now()) + " was " + str(self.combobox.currentText()))

        text_file.close()

class QDatabaseDoWork():
    foo = 2

app = QApplication(sys.argv)
dl = QCurrentFeels()
dl.show()
app.exec_()

