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

    temp_arr_x = []
    temp_arr_y = []
    self.fsampling = 1
    
    with open(path, 'r') as csvFile:    # 'r' its a mode for reading and writing
        csvReader = csv.reader(csvFile, delimiter=',')

        # neglect the first line in the csv file
        next(csvReader)

        for line in csvReader:
            if len(temp_arr_x) > MAX_SAMPLES:
                break
            else:
                temp_arr_y.append(float(line[1]))
                temp_arr_x.append(float(line[0]))

    self.fsampling = 1/(temp_arr_x[1]-temp_arr_x[0])
    self.browsed_signal = SampledSignal(self.fsampling, temp_arr_y)
    move_to_viewer(self, "browse")

def move_to_viewer(self, Input):
    if Input == "composer":
        self.viewer_original_signal = Signal(self.summed_signal.yAxis, self.summed_signal.xAxis, self.summed_signal.max_analog_frequency)
        # self.ui.WindowTabs.setCurrentIndex(1)

    elif Input == "browse":
        self.viewer_original_signal = Signal(self.browsed_signal.magnitude_array, self.browsed_signal.time_array, self.browsed_signal.max_analog_frequency)
        # self.ui.WindowTabs.setCurrentIndex(1)
        self.viewer_original_signal.get_max_frequency()  

    # update slider maximum
    self.ui.sampling_slider.setMaximum(3*(self.viewer_original_signal.max_analog_frequency))
    # self.ui.fmaxLCD.display(self.viewer_original_signal.max_analog_frequency)

    # initialize plots
    self.plotter_window_dict["Primary1"].plot_reference.setData(self.viewer_original_signal.time, self.viewer_original_signal.magnitude)
    self.plotter_window_dict["Secondary"].plot_reference.setData(self.viewer_original_signal.time, self.viewer_original_signal.magnitude)
    self.plotter_window_dict["Error"].plot_reference.setData(self.viewer_original_signal.time, self.viewer_original_signal.magnitude)
    self.graph_empty = False
    self.graph_deleted = False

def clear(self):
  if self.graph_empty == True:
      QtWidgets.QMessageBox.information(self, 'NO SIGNAL', 'No signal to delete')

  else:
      # overwrite variables
      self.viewer_original_signal = []
      self.interpolated_signal = []
      self.resampled_time = []
      self.resampled_magnitude = []
      # self.fmaxLCD.display(0)

      # plots to be reinitialized
      dict_keys = ["Primary1", "Primary2", "Primary3", "Secondary","Error"]
      for index in dict_keys:
          self.plotter_window_dict[index].plot_reference.clear()

      self.ui.sampling_slider.setValue(1)
      QtWidgets.QMessageBox.information(self, 'Deleted', 'Your signal has been deleted')
      self.graph_deleted = True
      self.graph_empty = True

def change_sampling_rate(self, freqvalue):
  if freqvalue == 0:  
      freqvalue = 1

  if self.signal_deleted:
      QtWidgets.QMessageBox.warning(self, 'NO SIGNAL ', 'The signal is deleted')
  elif self.graph_empty:
      QtWidgets.QMessageBox.warning(self, 'NO SINGAL ', 'No signal imported')
  else:
      returned_tuple = ()
      returned_tuple = downsample(self.viewer_original_signal.time, self.viewer_original_signal.magnitude, freqvalue)
      self.resampled_magnitude = np.array(returned_tuple[1])
      self.resampled_time = np.array(returned_tuple[0])

      # sinc interpolation
      self.interpolated_magnitude = sinc_interpolation(self.resampled_magnitude, self.resampled_time, self.viewer_original_signal.time)

      # refresh all viewer graphs
      self.pen = pg.mkPen(color=(150, 150, 150), width=2,style=QtCore.Qt.DotLine)
      self.plotter_window_dict["Primary1"].plot_reference.setData(self.viewer_original_signal.time, self.viewer_original_signal.magnitude, pen=self.pen)

      self.pen = pg.mkPen(color=(0, 200, 0), width=0)
      self.plotter_window_dict["Primary2"].plot_reference.setData(self.resampled_time, self.resampled_magnitude, symbol='o', pen=self.pen)

      self.pen = pg.mkPen(color=(0, 200, 0), width=2)
      self.plotter_window_dict["Primary3"].plot_reference.setData(self.viewer_original_signal.time, self.interpolated_magnitude, pen=self.pen)

      self.plotter_window_dict["Secondary"].plot_reference.setData(self.viewer_original_signal.time, self.interpolated_magnitude, pen=self.pen)
        

def sinc_interpolation(input_magnitude, input_time, original_time):
    '''Whittaker Shannon interpolation formula linked here:
      https://en.wikipedia.org/wiki/Whittaker%E2%80%93Shannon_interpolation_formula '''

    if len(input_magnitude) != len(input_time):
        print('not same')

    # Find the period
    if len(input_time) != 0:
        T = input_time[1] - input_time[0]

    # the equation
    sincM = np.tile(original_time, (len(input_time), 1)) - np.tile(input_time[:, np.newaxis], (1, len(original_time)))
    output_magnitude = np.dot(input_magnitude, np.sinc(sincM/T))
    return output_magnitude

def downsample(array_x, array_y, frequency):
    '''Returns a tuple containting downsampled (array_x, array_y) '''

    resampled_x = []
    resampled_y = []

    # divide total samples over maximum time to get 1/period
    max_sampling_frequency = len(array_x)/max(array_x)
    length = len(array_x)
    step = round(max_sampling_frequency/frequency)

    for index in range(0, length, step):
        resampled_x.append(array_x[index])
        resampled_y.append(array_y[index])

    return resampled_x, resampled_y