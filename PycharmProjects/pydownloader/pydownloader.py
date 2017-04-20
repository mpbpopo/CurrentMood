from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import urllib.request

class Downloader(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        """adding self in front of url makes the input an instance-wide variable"""
        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")
        browse = QPushButton("Browse")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File Save Location")

        self.progress.setValue(0)
        """First usage of QT.Core import"""
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)


        self.setLayout(layout)

        self.setWindowTitle("PyDownloader")
        self.setFocus()

        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse_file)

    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save File As", directory=".",
                                                filter="All Files (*.*)")
        self.save_location.setText(QDir.toNativeSeperators(save_file))

    """The handler (aka slot) for our event"""
    """The download method"""
    def download(self):
        """ the "text" in self.url.text is collecting the text that was entered into self.url"""
        url = self.url.text()
        save_location = self.save_location.text()
        """wrapping the function in error handling"""
        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The download failed")
            return

        """Notification box that the download is complere"""
        QMessageBox.information(self, "Information", "The download is complete")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")




    """The report method"""
    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.progress.setValue(int(percent))




app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()

"""Summary of pluralsight dialog
"""
