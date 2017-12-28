#!/usr/bin/python
"""
Created: 7/12/2017
Numpy doing FFT
Author:Qihao He
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft
import time

start = time.time()# Time counter

pause1 = time.time()
size = raw_input('Please input a job size:')
pause2 = time.time()

N = size # Number of points
T = 1.0 / float(size) # Spaceing between points
# if T is time/distance, 1/T is frequency/wavenumber

x = np.linspace(0, 2 * np.pi, N)
y1 = np.cos(20 * x)
y2 = np.sin(10 * x)
y3 = np.sin(5 * x)

y = y1 + y2 + y3 # Produces a random signal

fy = fft(y) # Finds the FFT
# print "original random signal array y:", y
# print "fft of x, y is:", fy

# xf = np.linspace(0.0, 1.0 / (2.0 * T), N / 2)
# plt.plot(xf,(2.0/N)*np.abs(fy[0:N/2]))
# Only half is valid. The other half is replica!

end = time.time()
print"Time elapsed:",(end - start - pause2 + pause1) # Print out time.
