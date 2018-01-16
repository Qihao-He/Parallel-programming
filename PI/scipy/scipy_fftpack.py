#!/usr/bin/python
# import libraries
import numpy as np
import scipy as sp
from scipy.fftpack import fft, ifft

# creat a long double precision array and print datatype
a = np.linspace(1., 4., 256)
print "double float array 'a' datatype:", a.dtype

# change it to a long single precision array and print datatype
b = np.float32(a)
print "single float array 'b' datatype:", b.dtype

# do a scipy.fftpack.fft()
c = sp.fftpack.fft(b)
print "output of FFT single float complex array 'c' datatype:", c.dtype
