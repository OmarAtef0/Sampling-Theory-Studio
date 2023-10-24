from scipy import fft
import numpy as np

# GLOBAL CONSTANTS
MAX_SAMPLES = 3000

class SampledSignal():
    '''An object containing sample points array'''

    def __init__(self, sampling_frequency=1, magnitude_array=[]):
        self.sampling_frequency = sampling_frequency
        self.max_analog_frequency = (1/2)*self.sampling_frequency
        self.magnitude_array = magnitude_array
        self.total_samples = len(magnitude_array)
        self.time_array = []
        self.generate_time_array()

    def generate_time_array(self):
        for index in range(self.total_samples):
            self.time_array.append(index/self.sampling_frequency)


class Signal():
    '''An object containing the generic signal'''

    def __init__(self, magnitude=[], time=[], max_analog_frequency=1):
        self.magnitude = magnitude
        self.time = time
        self.max_analog_frequency = max_analog_frequency

    def get_max_frequency(self):

        sample_period = self.time[1] - self.time[0]
        n_samples = len(self.time)

        # gets array of fft magnitudes
        fft_magnitudes = np.abs(fft.fft(self.magnitude))
        # gets array of frequencies
        fft_frequencies = fft.fftfreq(n_samples, sample_period)
        # create new "clean array" of frequencies
        fft_clean_frequencies_array = []
        for index in range(len(fft_frequencies)):
            # checks if signigifcant frequency is present
            if fft_magnitudes[index] > 0.001:
                fft_clean_frequencies_array.append(fft_frequencies[index])

        # get the last element and equate with max_frequency
        self.max_analog_frequency = max(fft_clean_frequencies_array)

        return self.max_analog_frequency


class PlotterWindow():
    '''Abstraction of plotter window properties'''

    def __init__(self, plot_reference,  x_start=0, x_end=1, y_start=-1, y_end=1):
        self.plot_reference = plot_reference

        self.x_range_tuple = (x_start, x_end)
        self.y_range_tuple = (y_start, y_end)

    def update_plot(self, PlotWindow):
        "Updates range of passed plot instance"
        self.plot_reference.setXRange(xMin=self.x_range_tuple[0], xMax=self.x_range_tuple[1],
                                      yMin=self.y_range_tuple[0], yMax=self.y_range_tuple[1])
