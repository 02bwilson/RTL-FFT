# RTL-FFT
RTL-FFT is a program that takes data from a RTL-SDR device and shows the Fast Fourier Transform (FFT) of the data. It is written in Python 3 and uses PyQt, numpy, scipy and pyqtgraph libraries.

# Features
Real-time FFT display of the input signal
Adjustable frequency range and resolution
Adjustable window function and dynamic range
Save and load FFT data as CSV files
Export FFT plot as PNG image
Installation
To run RTL-FFT, you need to have a RTL-SDR device and its driver installed on your system. You also need to install the following Python packages:

- PyQt6
- numpy
- scipy
- pyqtgraph
- pyrtlsdr
You can install them using pip:

```pip install PyQt6 numpy scipy pyqtgraph pyrtlsdr```

# Usage
To start the program, run the start.py script:

```python3 start.py```
You will see a window with a FFT plot and some controls. You can adjust the frequency range, resolution, window function and dynamic range using the sliders and buttons. You can also save and load FFT data as CSV files using the File menu. To export the FFT plot as a PNG image, use the Export button.

# License
This project is licensed under the ozilla Public License Version 2.0 - see the LICENSE file for details.
