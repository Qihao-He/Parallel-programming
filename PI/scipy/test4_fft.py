#!/usr/bin/python
"""
Created: 2/14/2018
desciption:
scipy doing FFT and generate the same input array and calculate the RMS
Author:Qihao He
"""
# import libraries
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
        log2_M = log2(FFT_length),       log2_M >= log2_N
        loops  = number of test repeats, loops>0,       default 1"""

# Default values for optional arguments
log2_N = 8 #default value to be 8
if len(sys.argv) > 1:
    log2_N = int(sys.argv[1])

log2_M = log2_N + 1 #default value to be 9
if len(sys.argv) > 2:
    if int(sys.argv[2]) <= int(sys.argv[1]):
        print(Usage)
        sys.exit()
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

# array of the log2_FFT_length
log2_FFT_length = np.zeros(log2_M - log2_N, dtype = np.int) # 1D array
REL_RMS_ERR = np.zeros((loops, log2_M - log2_N), dtype = np.float64) # 2D array
time_elapsed = np.zeros((loops, log2_M - log2_N), dtype = np.float64) # 2D array

for i in range(0, log2_M - log2_N):
    log2_FFT_length[i] = i + log2_N
# print "log2_FFT_length:", log2_FFT_length

for k in range(loops):
    for j in range(log2_M - log2_N):
        start = time.time()# Time counter

        N = 1 << int(log2_FFT_length[j]) #fft length
        # input buffer
        x = np.zeros((N, ), dtype = np.complex64)
        x.real[1] = x.real[N - 1] = np.float32(0.5)
        # x =  np.zeros((N, ), dtype = np.float64)
        tsq = np.zeros((2, 1), dtype = np.float64)

        # fft execute
        y = fft(x)

        # output buffer and rel_rms_err
        for i in range(N):
            re = np.cos(2 * math.pi * i / N) # True solution
            tsq[0] += pow(re, 2)
            tsq[1] += pow(re - y.real[i], 2) + pow(y.imag[i], 2)
        REL_RMS_ERR[k][j] = math.sqrt(tsq[1] / tsq[0])

        end = time.time()
        time_elapsed[k][j] = end -start
    # print"repeat %i,rel_rms_err = " %k, REL_RMS_ERR[k][:]
print"rel_rms_err = ", REL_RMS_ERR
print"time_elapsed = ", time_elapsed

# plot figures
plt.figure(1)
plt.subplot(211)
plt.title('REL_RMS_ERR repeat:%i' %loops)
for k in range(loops):
    plt.scatter(log2_FFT_length, REL_RMS_ERR[k, :], c ='b', marker ='o')
plt.autoscale(enable=True, axis='both', tight=None)
plt.xlabel('log2_FFT_length: log2_N')
plt.ylim(1e-07, 3e-07)
plt.yscale('symlog')
plt.ylabel('symetric log scale base epsilon')
plt.grid(True)


plt.subplot(212)
plt.title('time elapsed repeat:%i' %loops)
for k in range(loops):
    plt.scatter(log2_FFT_length, time_elapsed[k, :], c ='r', marker ='+')
plt.autoscale(enable=True, axis='both', tight=None)
plt.xlabel('log2_FFT_length: log2_N')
plt.yscale('log')
plt.ylabel('log scale')
plt.grid(True)

plt.show()
sys.exit()
