import urllib, urllib2
import string
import re
import matplotlib.pyplot as plt
import scipy.signal as signal
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

mjd = []
mag = []
magerr = []
with open('/home/helen/PH21/1/response.txt','r+') as f:
 #    f.write(the_page)
  #   f.flush()
     for i in f:
          if re.match('^<tr>',i):
               nums = i.strip().split('<td>')
               mag.append(float(nums[2].strip("'")))
             #  print 'mag'+str(mag)
               magerr.append(float(nums[3].strip("'")))
             #  print 'magerr'+str(magerr)
               mjd.append(float(nums[6].rstrip('</tr>').strip("'")))
              # print 'mjd'+str(mjd)
               
freq = np.linspace(0.01, 10., 1000000)
pgram = signal.lombscargle(mjd, mag, freq, normalize=True)

a = []
plt.plot(freq, pgram)
plt.show()


   

