# Signal Sampling and Recovery Application

## Overview
This desktop application is designed to illustrate the importance of the Nyquist-Shannon sampling theorem in digital signal processing. It allows users to load, sample, and recover analog signals, showing how different sampling frequencies affect signal recovery. our application offers the ability to mix, add noise, and perform real-time sampling and recovery. Additionally, it provides the flexibility to resize the application window. (make the application responsive)

## Features

### 1. Sample & Recover
- **Sample Signal**: Load a mid-length signal (approximately 1000 points) and visualize it. Users can sample it at various frequencies, which can be displayed in actual frequency or normalized frequency (concerning the maximum frequency).
- **Recover Signal**: The application uses the Whittaker-Shannon interpolation formula to recover the original signal based on the sampled points.
- **Visualization**: Three graphs display the original signal with markers for sampled points, the reconstructed signal, and the difference between the original and reconstructed signals.

### 2. Load & Compose
- **Load Signal**: Users can load a signal from a file or create a custom signal by mixing multiple sinusoidal components with different frequencies and magnitudes.
- **Signal Mixer**: The signal mixer allows users to add and remove single sinusoidal components to prepare a mixed signal.

### 3. Additive Noise
- **Noise Addition**: Users can introduce custom noise with a controllable Signal-to-Noise Ratio (SNR) level.
- **Noise Impact**: The application visually demonstrates the impact of noise on the signal, showcasing how the noise level varies with signal frequency.

### 4. Real-time Sampling and Recovery
- All operations, including sampling and recovery, are performed in real-time without the need for a manual update or refresh buttons.

### 5. Responsive UI
- The application is designed to be easily resizable without affecting the UI.

### 6. Different Sampling Scenarios
- The application includes at least three signals that cover a lot of scenarios. These signals are generated and saved through the built-in composer.
- Example Test Case: A mix of 2Hz and 6Hz sinusoidal signals. Sampling at 12Hz or higher results in successful recovery, while sampling at 4Hz shows the two frequencies as one. What happens when the signal is sampled at 8Hz?

## Information for the user
To use the application, follow these steps:

1. Load a signal or create a custom signal using the Signal Mixer.
2. Adjust the sampling frequency in real-time and observe the effects on signal recovery.
3. add noise to the signal and control the SNR level.
4. Resize the application window as needed.

## Examples
The application includes three signals, each designed to address different testing scenarios and illustrate specific features of signal sampling and recovery.

## Team Members
Hazem Rafaat

Ahmed Khaled

Omar Atef

Ibrahim Emad
