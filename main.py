# please use snake case
# avoid repeating code
import csv
import os
import sys
import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QSlider , QColorDialog, QAction, QTextEdit
from PyQt5.QtCore import QTimer,Qt, QPointF
from PyQt5.QtGui import QColor, QIcon, QCursor, QKeySequence
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QProgressBar, QDialog, QVBoxLayout
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import viewer
from classes import *
from task2 import Ui_MainWindow

MAX_SAMPLES = 3000
  
class SamplingStudioApp(QMainWindow):
  def __init__(self):
    super().__init__()
    # Set up the UI
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)  

    # for deleted signal/empty Graph
    self.signal_deleted = False
    self.graph_empty = True

    self.browsed_signal = SampledSignal()
    self.viewer_original_signal = Signal()
    self.interpolated_signal = Signal()

    # initialize graph objects array/dict
    self.plotter_window_dict = {
                                "Primary1": PlotterWindow(self.ui.primary_plot.plot()),
                                "Primary2": PlotterWindow(self.ui.primary_plot.plot()),
                                "Primary3": PlotterWindow(self.ui.primary_plot.plot()),
                                "Secondary": PlotterWindow(self.ui.reconstructed_plot.plot()),
                                "Error": PlotterWindow(self.ui.error_plot.plot())
                                # "Sinusoid": PlotterWindow(self.sinusoidalSignal.plot()),
                                # "Summed": PlotterWindow(self.summedSignal.plot())
                               }
    ''' 
    Primary1 is the original signal\n
    Primary2 is the resampled points \n
    Primary3 is the upsampled/interpolated signal\n
    '''

    #mouse
    self.ui.primary_plot.setMouseEnabled(x=False, y=False)
    self.ui.reconstructed_plot.setMouseEnabled(x=False, y=False)
    self.ui.error_plot.setMouseEnabled(x=False, y=False)

    self.ui.clear_btn.clicked.connect(lambda: viewer.clear(self))
    self.ui.import_btn.clicked.connect(lambda: viewer.browse(self))

    # Sampling frequency control
    self.ui.sampling_slider.setMinimum(1)
    self.ui.sampling_slider.valueChanged.connect(lambda: viewer.change_sampling_rate(self, self.ui.sampling_slider.value()))
    self.ui.sampling_slider.valueChanged.connect(lambda: self.ui.sampling_lcd.display(self.ui.sampling_slider.value()))

    # SNR control
    self.ui.noise_slider.setMinimum(1)
    # self.ui.noise_slider.valueChanged.connect()
    self.ui.noise_slider.valueChanged.connect(lambda: self.ui.noise_lcd.display(self.ui.noise_slider.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SamplingStudioApp()
    window.setWindowTitle("Sampling Studio")
    # app.setWindowIcon(QIcon("img/logo.png"))
    window.resize(1250,900)
    window.show()
    sys.exit(app.exec_())

