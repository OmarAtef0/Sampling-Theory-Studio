import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
import pyqtgraph as pg
import viewer
from classes import *
from task2 import Ui_MainWindow
import composer
import qdarkstyle

MAX_SAMPLES = 1000
NUM_OF_POINTS = 1000

class SamplingStudioApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  

        # for deleted signal/empty Graph
        self.graph_empty = True
        self.browsed_signal = SampledSignal()
        self.current_signal = Signal()

        self.resampled_time = []
        self.resampled_amplitude = []

        self.reconstructed_time = []
        self.reconstructed_amplitude = []

        self.original_amplitude = []
        self.error = []

        self.first_plot = True
        self.current_f_sampling = 1
        self.fraction_val = 1.0
        self.noise = []
        self.noisy_amplitude = []
        self.snr_level = 0
        self.sinusoidal_index = 0
        self.sinusoidal_number = 1
        self.sinusoidals_list = []
        self.ui.sinusoidals_signals_menu.addItem("Signal " + str(self.sinusoidal_number))
        
        plots = [
        self.ui.primary_plot,
        self.ui.reconstructed_plot,
        self.ui.error_plot,
        self.ui.sinusoidal_secondary_plot,
        self.ui.sinusoidal_main_plot
        ]

        # Loop through the list and set labels for each plot
        for plot_widget in plots:
            plot_widget.setLabel('bottom', "Time")
            plot_widget.setLabel('left', "Amplitude")

        # initialize graph objects array/dict
        self.plots_dict = {
                            "Primary1": self.ui.primary_plot.plot(),
                            "Primary2": self.ui.primary_plot.plot(),
                            "Secondary1": self.ui.reconstructed_plot.plot(),
                            "Error": self.ui.error_plot.plot(),
                            "Sinusoidal": self.ui.sinusoidal_secondary_plot.plot(),
                            "Summed": self.ui.sinusoidal_main_plot.plot()
                        }
        
        ''' 
        Primary1 is the original signal
        Primary2 is the resampled points 
        Secondary1 is the reconstructed signal
        '''

        # Disable auto-range for both axes
        self.ui.primary_plot.plotItem.enableAutoRange(pg.ViewBox.YAxis, enable=False)
        self.ui.reconstructed_plot.plotItem.enableAutoRange(pg.ViewBox.YAxis, enable=False)
        self.ui.error_plot.plotItem.enableAutoRange(pg.ViewBox.YAxis, enable=False)

        #mouse
        # self.ui.primary_plot.setMouseEnabled(x=False, y=False)
        # self.ui.reconstructed_plot.setMouseEnabled(x=False, y=False)
        # self.ui.error_plot.setMouseEnabled(x=False, y=False)
        # self.ui.sinusoidal_main_plot.setMouseEnabled(x=False, y=False)
        # self.ui.sinusoidal_secondary_plot.setMouseEnabled(x=False, y=False)

        self.ui.clear_btn.clicked.connect(lambda: viewer.clear(self))
        self.ui.import_btn.clicked.connect(lambda: viewer.browse(self))
        self.fmax_boolean = False

        # Sampling frequency control
        self.ui.sampling_slider.setMinimum(1)
        self.ui.sampling_slider.valueChanged.connect(lambda: viewer.change_sampling_rate(self, self.ui.sampling_slider.value()))
        self.ui.sampling_slider.valueChanged.connect(lambda: self.ui.sampling_lcd.display(self.ui.sampling_slider.value()))

        self.ui.sampling_slider_1.setMinimum(1)
        self.ui.sampling_slider_1.valueChanged.connect(lambda: viewer.change_sampling_rate(self, (self.ui.sampling_slider_1.value()) * int(self.current_signal.max_analog_freq)))
        self.ui.sampling_slider_1.valueChanged.connect(lambda: self.ui.sampling_lcd.display((self.ui.sampling_slider_1.value()) * int(self.current_signal.max_analog_freq)))
        self.ui.sampling_slider_1.valueChanged.connect(self.connect_slider_values)

        # SNR control
        self.ui.noise_slider.setMinimum(0)
        self.ui.noise_slider.valueChanged.connect(lambda: viewer.add_noise(self, self.ui.noise_slider.value() * 0.003))
        self.ui.noise_slider.valueChanged.connect(lambda: self.ui.noise_lcd.display(self.ui.noise_slider.value()))

        # Sinsusoidal_Sliders
        self.ui.sinusoidal_frequency_slider.valueChanged.connect(lambda: composer.plot_sinusoidal_wave(self))
        self.ui.sinusoidal_frequency_slider.valueChanged.connect(lambda: self.ui.sinusoidal_frequency_LCD.display(self.ui.sinusoidal_frequency_slider.value()))
        
        self.ui.sinusoidal_amplitude_slider.valueChanged.connect(lambda: composer.plot_sinusoidal_wave(self))
        self.ui.sinusoidal_amplitude_slider.valueChanged.connect(lambda: self.ui.sinusoidal_amplitude_LCD.display(self.ui.sinusoidal_amplitude_slider.value()))
        
        self.ui.sinusoidal_phase_slider.valueChanged.connect(lambda: composer.plot_sinusoidal_wave(self))
        self.ui.sinusoidal_phase_slider.valueChanged.connect(lambda: self.ui.sinusoidal_phase_LCD.display(self.ui.sinusoidal_phase_slider.value()))

        self.ui.add_sinusoidal_button.clicked.connect(lambda: composer.add_sinusoidal_wave(self))
        self.ui.sinusoidals_signals_menu.currentIndexChanged.connect(lambda: composer.update_sinusoidal_menubar(self, self.ui.sinusoidals_signals_menu.currentIndex()))
        self.ui.clear_composer_button.clicked.connect(lambda: composer.clear_composer(self))
        self.ui.delete_sinusoidal_button.clicked.connect(lambda: composer.deleteSinusoidal(self))
        self.ui.sample_sinusoidals_button.clicked.connect(lambda: composer.move_sinusoidal_to_sampling(self))
        self.ui.sample_sinusoidals_button.setDisabled(True)
        self.ui.clear_composer_button.setDisabled(True)
    
    def connect_slider_values(self):
        self.ui.sampling_slider.setValue(int(self.ui.sampling_slider_1.value() * self.current_signal.max_analog_freq))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SamplingStudioApp()
    window.setWindowTitle("Sampling Theory Studio")
    app.setWindowIcon(QIcon("logo.png"))
    window.resize(1250,900)
    window.show()
    sys.exit(app.exec_())
