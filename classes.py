from scipy import fft
import numpy as np

# GLOBAL CONSTANTS
MAX_SAMPLES = 3000

class SampledSignal():
    '''An object containing sample points array'''
    def __init__(self, sampling_freq=1, amplitude_arr=[]):
        # Fs = 2 * Fmax
        self.sampling_freq = sampling_freq
        self.max_analog_freq = (1/2)*self.sampling_freq
        self.amplitude_arr = amplitude_arr
        self.total_samples = len(amplitude_arr)
        self.time_array = []
        self.generate_time_array()

    def generate_time_array(self):
        for index in range(self.total_samples):
            self.time_array.append(index/self.sampling_freq)


class Signal():
    '''An object containing the generic signal'''
    def __init__(self, time=[] ,amplitude=[], max_analog_freq=1):
        self.amplitude = amplitude
        self.time = time
        self.max_analog_freq = max_analog_freq

    def get_max_freq(self):
        sample_period = self.time[1] - self.time[0]
        n_samples = len(self.time)

        # gets array of fft amplitudes
        fft_amplitudes = np.abs(fft.fft(self.amplitude))
        # gets array of frequencies
        fft_frequencies = fft.fftfreq(n_samples, sample_period)
        # create new "clean array" of frequencies
        fft_clean_frequencies_array = []
        for index in range(len(fft_frequencies)):
            # checks if signigifcant freq is present
            if fft_amplitudes[index] > 0.001:
                fft_clean_frequencies_array.append(fft_frequencies[index])

        # get the last element and equate with max_freq
        self.max_analog_freq = max(fft_clean_frequencies_array)

        return self.max_analog_freq


