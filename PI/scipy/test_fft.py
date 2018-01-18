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
# print "This is the name of the script: ", sys.argv[0]
print "The jobsize for the scipy-FFT is: ", sys.argv[1]
# print "Number of arguments: ", len(sys.argv)
# print "The arguments are: " , str(sys.argv)
jobsize = sys.argv[1] # Number of points

# T = 1.0 / float(jobsize) # Spaceing between points
# if T is time/distance, 1/T is frequency/wavenumber

x = np.linspace(0, 2 * np.pi, jobsize)
a1 = np.cos(20 * x)
a2 = np.sin(10 * x)
a3 = np.sin(5 * x)
a = a1 + a2 + a3 # Produces a random signal
print "double float array 'a' datatype:", a.dtype

# change it to a long single precision array and print datatype
b = np.float32(a)
print "single float array 'b' datatype:", b.dtype

# do a scipy.fftpack.fft()
c = sp.fftpack.fft(b)
print "output of FFT single float complex array 'c' datatype:", c.dtype

end = time.time()
print"Time elapsed:",(end - start) # Print out time.
