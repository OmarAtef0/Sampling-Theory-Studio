import sys
import csv
from PyQt5 import QtWidgets , QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QSlider , QColorDialog, QAction, QTextEdit
from PyQt5.QtCore import QTimer,Qt, QPointF
from PyQt5.QtGui import QColor, QIcon, QCursor, QKeySequence
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QProgressBar, QDialog, QVBoxLayout
import pyqtgraph as pg
import numpy as np
from pyqtgraph import PlotWidget
from classes import *

# import signal from csv 
def browse(self):
    self.graph_empty = False
    self.filename = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", )
    path = self.filename[0]

    time = []
    amplitude = []
    self.fsample = 1
    
    with open(path, 'r') as csvFile:    # 'r' its a mode for reading and writing
        csvReader = csv.reader(csvFile, delimiter=',')

        # neglect the first line in the csv file
        next(csvReader)

        for line in csvReader:
            if len(time) > MAX_SAMPLES:
                break
            else:
                amplitude.append(float(line[1]))
                time.append(float(line[0]))

    self.fsample = 1 / (time[1]-time[0])   # T = (time[1]-time[0])
    self.browsed_signal = SampledSignal(self.fsample, amplitude)
    move_to_viewer(self, "browse")

def move_to_viewer(self, Input):
    if Input == "composer":
        self.current_signal = Signal(self.summed_signal.xAxis,self.summed_signal.yAxis, self.summed_signal.max_analog_freq)
        self.ui.WindowTabs.setCurrentIndex(0)

    elif Input == "browse":
        self.current_signal = Signal(self.browsed_signal.time_array,self.browsed_signal.amplitude_arr, self.browsed_signal.max_analog_freq)
        self.current_signal.get_max_freq()  
        self.ui.WindowTabs.setCurrentIndex(0)
        
    # update slider maximum to 4Fmax
    self.ui.sampling_slider.setMaximum(int(4 * self.current_signal.max_analog_freq ))
    self.ui.sampling_slider.setSingleStep(int (self.current_signal.max_analog_freq))

    # self.ui.fmaxLCD.display(self.current_signal.max_analog_freq)

    # initialize plots
    self.plots_dict["Primary"].setData(self.current_signal.time, self.current_signal.amplitude)

    self.pen = pg.mkPen(color=(0, 200, 0), width=0)
    self.plots_dict["Secondary1"].setData(self.resampled_time, self.resampled_amplitude, symbol='o', pen=self.pen)

    self.pen = pg.mkPen(color=(0, 200, 0), width=2)
    self.plots_dict["Secondary2"].setData(self.current_signal.time, self.interpolated_amplitude, pen=self.pen)

    self.plots_dict["Error"].setData(self.current_signal.time, self.interpolated_amplitude, pen=self.pen)
    
    self.graph_empty = False
    self.graph_deleted = False

def clear(self):
  if self.graph_empty == True:
      QtWidgets.QMessageBox.information(self, 'NO SIGNAL', 'No signal to delete')
  else:
      # overwrite variables
      self.browsed_signal = SampledSignal()
      self.current_signal = Signal()
      self.interpolated_signal = Signal()

      self.resampled_time = []
      self.resampled_amplitude = []
      self.ui.sampling_slider.setValue(0)
      self.graph_empty = True

      # plots to be cleared
      dict_keys = ["Primary1", "Primary2", "Primary3", "Secondary","Error"]
      for index in dict_keys:
          self.plots_dict[index].clear()

#################################################################################################

def change_sampling_rate(self, freqvalue):
  if freqvalue == 0:  
      freqvalue = 1

  if self.graph_empty:
      QtWidgets.QMessageBox.warning(self, 'NO SINGAL ', 'No signal imported!')
  else:
      returned_tuple = ()
      returned_tuple = downsample(self.current_signal.time, self.current_signal.amplitude, freqvalue)
      self.resampled_amplitude = np.array(returned_tuple[1])
      self.resampled_time = np.array(returned_tuple[0])

      # sinc interpolation
      self.interpolated_amplitude = sinc_interpolation(self.resampled_amplitude, self.resampled_time, self.current_signal.time)

      # refresh all viewer graphs
      self.pen = pg.mkPen(color=(0, 200, 0), width=0)
      self.plots_dict["Secondary1"].setData(self.resampled_time, self.resampled_amplitude, symbol='o', pen=self.pen)

      self.pen = pg.mkPen(color=(0, 200, 0), width=2)
      self.plots_dict["Secondary2"].setData(self.current_signal.time, self.interpolated_amplitude, pen=self.pen)

      self.pen = pg.mkPen(color=(150, 150, 150), width=2)
      self.plots_dict["Primary"].setData(self.current_signal.time, self.current_signal.amplitude, pen=self.pen)

      self.pen = pg.mkPen(color=(0, 200, 0), width=2)
      self.plots_dict["Error"].setData(self.current_signal.time, self.interpolated_amplitude, pen=self.pen)


def sinc_interpolation(input_amplitude, input_time, original_time):
    '''Whittaker Shannon interpolation formula linked here:
      https://en.wikipedia.org/wiki/Whittaker%E2%80%93Shannon_interpolation_formula '''

    if len(input_amplitude) != len(input_time):
        print('not same')

    # Find the period
    if len(input_time) != 0:
        T = input_time[1] - input_time[0]

    # the equation
    sincM = np.tile(original_time, (len(input_time), 1)) - np.tile(input_time[:, np.newaxis], (1, len(original_time)))
    output_amplitude = np.dot(input_amplitude, np.sinc(sincM/T))
    return output_amplitude

def downsample(array_x, array_y, freq):
    '''Returns a tuple containting downsampled (array_x, array_y) '''

    resampled_x = []
    resampled_y = []

    # divide total samples over maximum time to get 1/period
    max_sampling_freq = len(array_x)/max(array_x)
    length = len(array_x)
    step = round(max_sampling_freq/freq)

    for index in range(0, length, step):
        resampled_x.append(array_x[index])
        resampled_y.append(array_y[index])

    return resampled_x, resampled_y