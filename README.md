# Sampling-Theory Studio

- [Overview](#overview)
- [Features](#features)
- [Informatio-for-the-user](#information-for-the-user)
- [Run-App](#run-app)
- [Team-Members](#team-members)

## Overview
This desktop application is designed to illustrate the importance of the Nyquist-Shannon sampling theorem in digital signal processing. It allows users to load, sample, and recover analog signals, showing how different sampling frequencies affect signal recovery. our application offers the ability to mix, add noise, and perform real-time sampling and recovery.

## Features

### 1. Sample & Recover
- **Sample Signal**: Load a signal and visualize it. Users can sample it at various frequencies.
- **Recover Signal**: The application uses the Whittaker-Shannon interpolation formula to recover the original signal based on the sampled points.
- **Visualization**: Three graphs display the original signal with markers for sampled points, the reconstructed signal, and the difference between the original and reconstructed signals.

### 2. Load & Compose
- **Load Signal**: Users can load a signal from a file or create a custom signal by mixing multiple sinusoidal components with different frequencies and magnitudes.
- **Signal Mixer**: The signal mixer allows users to add and remove single sinusoidal components to prepare a mixed signal.

### 3. Additive Noise
- **Noise Addition**: Users can introduce custom noise with a controllable Signal-to-Noise Ratio (SNR) level.

### 4. Responsive UI
- The application is designed to be easily resizable without affecting the UI.


## Information for the user
To use the application, follow these steps:

1. Load a signal or create a custom signal using the Signal Mixer.
2. Adjust the sampling frequency in real-time and observe the effects on signal recovery.
3. add noise to the signal and control the SNR level.

## Run-App

1. **_install project dependencies_**
```sh
pip install -r requirements.txt
```
2. **_Run the application_**
```sh
python main.py
```

<tr>
    <td align="center">
      <a href="https://github.com/OmarAtef0" target="_black">
      <img src="https://avatars.githubusercontent.com/u/131784941?v=4" width="150px;" alt="Omar Atef"/>
      <br />
      <sub><b>Omar Atef</b></sub></a>
    </td>  
    <td align="center">
      <a href="https://github.com/IbrahimEmad11" target="_black">
      <img src="https://avatars.githubusercontent.com/u/110200613?v=4" width="150px;" alt="Omar Atef"/>
      <br />
      <sub><b>Ibrahim Emad</b></sub></a>
    </td>  
    <td align="center">
      <a href="https://github.com/Hazem-Raafat" target="_black">
      <img src="https://avatars.githubusercontent.com/u/100636693?v=4" width="150px;" alt="Omar Atef"/>
      <br />
      <sub><b>Hazem Rafaat</b></sub></a>
    </td>  
    <td align="center">
      <a href="https://github.com/Ahmedkhaled222" target="_black">
      <img src="https://avatars.githubusercontent.com/u/109425772?v=4" width="150px;" alt="Omar Atef"/>
      <br />
      <sub><b>Ahmed Khaled</b></sub></a>
    </td>  
  </tr>
