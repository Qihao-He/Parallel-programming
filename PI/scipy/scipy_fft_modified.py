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
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
import time

start = time.time()# Time counter

# Usage
Usage = """Usage: scipy_fft_modifited log2_N [loops]
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

if (len(sys.argv) < 2 or len(sys.argv) >3 or loops < 1):
    print(Usage)
    sys.exit()

N = int(sys.argv[1])<<1 #fft length
print "The fft length is:", N

base = 10 #base for the input jobsize
if sys.argv[1].startswith("0x"): #if the base is hex
    base =16
try:
    jobsize = np.power(2, int(sys.argv[1], base))
except ValueError:
    print(Usage)
    sys.exit()

print "The jobsize is: " , jobsize

for k in range(0,loops):
    # input buffer

    # execute the ifft
    # c = sp.fftpack.fft(b)

    # output buffer

    # rel_rms_err, time, repeat times
    # print

end = time.time()
print"Time elapsed:",(end - start) # Print out time.
