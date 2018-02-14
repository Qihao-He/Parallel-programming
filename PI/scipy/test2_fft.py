#!/usr/bin/python
import sys
import numpy as np
import math
from scipy.fftpack import ifft, fft
import matplotlib.pyplot as plt
import matplotlib.axes as axes
import time

# start = time.time()# Time counter
# array of the FFT_length
FFT_length = np.zeros(int(sys.argv[2])-int(sys.argv[1]), )
REL_RMS_ERR = np.zeros(int(sys.argv[2])-int(sys.argv[1]), )
duration = np.zeros(int(sys.argv[2])-int(sys.argv[1]), )
for i in range(int(sys.argv[1]), int(sys.argv[2])):
    FFT_length[i-int(sys.argv[1])] = i
# print "FFT_length:", FFT_length

for j in range(int(sys.argv[2])-int(sys.argv[1])):
    start = time.time()# Time counter

    N = 1 << int(FFT_length[j]) #fft length
    xf = np.linspace(0, 1, N)
    x =  np.zeros((N, ), dtype = np.float64)
    tsq = np.zeros((2, 1), dtype = np.float64)
    for i in range(N):
        x[i] = np.cos(2 * math.pi * i / N)
        tsq[0] += pow(x[i], 2)
    y = fft(x)
    yinv = ifft(y)
    for i in range(N):
        tsq[1] += pow(x[i] - yinv.real[i], 2) + pow(yinv.imag[i], 2)
    # rel_rms_err
    REL_RMS_ERR[j] = math.sqrt(tsq[1] / tsq[0])
    # print"rel_rms_err = ", REL_RMS_ERR[j]

    end = time.time()
    duration[j] = end -start

plt.figure(1)
plt.title('rel_rms_err')
plt.scatter(FFT_length, REL_RMS_ERR)
axes.Axes.autoscale(enable = True, axis = 'both')

plt.grid()
plt.show()


plt.figure(2)
plt.title('time')
plt.scatter(FFT_length, duration)
axes.Axes.autoscale(enable = True, axis = 'both')

plt.grid()
plt.show()
# plt.subplot(311)
# plt.scatter(xf, x, c ='b', marker ='.')
# plt.ylabel('FFT Input time domain')
#
# plt.subplot(312)
# plt.scatter(xf, y,  c ='r', marker ='+')
# plt.ylabel('FFT output Frequency domain')
#
# plt.subplot(313)
# plt.scatter(xf, yinv,  c ='g', marker ='o')
# plt.ylabel('IFFT output time domain')
