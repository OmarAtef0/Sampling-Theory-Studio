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

def add_noise(self, noise_slider_value):
    np.random.seed(42)
    if self.graph_empty:
        return
    else:
        if noise_slider_value == 0:
            self.current_signal.amplitude = self.original_amplitude
        else:
            # Extract the amplitude values from the current_signal and convert them to a NumPy array
            signal_amplitude = np.array(self.current_signal.amplitude)

            # Generate random noise with the same length as the signal, sampled from a normal distribution
            noise = np.random.normal(0, abs(signal_amplitude), len(signal_amplitude))
            print("noise : ",noise)

            # Adjust the noise level using a slider value (noise_slider_value)
            noisy_amplitude = signal_amplitude + noise * noise_slider_value / 30

            # Update the amplitude values of the current_signal with the noisy signal
            self.current_signal.amplitude = noisy_amplitude

        # refresh all viewer graphs
        refresh_graphs(self)
        change_sampling_rate(self, self.ui.sampling_slider.value()+4)
        self.ui.sampling_lcd.display(self.ui.sampling_slider.value())

def move_to_viewer(self, Input):
    self.graph_empty = False
    self.ui.sampling_slider.setEnabled(True)
    self.ui.noise_slider.setEnabled(True)
    if Input == "composer":
        self.ui.import_btn.setDisabled(True)
        self.current_signal = Signal(self.summed_sinusoidals.xAxis, self.summed_sinusoidals.yAxis, self.summed_sinusoidals.max_frequency)
        self.ui.WindowTabs.setCurrentIndex(0)

    elif Input == "browse":
        self.current_signal = Signal(self.browsed_signal.time_array,self.browsed_signal.amplitude_arr, self.browsed_signal.max_analog_freq)
        self.current_signal.get_max_freq()  
        self.ui.WindowTabs.setCurrentIndex(0)
        
    # update slider maximum to 4Fmax
    self.ui.sampling_slider.setMaximum(int(30 * self.current_signal.max_analog_freq ))
    self.ui.sampling_slider.setSingleStep(1)
    self.ui.fmaxLCD.display(int(self.current_signal.max_analog_freq))
    
    self.original_amplitude = self.current_signal.amplitude
    # initialize plots
    refresh_graphs(self)

def clear(self):
    if self.graph_empty == True:
        QtWidgets.QMessageBox.information(self, 'NO SIGNAL', 'No signal to delete')
    else:
        # overwrite variables
        self.graph_empty = True
        self.browsed_signal = SampledSignal()
        self.current_signal = Signal()
        self.resampled_time = []
        self.resampled_amplitude = []
        self.reconstructed_amplitude = []
        self.original_amplitude = []

        self.ui.sampling_slider.setValue(1)
        self.ui.noise_slider.setValue(0)
        self.ui.sampling_slider.setDisabled(True)
        self.ui.noise_slider.setDisabled(True)
        self.ui.fmaxLCD.display(0)
        self.ui.import_btn.setEnabled(True)
        self.ui.sampling_lineEdit.setText("1")

        # plots to be cleared
        refresh_graphs(self)

def refresh_graphs(self):
    y_range = (-max(self.original_amplitude)*1.5, max(self.original_amplitude)*1.5)
    print("max amplitude: ", max(self.original_amplitude))
    self.ui.primary_plot.setYRange(*y_range)
    self.ui.reconstructed_plot.setYRange(*y_range)
    self.ui.error_plot.setYRange(*y_range)

    # refresh all viewer graphs
    self.pen = pg.mkPen(color=(150, 150, 150), width=2)
    self.plots_dict["Primary1"].setData(self.current_signal.time, self.original_amplitude, pen=self.pen)

    self.pen = pg.mkPen(color=(0, 200, 0), width=0)
    self.plots_dict["Primary2"].setData(self.resampled_time, self.resampled_amplitude, symbol='o', pen=self.pen,  symbolSize=10)

    self.pen = pg.mkPen(color=(0, 200, 0), width=2)
    self.plots_dict["Secondary1"].setData(self.current_signal.time, self.reconstructed_amplitude, pen=self.pen)

    if len(self.current_signal.amplitude) > 0 and len(self.reconstructed_amplitude) > 0:
        self.pen = pg.mkPen(color=(0, 200, 250), width=2)

        self.error = self.current_signal.amplitude - self.reconstructed_amplitude
        self.plots_dict["Error"].setData(self.current_signal.time, self.error, pen=self.pen)

        print("error: ",self.error)
        # print("original: ",self.current_signal.amplitude)
        # print("interpolated: ",self.reconstructed_amplitude)

    else:
        self.pen = pg.mkPen(color=(0, 200, 250), width=2)
        self.plots_dict["Error"].setData(self.current_signal.time, self.current_signal.amplitude, pen=self.pen)


def change_sampling_rate(self, freqvalue):
  if self.graph_empty:
    return
  else:
    returned_tuple = ()
    returned_tuple = downsample(self.current_signal.time, self.current_signal.amplitude, freqvalue)
    self.resampled_time = np.array(returned_tuple[0])
    self.resampled_amplitude = np.array(returned_tuple[1])
    
    # sinc interpolation
    self.reconstructed_amplitude = sinc_interpolation(self.resampled_amplitude, self.resampled_time, self.current_signal.time)

    # refresh all viewer graphs
    refresh_graphs(self)

def sinc_interpolation(input_amplitude, input_time, original_time):
    '''Whittaker Shannon interpolation formula linked here:
      https://en.wikipedia.org/wiki/Whittaker%E2%80%93Shannon_interpolation_formula '''

    # Find the period
    if len(input_time) != 0:
        T = input_time[1] - input_time[0]

    # The equation 
    # original_time - downsampled_time -> divide this matrix by period -> np.sinc() -> dot product by input_amplitude

    # The goal of this code is to create a matrix sincM with dimensions (M, N)
    sincM = np.tile(original_time, (len(input_time), 1)) - np.tile(input_time[:, np.newaxis], (1, len(original_time)))

    # np.newaxis -> transpose 
    
    # sinc(x) = sin(pi * x) / (pi * x)
    output_amplitude = np.dot(input_amplitude, np.sinc(sincM / T))
    return output_amplitude

def downsample(arr_x, arr_y, freq):
    '''Returns a tuple containing downsampled (arr_x, arr_y)'''

    # Lists to store downsampled x and y values
    resampled_x = []
    resampled_y = []

    # Calculate the maximum sampling frequency based on the input x values
    # arr_x is a time array, and the maximum sampling frequency is determined by the maximum time value
    length = len(arr_x)
    max_sampling_freq = length / max(arr_x)

    # Calculate the step size for downsampling
    step = round(max_sampling_freq / freq)

    # Iterate through the original arrays with the calculated step size
    for index in range(0, length, step):
        # Append the downsampled x and y values to the result lists
        resampled_x.append(arr_x[index])
        resampled_y.append(arr_y[index])
    
    # Print the original and downsampled x values for debugging or analysis
    print("Original x values size:", len(arr_x))
    print("Downsampled x values size:", len(resampled_x))

    # Return a tuple containing the downsampled x and y values
    return resampled_x, resampled_y
