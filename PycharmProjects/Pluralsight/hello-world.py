from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
""" importing all like this could lead to global name conflicts"""

class HelloWorld(QDialog):
    """This creates a new class that then inherets from Qdialog (base class of dialog windows) class"""
    def __init__(self):

        """overrides the constructor method. Another way to override the constructor method
        super(HelloWorld, self).__init__() """
        QDialog.__init__(self)


        """grid layout will be what you use instead for more complex applications"""
        layout = QGridLayout()


        """set the elements"""

        self.label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        """add the elements to the layout. "use layouts, they are your friend." """

        layout.addWidget(self.label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(button, 1, 1)

        self.setLayout(layout)


        """button is the function, clicked is what happens, and connect attaches an event to a handler and is how you pass it into what is in the paren
        Pythonic because it uses just one line of code"""
        button.clicked.connect(self.close)
        line_edit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
        self.label.setText(text)


        """Older syntax for event handling
        self.connect(line_edit, SIGNAL("textChanged(Qstring)"), self.changeTextLabel)
        """



app = QApplication(sys.argv)

"""setting the dialog equal to our HelloWorld class"""
dialog = HelloWorld()

"""start/open the dialog"""
dialog.show()
app.exec_()

