"""summary section of pluralsight class. Examples for QLineEdit, Qlabel, QCheckbox
QCombobox"""

#http://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds-in-python

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import datetime
import sys

import urllib.request


class QWidgetDemos(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidgets Demo")

        self.comboboxmood = QComboBox()

        self.comboboxmood.addItem("Happy")
        self.comboboxmood.addItem("Sad")
        self.comboboxmood.addItem("Medium")
        #event called "Current Index Changed" fired when something is selected

        self.comboboxrank = QComboBox()

        self.comboboxrank.addItem("1")
        self.comboboxrank.addItem("2")
        self.comboboxrank.addItem("3")
        self.comboboxrank.addItem("3")
        self.comboboxrank.addItem("5")
        self.comboboxrank.addItem("6")
        self.comboboxrank.addItem("7")
        self.comboboxrank.addItem("8")
        self.comboboxrank.addItem("9")
        self.comboboxrank.addItem("10")


        moodlabel = QLabel()
        moodlabel.setText("<b>Current Mood?</b>")
        #line_edit = QLineEdit()

        ranklabel = QLabel()
        ranklabel.setText("<b>On a scale of 1-10?</b>")


        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(moodlabel)
        layout.addWidget(self.comboboxmood)
        layout.addWidget(ranklabel)
        layout.addWidget(self.comboboxrank)
        #layout.addWidget(line_edit)
        #layout.addWidget(self.checkbox)
        layout.addWidget(close_button)
        self.setLayout(layout)

        self.setFocus()

        self.comboboxmood.currentIndexChanged.connect(self.selected)

        self.comboboxrank.currentIndexChanged.connect(self.selected)

    def selected(self):
        current_mood_text = self.comboboxmood.currentText()
        current_mood_index = str(self.comboboxmood.currentIndex())

        current_rank_text = self.comboboxrank.currentText()
        current_rank_text = self.comboboxrank.currentText()


        print(current_mood_text + " at the index " + current_mood_index)

    def selected(self):
        text_file = open("CurrentMoodLog.txt", "w")

        text_file.write("Mood at " + str(datetime.datetime.now()) + " was " + str(self.comboboxmood.currentText()))

        text_file.close()


app = QApplication(sys.argv)
dl = QWidgetDemos()
dl.show()
app.exec_()

