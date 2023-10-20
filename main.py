# please use snake case
# avoid repeating code
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import csv
import numpy as np
# from task2 import Ui_MainWindow

class SamplingStudioApp(QMainWindow):
    def __init__(self):
      super().__init__()
      # Set up the UI
      # self.ui = Ui_MainWindow()
      # self.ui.setupUi(self)  
      uic.loadUi('GUI.ui', self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SamplingStudioApp()
    window.setWindowTitle("Sampling Studio")
    window.show()
    sys.exit(app.exec_())