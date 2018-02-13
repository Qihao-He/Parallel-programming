#!/usr/bin/python
"""
Created: 2/9/2018
desciption:
scipy doing FFT and generate the same input array and calculate the RMS
Author:Qihao He
"""
# import libraries
import sys
import numpy as np
import scipy as sp
import math
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import time

start = time.time()# Time counter

# Usage
Usage = """Usage: hello_scipy_fft.py log2_N [loops]
        log2_N = log2(FFT_length),       log2_N = 1...30
        loops  = number of test repeats, loops>0,       default 1"""

# Default values for optional arguments
log2_N = 8 #default value to be 8
if len(sys.argv) > 1:
    log2_N = int(sys.argv[1])
print "The jobsize for the scipy-FFT is 2^", log2_N

loops = 1 #default value to be 1
if len(sys.argv) > 2:
    loops = int(sys.argv[2])
print "Repeat times:", loops

if (len(sys.argv) < 2 or len(sys.argv) > 3 or loops < 1):
    print(Usage)
    sys.exit()

N = int(sys.argv[1])<<1 #fft length
print "The fft length is:", N

powerbase = 10 #base for the input jobsize
if sys.argv[1].startswith("0x"): #if the base is hex
    powerbase =16
try:
    jobsize = np.power(2, int(sys.argv[1], powerbase))
except ValueError:
    print(Usage)
    sys.exit()

print "The jobsize is: ", jobsize

for k in range(0, loops):
    # input buffer
    base_total = np.zeros((N, 1), dtype = np.complex64)
    base_total.real[1] = base_total.real[N - 1] = np.float32(0.5)
    # print "base_total.real:", base_total.real
    # print "base_total.imag:", base_total.imag
    print "input buffer base_total:", base_total, base_total.dtype

    # execute the ifft
    inversefft = sp.fftpack.ifft(base_total)
    print "ifft is:", inversefft, inversefft.dtype

    # output buffer
    tsq = np.zeros((2, 1), dtype = np.complex64)
    for i in range(N):
        re = np.cos(2 * math.pi * i / N)
        tsq[0] += pow(re, 2)
        tsq[1] += pow(re - inversefft.real[i], 2) + pow(inversefft.imag[i], 2)
    print "re", re, re.dtype

    # rel_rms_err
    print"rel_rms_err = ", math.sqrt(tsq[1]/tsq[0])

end = time.time()
print"Time elapsed:",(end - start) # Print out time.
