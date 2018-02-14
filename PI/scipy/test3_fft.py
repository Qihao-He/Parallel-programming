#!/usr/bin/python
import sys
import numpy as np
import scipy as sp
import math
from scipy.fftpack import ifft, fft
import matplotlib.pyplot as plt
import matplotlib.axes as axes
from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import time

# Usage
Usage = """Usage: hello_scipy_fft.py log2_N [log2_M [loops]]
        log2_N = log2(FFT_length),       log2_N = 1...30
        log2_M = log2(FFT_length),       log2_M =>log2_N
        loops  = number of test repeats, loops>0,       default 1"""

# Default values for optional arguments
log2_N = 8 #default value to be 8
if len(sys.argv) > 1:
    log2_N = int(sys.argv[1])

log2_M = log2_N + 1 #default value to be 8
if len(sys.argv) > 2:
    log2_M = int(sys.argv[2])

loops = 1 #default value to be 1
if len(sys.argv) > 3:
    loops = int(sys.argv[3])

if (len(sys.argv) < 2 or len(sys.argv) > 4 or loops < 1):
    print(Usage)
    sys.exit()
print "The jobsize for the scipy-FFT is 2^", log2_N
print "The jobsize_end for the scipy-FFT is 2^", log2_M
print "Repeat times:", loops

# array of the FFT_length
FFT_length = np.zeros(log2_M - log2_N, )
REL_RMS_ERR = np.zeros(log2_M - log2_N, )
duration = np.zeros(log2_M - log2_N, )

for i in range(0, log2_M - log2_N):
    FFT_length[i] = i + log2_N
# print "FFT_length:", FFT_length

for j in range(log2_M - log2_N):
    start = time.time()# Time counter

    N = 1 << int(FFT_length[j]) #fft length
    xf = np.linspace(0, 1, N)

    # input buffer
    x =  np.zeros((N, ), dtype = np.float64)
    tsq = np.zeros((2, 1), dtype = np.float64)
    for i in range(N):
        x[i] = np.cos(2 * math.pi * i / N)
        tsq[0] += pow(x[i], 2)

    # fft and ifft
    y = fft(x)
    yinv = ifft(y)

    # output buffer
    for i in range(N):
        tsq[1] += pow(x[i] - yinv.real[i], 2) + pow(yinv.imag[i], 2)
    # rel_rms_err
    REL_RMS_ERR[j] = math.sqrt(tsq[1] / tsq[0])
    # print"rel_rms_err = ", REL_RMS_ERR[j]

    end = time.time()
    duration[j] = end -start


# plot figures
plt.figure(1)
plt.subplot(211)
plt.title('rel_rms_err')
plt.scatter(FFT_length, REL_RMS_ERR, c ='b', marker ='.')
plt.yscale('symlog')
plt.ylabel('symetric log scale')
plt.grid(True)
# axes.Axes.autoscale(enable = True, axis = 'both')

# plt.figure(2)
plt.subplot(212)
plt.title('time')
plt.scatter(FFT_length, duration, c ='r', marker ='+')
plt.yscale('log')
plt.ylabel('log scale')
plt.grid(True)
# axes.Axes.autoscale(enable = True, axis = 'both')
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
