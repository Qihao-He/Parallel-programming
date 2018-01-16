#!/usr/bin/python
"""
Created: 1/16/2018
scipy doing FFT
Author:Qihao He
"""
# import libraries
import numpy as np
import scipy as sp
from scipy.fftpack import fft, ifft
import time

start = time.time()# Time counter

pause1 = time.time()
jobsize = raw_input('Please input a job size:')
pause2 = time.time()

# jobsize = 256
# print "jobsize of the array:", jobsize

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
print"Time elapsed:",(end - start - pause2 + pause1) # Print out time.
