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
# print "This is the name of the script: ", sys.argv[0]
print "The jobsize for the FFT is: ", sys.argv[1]
# print "Number of arguments: ", len(sys.argv)
# print "The arguments are: " , str(sys.argv)
jobsize = sys.argv[1]

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
print"Time elapsed (Without user input):",(end - start) # Print out time.
