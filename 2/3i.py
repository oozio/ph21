import urllib, urllib2
import string
import re
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.fftpack import fft
import numpy as np 


N = 10000.
T = 0.001
time = np.linspace(0.00, N*T, N)
#plt.plot(time, ff)
#plt.show()

c = 1
a = 2
f = 3
b = 4
L = 5
phi = np.pi

#dt = np.linspace(0,5,5)
gauss = a*np.exp(-b*(time-L/2)/2.)
cosines = c+ a*np.cos(f*time + phi)
g = fft(gauss)
c = fft(cosines)


plt.subplot(2, 1, 1)
plt.plot(time, g)
plt.subplot(2, 1, 2)
plt.plot(time, c)
plt.show()

