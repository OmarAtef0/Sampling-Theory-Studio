import csv
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QFileDialog
import pyqtgraph as pg
import numpy as np
from classes import *

# import signal from csv 
def browse(self):
    self.graph_empty = False
    self.filename = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", )
    path = self.filename[0]

    time = []
    amplitude = []
    self.fsample = 1
    
    with open(path, 'r') as csvFile:   
        csvReader = csv.reader(csvFile, delimiter=',')
        for line in csvReader:
            if len(time) - 1 >= MAX_SAMPLES:
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
            # Extract the amplitude values from the current_signal and convert them to a NumPy array
        signal_amplitude = np.array(self.original_amplitude)

        # Generate random noise with the same length as the signal, sampled from a normal distribution
        self.noise = np.random.normal(0, abs(signal_amplitude), len(signal_amplitude)) 

        self.noisy_amplitude = np.array(self.original_amplitude + self.noise * noise_slider_value * 0.8)

        self.current_signal.amplitude = np.array(self.noisy_amplitude)

        # refresh all viewer graphs
        refresh_graphs(self)
        change_sampling_rate(self, self.ui.sampling_slider.value())

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
    
    self.ui.sampling_slider.setMaximum(100 * int(self.current_signal.max_analog_freq))
    self.ui.fmaxLCD.display(int(self.current_signal.max_analog_freq))
    
    self.original_amplitude = np.array(self.current_signal.amplitude)
    # initialize plots
    refresh_graphs(self)
    change_sampling_rate(self, self.ui.sampling_slider.value())

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
        self.noisy_amplitude = []

        self.ui.sampling_slider.setValue(1)
        self.ui.noise_slider.setValue(0)
        self.ui.sampling_slider.setDisabled(True)
        self.ui.noise_slider.setDisabled(True)
        self.ui.fmaxLCD.display(0)
        self.ui.import_btn.setEnabled(True)

        # plots to be cleared
        refresh_graphs(self)

def refresh_graphs(self):
    if len(self.original_amplitude):
        y_range = (-max(self.original_amplitude)*1.5, max(self.original_amplitude)*1.5)
        self.ui.primary_plot.setYRange(*y_range)
        self.ui.reconstructed_plot.setYRange(*y_range)
        self.ui.error_plot.setYRange(*y_range)

    # refresh all viewer graphs
    self.pen = pg.mkPen(color=(0, 200, 250), width=2) 
    self.plots_dict["Primary1"].setData(self.current_signal.time, self.current_signal.amplitude, pen=self.pen)

    self.pen = pg.mkPen(color=(0, 200, 0), width=0)
    self.plots_dict["Primary2"].setData(self.resampled_time, self.resampled_amplitude, symbol='o', pen=self.pen,  symbolSize=3)

    self.pen = pg.mkPen(color=(0, 200, 0), width=2)
    self.plots_dict["Secondary1"].setData(self.current_signal.time[0:1000], self.reconstructed_amplitude, pen=self.pen)
    
    self.pen = pg.mkPen(color=(0, 200, 250), width=2) 
    if len(self.error) > 0:
        self.plots_dict["Error"].setData(self.current_signal.time[0:1000], self.error, pen=self.pen)
    else:
        self.plots_dict["Error"].setData(self.current_signal.time[0:1000], self.current_signal.amplitude[0:1000], pen=self.pen)

def resample(self):
    # points
    x_vec = self.current_signal.time
    y_vec = self.current_signal.amplitude

    # Sampling the signal
    x_sampled = np.arange(x_vec[0], x_vec[-1], 1/self.f_sampling)
    y_sampled = np.interp(x_sampled, x_vec, y_vec)

    self.resampled_time = x_sampled 
    self.resampled_amplitude = y_sampled

def reconstruct(self):
    # Reconstruct Signal
    t = np.linspace(self.current_signal.time[0], self.current_signal.time[-1], 1000)
    x_vec = self.resampled_time
    y_vec = self.resampled_amplitude

    # Whittaker–Shannon interpolation formula
    y_interp = np.zeros_like(t)
    for i, t_i in enumerate(t):
        y_interp[i] = np.sum(y_vec * np.sinc((x_vec - t_i) * self.f_sampling))
    
    self.reconstructed_time = t
    self.reconstructed_amplitude = y_interp


def display_error_signal(self):
    # calculate difference between original signal and reconstructed signal
    y_vec_error = np.abs(self.current_signal.amplitude[0:1000] - self.reconstructed_amplitude)
    self.error = y_vec_error

def change_sampling_rate(self, freqvalue):
  self.f_sampling = freqvalue
  if self.graph_empty:
    return
  else:      
    resample(self)
    reconstruct(self)
    display_error_signal(self)
    refresh_graphs(self)

        
 