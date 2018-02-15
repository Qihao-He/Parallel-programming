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
Usage = """Usage: hello_scipy_fft.py log2_N [log2_M [loops [RMS_C [ELP_C [FIG]]]]]
        log2_N = log2(FFT_length),       log2_N = 1...30
        log2_M = log2(FFT_length),       log2_M >= log2_N
        loops  = number of test repeats, loops>0,       default 1
        RMS_C = True(1), False(0),    default 0
        ELP_C = True(1), False(0),   defalt 0
        FIG = True(1), False(0),   defalt 0"""

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

RMS_C = 0
if len(sys.argv) > 4:
    RMS_C = int(sys.argv[4])

ELP_C = 0
if len(sys.argv) > 5:
    ELP_C = int(sys.argv[5])

FIG = 0
if len(sys.argv) > 6:
    FIG = int(sys.argv[6])

if (len(sys.argv) < 2 or len(sys.argv) > 7 or loops < 1):
    print(Usage)
    sys.exit()

print "The jobsize for the scipy-FFT is 2^", log2_N
print "The jobsize_end for the scipy-FFT is 2^", log2_M
print "Repeat times:", loops
print "REL_RMS_ERR", RMS_C
print "elapsed time", ELP_C
print "Figure", FIG

# array of the log2_FFT_length
log2_FFT_length = np.zeros(log2_M - log2_N, dtype = np.int) # 1D array
if RMS_C == 1:
    REL_RMS_ERR = np.zeros((loops, log2_M - log2_N), dtype = np.float64) # 2D array
if ELP_C == 1:
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
        if RMS_C == 1:
            for i in range(N):
                re = np.cos(2 * math.pi * i / N) # True solution
                tsq[0] += pow(re, 2)
                tsq[1] += pow(re - y.real[i], 2) + pow(y.imag[i], 2)
            REL_RMS_ERR[k][j] = math.sqrt(tsq[1] / tsq[0])

        end = time.time()
        if ELP_C == 1:
            time_elapsed[k][j] = end -start
    # print"repeat %i,rel_rms_err = " %k, REL_RMS_ERR[k][:]
if RMS_C == 1:
    print"rel_rms_err = ", REL_RMS_ERR
if ELP_C == 1:
    print"time_elapsed = ", time_elapsed

# plot figures
if FIG == 1:
    plt.figure(1)
    if RMS_C == 1:
        if (RMS_C == 1 and ELP_C == 1):
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
    if ELP_C == 1:
        if (RMS_C == 1 and ELP_C == 1):
            plt.subplot(212)
        plt.title('time elapsed repeat:%i' %loops)
        for k in range(loops):
            plt.scatter(log2_FFT_length, time_elapsed[k, :], c ='r', marker ='+')
        # plt.autoscale(enable=True, axis='both', tight=None)
        plt.ylim(1e-05, 1)
        plt.xlabel('log2_FFT_length: log2_N')
        plt.yscale('log')
        plt.ylabel('log scale')
        plt.grid(True)
    plt.savefig('test4.png')
    plt.show()
    # plt.close(fig)
sys.exit()
