import urllib, urllib2
#import urllib
import string
import re
import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np
from astropy.stats import LombScargle
from astropy import units as u
from astropy.time import Time
url = 'http://nesssi.cacr.caltech.edu/cgi-bin/getcssconedbid_release2.cgi'
values = {'Name' : 'HER X-1',
          'Rad' : 0.3 ,
          'OUT' : 'web',
          'DB' : "photcat",
          'SHORT' : 'long'}

          
data = urllib.urlencode(values)
#data = urllib.parse.urlencode(values)
#data = data.encode('ascii') # data should be bytes
req = urllib2.Request(url, data)
#req = urllib.request(url,data)
response = urllib2.urlopen(req)
#response = urllib.request.urlopen(url,data)
the_page = response.read()

mjd = []
mag = []
magerr = []
with open('/home/helen/PH21/1/response.txt','r+') as f:
 #    f.write(the_page)
  #   f.flush()
     for i in   f:
          if re.match('^<tr>',i):
               nums = i.strip().split('<td>')
               mag.append(float(nums[2].strip("'")))
             #  print 'mag'+str(mag)
               magerr.append(float(nums[3].strip("'")))
             #  print 'magerr'+str(magerr)
               mjd.append(float(nums[6].rstrip('</tr>').strip("'")))
              # print 'mjd'+str(mjd)
          
          
mjd = np.array(mjd)
mag = np.array(mag)
#mjd = Time(mjd,format='mjd')
#mjd = mjd.gps
frequency = np.linspace(0.4, 0.6, 1000)
power = LombScargle(mjd, mag,magerr).power(frequency)
#print frequency[np.argmax(power)]  

#plt.plot(frequency, power)
#plt.xlabel('freq')
#plt.ylabel('power')
#plt.savefig('uneven.png')

c = 1
a = 2
f = 3
b = 0.4
L = 50
phi = np.pi


frequency = np.linspace(0.9, 1.1, 1000)
time = np.arange(0., L, b)
gauss = a*np.exp(-b*(time-(L/2))**2)+1
power = LombScargle(gauss, time).power(frequency)
   
#plt.plot(frequency, power)
#plt.xlabel('freq')
#plt.ylabel('power')
#plt.savefig('gauss.png')

ns =[]
with open('/home/helen/PH21/2/arecibo1.txt','r+') as f:
     for i in f:
          ns.append(float(i))
frequency = np.linspace(0.9, 1.1, 1000)
N = len(ns)
time = np.linspace(0.00, N, N)
power = LombScargle(ns, time).power(frequency)
   
plt.plot(frequency, power)
plt.xlabel('freq')
plt.ylabel('power')
plt.savefig('arescibo.png')




