#!/usr/bin/python
"""
Created: 2/14/2018
desciption:
scipy doing FFT and calcualte Relative RMS
Author:Qihao He
"""
# import libraries
import sys
import gc
import numpy as np
import scipy as sp
import math
from scipy.fftpack import ifft2, fft2
import time


# Usage
Usage = """Usage: hello_scipy_fft.py log2_N [log2_M [loops [RMS_C]]]
        log2_N = log2(FFT_length),       log2_N = 8...11
        log2_M = log2(FFT_length),       log2_M > log2_N
        loops  = number of test repeats, loops>0,       default 1
        RMS_C = True(1), False(0),    default 0"""

# Default values for optional arguments
log2_N = 8 #default value to be 8
if len(sys.argv) > 1:
    log2_N = int(sys.argv[1])

log2_M = log2_N + 1 #default value to be 9
if len(sys.argv) > 2:
    log2_M = int(sys.argv[2])

loops = 1 #default value to be 1
if len(sys.argv) > 3:
    loops = int(sys.argv[3])

RMS_C = 0
if len(sys.argv) > 4:
    RMS_C = int(sys.argv[4])

if (not 2 <= len(sys.argv) <= 5 or log2_M <= log2_N  or loops < 1 or not
0 <= RMS_C <= 1):
    print(Usage)
    sys.exit()

span_N = log2_M - log2_N
if RMS_C == 1:
    REL_RMS_ERR = np.zeros((span_N, loops), dtype = np.float64) # 2D array

print "log2_N,","Init_T,","FFT_T,","RMS_T,","Total_T"
gc.enable()
print gc.isenabled()
for l in range(span_N):
    log2_P = l + log2_N
    N = 1 << log2_P #fft length
    for k in range(loops):
        t0 = time.time()# Time counter
        # input buffer
        x = np.zeros((N, N), dtype = np.complex64)
        # print "refcount:",sys.getrefcount(x)
        x.real[0,0] = np.float32(1)

        # fft execute
        t1 = time.time()
        y = fft2(x)
        t2 = time.time()

        # output buffer and rel_rms_err
        if RMS_C == 1:
            tsq0 = 0
            tsq1 = 0
            tsq0 = N * N
            for i in range(N):
                for j in range(N):
                    a = 1 - y.real[i][j]
                    b = y.imag[i][j]
                    tsq1 += a * a + b * b
            REL_RMS_ERR[l][k] = math.sqrt(tsq1 / tsq0)

        t3 = time.time()
        print  log2_P,",",t1 - t0,",",t2 - t1,",",t3 - t2,",",t3 - t0
        print gc.get_count()
        gc.collect()

if RMS_C == 1:
    print"rel_rms_err = ", REL_RMS_ERR
