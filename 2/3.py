import urllib, urllib2
import string
import re
import matplotlib.pyplot as plt
import scipy.signal as signal
from scipy.fftpack import fft
import numpy as np 

url = 'http://nesssi.cacr.caltech.edu/cgi-bin/getcssconedbid_release2.cgi'
values = {'Name' : 'HER X-1',
          'Rad' : 0.3 ,
          'OUT' : 'web',
          'DB' : "photcat",
          'SHORT' : 'long'}

          
data = urllib.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

values = []
with open('/home/helen/PH21/2/arecibo1.txt','r+') as f:
     for i in f:
          values.append(float(i))
               
f = fft(values)
ff = fft(values)
maxf = max(f)
maxi = np.where(f == maxf)
print max(np.delete(f,maxi))
N = f.size
T = 0.001
time = np.linspace(0.00, N*T, N)
#plt.plot(time, ff)
#plt.show()


t0 = 0.2
dt = 0.00005
#dt = .00002
#dt = np.linspace(0.01,10.,N)
gauss = np.exp(-(time-t0)**2/dt**2)
sines = np.sin(time)
g = fft(gauss)
s = fft(sines)

gs = signal.fftconvolve(gauss,sines,mode='same')
gs = fft(gs)
plt.plot(time, gs, 'r+')
plt.plot(time, ff, 'b+')
plt.show()

