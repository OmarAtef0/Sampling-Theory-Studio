from scipy import fft
import numpy as np

# GLOBAL CONSTANTS
MAX_SAMPLES = 3000
NUM_OF_POINTS = 3001

class SampledSignal():
    '''An object containing sample points array'''
    def __init__(self, sampling_freq=1, amplitude_arr=[]):
        self.sampling_freq = sampling_freq

        #Fs = 2*Fmax
        self.max_analog_freq = (1/2) * self.sampling_freq
        self.amplitude_arr = amplitude_arr
        self.total_samples = len(amplitude_arr)
        self.time_array = []
        self.generate_time_array()

    # Function to generate a time array based on the total number of samples and the sampling frequency
    def generate_time_array(self):
        # Iterate through each index from 0 to (total_samples - 1)
        for index in range(self.total_samples):
            # Calculate the corresponding time value for each index using the sampling frequency
            time_value = index / self.sampling_freq
            
            # Append the calculated time value to the time_array
            self.time_array.append(time_value)


class Signal():
  '''An object containing the generic signal'''
  def __init__(self, time=[] ,amplitude=[], max_analog_freq=1):
    self.amplitude = amplitude
    self.time = time
    self.max_analog_freq = max_analog_freq

  # Function to calculate and return the maximum analog frequency present in the signal
  def get_max_freq(self):
    spec = np.fft.rfft(self.amplitude)
    peak = np.argmax(spec)
    val = np.abs(peak) 

    self.max_analog_freq = (val/6)*100 / 2
    print("2Fmax: ", (val/6)*100)

# Class definition for a sinusoidal wave
class sinusoidal_wave():
  def __init__(self, index=0, amplitude=1, frequency=1, phase=0):
    self.index = index             # Index of the wave
    self.amplitude = amplitude     # Amplitude of the wave
    self.frequency = frequency     # Frequency of the wave
    self.phase = phase             # Phase of the wave (in degrees)

    # Constants
    self.PI = np.pi                

    # Create x-axis values using NUM_OF_POINTS points from 0 to 2*pi
    self.xAxis = np.linspace(0, np.pi * 2, NUM_OF_POINTS)

    # Calculate y-axis values using the sinusoidal wave equation
    # Amplitude * sin(frequency * x + phase (converted to radians))
    self.yAxis = self.amplitude * np.sin(self.frequency * self.xAxis + (self.phase * (self.PI / 180)))

class summed_sinusoidals():
  def __init__(self, sinusoidals_list=[sinusoidal_wave()]):
    self.sinusoidals_list = sinusoidals_list    # List of sinusoidal waves to be summed
    self.max_frequency = 1                      # Maximum frequency among the sinusoidal components
    self.xAxis = []                             # X-axis values for the summed wave
    self.yAxis = []                             # Y-axis values for the summed wave

    # Check if the list of sinusoidal waves is not empty
    if len(self.sinusoidals_list) > 0:
      # Use the x-axis values of the first sinusoidal wave as the x-axis values for the summed wave
      self.xAxis = self.sinusoidals_list[0].xAxis

      # Initialize the summed y-axis values with the y-axis values of the first sinusoidal wave
      self.yAxis_sum = self.sinusoidals_list[0].yAxis

      # Initialize the maximum frequency with the frequency of the first sinusoidal wave
      self.max_frequency = self.sinusoidals_list[0].frequency

      # If there are more than one sinusoidal components, iterate through the list
      if len(self.sinusoidals_list) > 1:
          for component in range(1, len(self.sinusoidals_list)):
              # Add the y-axis values of each component to the summed y-axis values
              self.yAxis_sum += self.sinusoidals_list[component].yAxis

              # Update the maximum frequency if the current component has a higher frequency
              self.max_frequency = max(self.sinusoidals_list[component].frequency, self.max_frequency)
    else:
      # If the list is empty, set the summed y-axis values to an empty list
      self.yAxis_sum = []

    # Set the final y-axis values of the summed wave
    self.yAxis = self.yAxis_sum
