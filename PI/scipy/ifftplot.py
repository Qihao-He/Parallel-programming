#!/usr/bin/python
import numpy as np
from scipy.fftpack import ifft
import matplotlib.pyplot as plt
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
print "x array:", x
xf = np.linspace(0, 1, 5)
y = np.array([ 4.50000000+0.j        ,  2.08155948-1.65109876j,
       -1.83155948+1.60822041j, -1.83155948-1.60822041j,
        2.08155948+1.65109876j])
yinv = ifft(y)
print "yinv", yinv
plt.plot(xf, y)
plt.grid()
plt.show()
