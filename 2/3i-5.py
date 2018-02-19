import urllib, urllib2
import string
import re
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.fftpack import fft
import numpy as np 


c = 1
a = 2
f = 3
b = 0.4
L = 50
phi = np.pi

time = np.arange(0., L, b)
#plt.plot(time, ff)
#plt.show()



#dt = np.linspace(0,5,5)
gauss = a*np.exp(-b*(time-(L/2))**2)
cosines = c+ a*np.cos(f*time + phi)

name = 'cosines'
plt.plot(time,cosines)
plt.savefig(name+'_original.png')
plt.show()

ff = np.fft.fft(cosines)
fi = np.fft.ifft(ff)
f = np.fft.fftfreq(time.size,b)
#     plt.subplot(2, 1, 1)
plt.plot(f, ff.real)
plt.savefig(name+'_fft.png')
plt.show()
#    plt.subplot(2, 1, 2)
plt.plot(f, fi.real)
plt.savefig(name+'_inverse_fft.png')
plt.show()


name = 'gauss'
plt.plot(time,gauss)
plt.savefig(name+'_original.png')
plt.show()

ff = np.fft.fft(gauss)
fi = np.fft.ifft(ff)
f = np.fft.fftfreq(time.size,b)
#     plt.subplot(2, 1, 1)
plt.plot(f, ff.real)
plt.savefig(name+'_fft.png')
plt.show()
#    plt.subplot(2, 1, 2)
plt.plot(f, fi.real,'+')
plt.savefig(name+'_inverse_fft.png')
plt.show()

