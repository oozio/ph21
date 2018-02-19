import urllib, urllib2
import string
import re
import matplotlib.pyplot as plt
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
  
T = 0.001    
f = np.fft.fftfreq(len(values))
ff = np.fft.fft(values).real * T
maxi = np.where(ff == max(ff))
maxf = f[maxi]
N = f.size

time = np.linspace(0.00, N, N)
plt.plot(f, ff)
#plt.show()

t0 = N/2
for dt in range(t0, 0, -t0/4):
     g = np.exp(-(time-t0)**2/dt**2)
     fg = np.fft.fft(g)
     plt.plot(f+maxf,fg.real)
    

plt.show()

