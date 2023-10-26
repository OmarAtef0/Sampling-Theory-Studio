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
import composer
MAX_SAMPLES = 3000
NUM_OF_POINTS = 3000
  
class SamplingStudioApp(QMainWindow):
  def __init__(self):
    super().__init__()
    # Set up the UI
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)  

    # for deleted signal/empty Graph
    self.graph_empty = True
    self.browsed_signal = SampledSignal()
    self.current_signal = Signal()
    self.interpolated_signal = Signal()

    self.sinusoidal_index = 0
    self.sinusoidal_number = 1
    self.sinusoidals_list = []
    self.ui.sinusoidals_signals_menu.addItem("Signal " + str(self.sinusoidal_number))

    # initialize graph objects array/dict
    self.plots_dict = {
                        "Primary": self.ui.primary_plot.plot(),
                        "Secondary1": self.ui.primary_plot.plot(),
                        "Secondary2": self.ui.reconstructed_plot.plot(),
                        "Error": self.ui.error_plot.plot(),
                        "Sinusoidal": self.ui.sinusoidal_secondary_plot_widget.plot(),
                        "Summed": self.ui.sinusoidal_main_plot_widget.plot()
                        }
    
    ''' 
    Primary1 is the original signal
    Secondary1 is the resampled points 
    Secondary2 is the reconstructed signal
    '''

    #mouse
    self.ui.primary_plot.setMouseEnabled(x=False, y=False)
    self.ui.reconstructed_plot.setMouseEnabled(x=False, y=False)
    self.ui.error_plot.setMouseEnabled(x=False, y=False)

    self.ui.clear_btn.clicked.connect(lambda: viewer.clear(self))
    self.ui.import_btn.clicked.connect(lambda: viewer.browse(self))

    # Sampling frequency control
    self.ui.sampling_slider.setMinimum(self.current_signal.max_analog_freq)
    self.ui.sampling_slider.valueChanged.connect(lambda: viewer.change_sampling_rate(self, self.ui.sampling_slider.value()))
    self.ui.sampling_slider.valueChanged.connect(lambda: self.ui.sampling_lcd.display(self.ui.sampling_slider.value()))

    # SNR control
    self.ui.noise_slider.setMinimum(1)
    # self.ui.noise_slider.valueChanged.connect()
    self.ui.noise_slider.valueChanged.connect(lambda: self.ui.noise_lcd.display(self.ui.noise_slider.value()))

    # Sinsusoidal_Sliders
    self.ui.sinusoidal_frequency_slider.valueChanged.connect(lambda: composer.plot_sinusoidal_wave(self))
    self.ui.sinusoidal_frequency_slider.valueChanged.connect(lambda: self.ui.sinusoidal_frequency_LCD.display(self.ui.sinusoidal_frequency_slider.value()))
    
    self.ui.sinusoidal_amplitude_slider.valueChanged.connect(lambda: composer.plot_sinusoidal_wave(self))
    self.ui.sinusoidal_amplitude_slider.valueChanged.connect(lambda: self.ui.sinusoidal_amplitude_LCD.display(self.ui.sinusoidal_amplitude_slider.value()))
    
    self.ui.sinusoidal_phase_slider.valueChanged.connect(lambda: composer.plot_sinusoidal_wave(self))
    self.ui.sinusoidal_phase_slider.valueChanged.connect(lambda: self.ui.sinusoidal_phase_LCD.display(self.ui.sinusoidal_phase_slider.value()))

    self.ui.add_sinusoidal_button.clicked.connect(lambda: composer.add_sinusoidal_wave(self))
    self.ui.sinusoidals_signals_menu.currentIndexChanged.connect(lambda: composer.update_sinusoidal_menubar(self, 
                                                                                            self.ui.sinusoidals_signals_menu.currentIndex()))
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SamplingStudioApp()
    window.setWindowTitle("Sampling Studio")
    # app.setWindowIcon(QIcon("img/logo.png"))
    window.resize(1250,900)
    window.show()
    sys.exit(app.exec_())

