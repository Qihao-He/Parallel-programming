#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 14:45:09 2017

@author: qihaohe
"""
# Time library for performance measure
import time
# Time counter
start = time.time()

# Do something
a=1+2+3+4+5+6+7+8+9
b=([0,1,2,3,4,5,6,7,8,9])
print("hello")
print "a sum of 1 to 9 is: ", a
print "b list of array is: ", b

end = time.time()
# Print out time.
print(end - start)
