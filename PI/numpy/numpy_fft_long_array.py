"""
Created: 12/27/2017
Numpy doing FFT
Author:Qihao He
"""
#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft
# Time library for performance measure
import time
# Time counter
start = time.time()


N = 64 # Number of points
T = 1 / 64.0 # Spaceing between points
# if T is time/distance, 1/T is frequency/wavenumber

x = np.linspace(0, 2 * np.pi * N * T, N)
y1 = np.cos(20 * x)
y2 = np.sin(10 * x)
y3 = np.sin(5 * x)

y = y1 + y2 + y3 # Produces a random signal

fy = fft(y) # Finds the FFT
xf = np.linspace(0.0, 1.0 / (2.0 * T), N / 2)

end = time.time()
# Print out time.
print"Time elapsed:",(end - start)

#plt.plot(xf,(2.0/N)*np.abs(fy[0:N/2]))
# Only half is valid. The other half is replica!
