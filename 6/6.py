from numpy import cov
from numpy import linalg #.eig
import numpy as np


n = 10

x = range(n) + np.random.uniform(low=0.0, high=0.5,size=n)
y = [(2. + 1.5*xi)+np.random.normal(0.1,0.05) for xi in x] 
xy = np.array([x,y])

for row in xy:
     row = row - np.mean(row)

c = cov(xy)
ev = linalg.eig(c)[0]
evs = linalg.eig(c)[1]

P = np.transpose(evs)

for i in range(0,n):
     print 'x: '+str(x[i])+ ' y: ' + str(y[i])
for i in range(0,len(ev)):
     print 'eigenvalue: '+ str(ev[i]) + '; p.v.: ' + str(P[i])
     

print '-----------------------------------------------------'
y1 = [(0.2 + 1.1*xi)+np.random.normal(1,0.5) for xi in x] 
y2 = [(3. + 0.15*xi)+np.random.normal(1,0.5) for xi in x] 
y3 = [(np.pi + 0.7*xi)+np.random.normal(1,0.5) for xi in x] 

xy1 = np.array([x,y1,y2,y3])
for row in xy1:
     row = row - np.mean(row)
c1 = cov(xy1)
ev1 = linalg.eig(c1)[0]
evs1 = linalg.eig(c1)[1]
P1 = np.transpose(evs1)



for i in range(0,n):
     print 'x: '+str(x[i])+ ' y1: ' + str(y1[i])+ ' y2: ' + str(y2[i])+ ' y4: ' + str(y3[i])

for i in range(0,len(ev1)):
     print 'eigenvalue: '+ str(ev1[i]) + '; p.v.: ' + str(P1[i])










