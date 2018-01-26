#!/usr/bin/python
"""
Created: 1/16/2018
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

# creat a long double precision array and print datatype
a = np.linspace(1., 4., jobsize)
# print "double float array 'a' datatype:", a.dtype

# change it to a long single precision array and print datatype
b = np.float32(a)
# print "single float array 'b' datatype:", b.dtype

# do a scipy.fftpack.fft()
c = sp.fftpack.fft(b)
# print "output of FFT single float complex array 'c' datatype:", c.dtype

end = time.time()
print"Time elapsed:",(end - start) # Print out time.
