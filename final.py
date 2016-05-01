import sys
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog

from gui import Ui_MainWindow

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #buttons
        self.ui.browsebutton.clicked.connect(self.set_directory)
        self.ui.clearbutton.clicked.connect(self.clear_directory)
        
    def set_directory(self):
        self.ui.directorybox.clear()
        self.ui.directorybox.setText(QFileDialog.getExistingDirectory())
        self.display_scripts()
	
    def clear_directory(self):
        self.ui.scriptlist.clear()
        self.ui.directorybox.clear()
        
    def display_scripts(self):
        self.ui.scriptlist.clear()
        path = self.ui.directorybox.text()
        os.chdir(path)
        filelist = os.listdir()
        
        for i in filelist:
            if(i.endswith('.py')):
                self.ui.scriptlist.append(i)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
