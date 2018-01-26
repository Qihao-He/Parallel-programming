#!/usr/bin/python
"""
Created: 1/18/2018
scipy doing FFT
Author:Qihao He
"""
# import libraries
import sys
import numpy as np
import scipy as sp
from scipy.fftpack import fft, ifft
import time

start = time.time()# Time counter
print "The jobsize for the scipy-FFT is 2^", sys.argv[1]
base = 10 #base for the input jobsize
if sys.argv[1].startswith("0x"): #if the base is hex
    base =16
try:
    jobsize = np.power(2, int(sys.argv[1], base))
except ValueError:
    print "You must supply an integer"
    sys.exit()
print "The jobsize is: " , jobsize

# T = 1.0 / float(jobsize) # Spaceing between points
# if T is time/distance, 1/T is frequency/wavenumber

x = np.linspace(0, 2 * np.pi, jobsize)
a1 = np.cos(20 * x)
a2 = np.sin(10 * x)
a3 = np.sin(5 * x)
a = a1 + a2 + a3 # Produces a random signal
# print "double float array 'a' datatype:", a.dtype

# change it to a long single precision array and print datatype
b = np.float32(a)
# print "single float array 'b' datatype:", b.dtype

# do a scipy.fftpack.fft()
c = sp.fftpack.fft(b)
# print "output of FFT single float complex array 'c' datatype:", c.dtype

end = time.time()
print"Time elapsed:",(end - start) # Print out time.
