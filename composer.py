from PyQt5 import QtWidgets
import classes
import numpy as np
import viewer
NUM_OF_POINTS = 1000
summed_graph = False

def plot_sinusoidal_wave(self):
    #TODO make the plotting more efficient
    amplitude = self.ui.sinusoidal_amplitude_slider.value()
    frequency = self.ui.sinusoidal_frequency_slider.value()
    phase = self.ui.sinusoidal_phase_slider.value()
    # Set axes and plot
    xAxis = np.linspace(0, 2 * np.pi, int(NUM_OF_POINTS)) #Time
    yAxis = amplitude * np.sin(frequency * xAxis + phase) #wave
    self.plots_dict["Sinusoidal"].setData(xAxis, yAxis, pen='w', title="Sinusoidal Waveform")



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
      xAxis = np.linspace(0, 2 * np.pi, NUM_OF_POINTS)
      yAxis = amplitude * np.sin(frequency * xAxis + phase)
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
  if len(self.sinusoidals_list) != 0 and self.sinusoidal_index < len(self.sinusoidals_list):
    self.ui.sinusoidal_frequency_slider.setValue(self.sinusoidals_list[self.sinusoidal_index].frequency)
    self.ui.sinusoidal_amplitude_slider.setValue(self.sinusoidals_list[self.sinusoidal_index].amplitude)
    self.ui.sinusoidal_phase_slider.setValue(self.sinusoidals_list[self.sinusoidal_index].phase)
    self.ui.add_sinusoidal_button.setText("Apply")
  else:
    self.ui.add_sinusoidal_button.setText("Add")
    self.ui.sinusoidal_amplitude_slider.setValue(0)
    self.ui.sinusoidal_frequency_slider.setValue(0)
    self.ui.sinusoidal_phase_slider.setValue(0)

  plot_sinusoidal_wave(self)

def sum_sinusoidal_waves(self):
    summed_graph = True
    self.summed_sinusoidals = classes.summed_sinusoidals(self.sinusoidals_list)   
    # max_frequency = classes.summed_sinusoidals.max_frequency
    self.plots_dict["Summed"].setData(self.summed_sinusoidals.xAxis, self.summed_sinusoidals.yAxis, pen='b', title="Sinusoidal Waveform")

def deleteSinusoidal(self):
    if self.sinusoidal_index >= 0 and self.sinusoidal_index < len(self.sinusoidals_list):
        # Remove the item from the list
        self.sinusoidals_list.pop(self.sinusoidal_index)

        # Remove the corresponding item from the menu
        self.ui.sinusoidals_signals_menu.removeItem(self.sinusoidal_index)

        # Update the index to a valid value (e.g., the last item in the list)
        self.ui.sinusoidals_signals_menu.setCurrentIndex(len(self.sinusoidals_list))

        # Recalculate and update the summed waveform
        sum_sinusoidal_waves(self)
    else:
        print("Invalid index or empty list, cannot delete.")



def clear_composer(self):
    # Clear the "Summed" signal by setting empty arrays for data
    self.plots_dict["Summed"].setData([], [], pen='b', title="Sinusoidal Waveform")

    # Clear the list of sinusoidal signals
    self.sinusoidals_list = []

    # Clear the signal menu
    self.ui.sinusoidals_signals_menu.clear()

    # Reset the signal number
    self.sinusoidal_number = 1

    # Add a default "Signal 1" to the menu
    self.ui.sinusoidals_signals_menu.addItem("Signal 1")

def move_sinusoidal_to_sampling(self):
    
    if not self.graph_empty: 
      QtWidgets.QMessageBox.information(self, 'Error', 'Clear the viewer first!')
    
    # elif not summed_graph:
    #   QtWidgets.QMessageBox.information(self, 'Error', 'Please add a sin wave first!')
    else:
      self.graph_empty = False
      # Get the data from the "Summed" plot
      x_data, y_data = self.plots_dict["Summed"].getData()
      
      if len(x_data) > 0 and len(y_data) > 0:
          # Move the data to the selected plot
          self.summed_sinusoidals = classes.summed_sinusoidals(self.sinusoidals_list)  
          viewer.move_to_viewer(self, Input = "composer")
      else:
          print("No data to move from 'Summed' plot.")

