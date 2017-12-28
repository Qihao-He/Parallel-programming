#!/usr/bin/python
"""
Created: 12/27/2017
Numpy doing FFT
Author:Qihao He
"""
import numpy as np
import matplotlib.pyplot as plt
# from scipy.fftpack import fft,ifft
import time # Time library for performance measure

start = time.time() # Time counter
pause1 = time.time()
size = raw_input('Please input a job size:')
pause2 = time.time()

a = np.linspace(1., 100., size)
b = np.fft.fft(a)
# c = np.fft.ifft(b)
# print "The original array a is:", a
# print "The FFT of the original array a is b:", b
# print "The IFFT of the b is c:", c

end = time.time()
print"Time elapsed:",(end - start - pause2 + pause1) # Print out time
