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


class sinusoidal_wave():
  def __init__(self, index=0, amplitude=1, frequency=1, phase=0):
      self.index = index
      self.amplitude= amplitude
      self.frequency= frequency
      self.phase= phase
      self.PI = np.pi
      self.xAxis = np.linspace(0, np.pi*2, 1000)
      self.yAxis = self.amplitude * np.sin(2*self.PI*self.frequency*self.xAxis + self.phase*(self.PI/180))
  
  # def creat_sin_wave(self):
  #   if(self.kind == "Sinusoidal"):
  #     self.sinusiodal_values = self.amplitude * np.sin(2*self.PI*self.frequency*self.xAxis + self.phase*(self.PI/180))
  #   else:
  #     self.sinusiodal_values = self.amplitude * np.cos(2*self.PI*self.frequency*self.xAxis + self.phase*(self.PI/180))

  #   return self.sinusiodal_values
  
  def getLabel(self):
    return f'{self.amplitude}@{self.frequency} HZ + {self.phase}'

  def get_frequency(self):
    return self.frequency
  
class summed_sinusoidals():
  def __init__(self, sinusoidals_list=[sinusoidal_wave()]):
    self.sinusoidals_list = sinusoidals_list
    self.max_frequency = 1
    self.xAxis = []
    self.yAxis = []

    if len(self.sinusoidals_list) > 0:
      self.xAxis = self.sinusoidals_list[0].xAxis
      self.yAxis_sum = self.sinusoidals_list[0].yAxis
      self.max_frequency = self.sinusoidals_list[0].frequency

    if len(self.sinusoidals_list) > 1:
      for component  in range(1, len(self.sinusoidals_list)):
        self.yAxis_sum += self.sinusoidals_list[component].yAxis
        self.max_frequency = max(self.sinusoidals_list[component].frequency, self.max_frequency)
    
    self.yAxis = self.yAxis_sum