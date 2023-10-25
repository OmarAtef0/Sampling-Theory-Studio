# WHAT SHOULD THE COMPOSER DO?
'''
Rightmost graph
1. Connect to all the sliders
2. Modify(return) "sinusoid" object accordingly
X. if confirmation button is clicked, 1. pass finished sinusiod object array to the summing function
                                      2. create new sinusiod object to start modifying again
X. if delete sinusiod button is clicked, 1.sinusiod creator array.pop(current combobox index) 
                                        2. update combobox accordingly?
Leftmost graph
1. Connect to confirmation button of sinusoid creator
2. if sinusoid confirmation or deletion button is clicked trigger the sine summing function
3. and then update plot with the sine summing function's output array

Required function to be implemented
1- plot sinusoidal 2- add sinusoidal 3- delete sinusoidal 4-l

'''
import classes
import numpy as np
NUM_OF_POINTS = 1000

def plot_sinusoidal_wave(self):
    #TODO make the plotting more efficient
    amplitude = self.ui.sinusoidal_amplitude_slider.value()
    frequency = self.ui.sinusoidal_frequency_slider.value()
    phase = self.ui.sinusoidal_phase_slider.value()
    # Set axes and plot
    xAxis = np.linspace(0, 10, int(NUM_OF_POINTS)) #Time
    yAxis = amplitude * np.sin(2 * np.pi * frequency * xAxis + phase) #wave
    self.plots_dict["Sinusoidal"].setData(xAxis, yAxis, pen='b', title="Sinusoidal Waveform")



def add_sinusoidal_wave(self):
  self.sinusoidal_index = self.ui.sinusoidals_signals_menu.currentIndex()
  amplitude = self.ui.sinusoidal_amplitude_slider.value()
  frequency = self.ui.sinusoidal_frequency_slider.value()
  phase = self.ui.sinusoidal_phase_slider.value()

  if self.sinusoidal_index == len(self.sinusoidals_list):
    new_sinusoidal_wave = classes.sinusoidal_wave(index = self.sinusoidal_index, amplitude=amplitude, frequency=frequency, phase=phase)
    self.sinusoidals_list.append(new_sinusoidal_wave)
    self.sinusoidal_number += 1
    self.ui.sinusoidals_signals_menu.addItem("Signal " + str(self.sinusoidal_number))


  else:
      xAxis = np.linspace(0, 2* np.pi, NUM_OF_POINTS)
      yAxis = amplitude * np.sin(2 * np.pi * frequency * xAxis + phase)
      self.sinusoidals_list[self.sinusoidal_index].amplitue = amplitude
      self.sinusoidals_list[self.sinusoidal_index].frequency = frequency
      self.sinusoidals_list[self.sinusoidal_index].phase = phase
      self.sinusoidals_list[self.sinusoidal_index].xAxis = xAxis
      self.sinusoidals_list[self.sinusoidal_index].yAxis = yAxis

  sum_sinusoidal_waves(self)
  self.ui.sinusoidals_signals_menu.setCurrentIndex(len(self.sinusoidals_list))



def update_sinusoidal_menubar(self, input):
  self.sinusoidal_index = input
  # Set slider values to appropriate positions when user selects already added signal
  if len(self.sinusoidals_list) != 0:
      if self.sinusoidal_index < len(self.sinusoidals_list):
          self.ui.sinusoidal_frequency_slider.setValue(
              self.sinusoidals_list[self.sinusoidal_index].frequency)
          self.ui.sinusoidal_amplitude_slider.setValue(
              self.sinusoidals_list[self.sinusoidal_index].amplitude)
          self.ui.sinusoidal_phase_slider.setValue(
              self.sinusoidals_list[self.sinusoidal_index].phase)
      # Set slider values to default when yet to be confirmed signal is selected
      else:
        self.ui.sinusoidal_amplitude_slider.setValue(1)
        self.ui.sinusoidal_frequency_slider.setValue(1)
        self.ui.sinusoidal_phase_slider.setValue(0)
  else:
      self.ui.sinusoidal_amplitude_slider.setValue(1)
      self.ui.sinusoidal_frequency_slider.setValue(1)
      self.ui.sinusoidal_phase_slider.setValue(0)

  plot_sinusoidal_wave(self)

def sum_sinusoidal_waves(self):
    summed_sinusoidals = classes.summed_sinusoidals(self.sinusoidals_list)   
    # max_frequency = classes.summed_sinusoidals.max_frequency
    self.plots_dict["Summed"].setData(summed_sinusoidals.xAxis, summed_sinusoidals.yAxis, pen='b', title="Sinusoidal Waveform")



# def remove_sinusoidal_wave(self, index):
#     pass


# def clear_composer(self):
#     pass
