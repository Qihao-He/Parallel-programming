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
import time

start = time.time()# Time counter

# Usage
    "Usage: scipy_fft_modifited log2_N [loops]\n"
    "log2_N = log2(FFT_length),       log2_N = 8...22\n"
    "loops  = number of test repeats, loops>0,       default 1\n";

print "The jobsize for the scipy-FFT is 2^", int(sys.argv[1])
print "Repeat times:", int(sys.argv[2])
int(N) = sys.argv[1]<<1 #fft length
int(loops) = sys.argv[2] #test repetitions

base = 10 #base for the input jobsize
if sys.argv[1].startswith("0x"): #if the base is hex
    base =16
try:
    jobsize = np.power(2, int(sys.argv[1], base))
except ValueError:
    print "You must supply an integer"
    sys.exit()

print "The jobsize is: " , jobsize


for k in range(0,loops)
# input buffer

# execute the fft
c = sp.fftpack.fft(b)

# output buffer

# rel_rms_err, time, repeat times

end = time.time()
print"Time elapsed:",(end - start) # Print out time.
