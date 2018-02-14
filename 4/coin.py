import numpy as np
from scipy import special
import matplotlib.pyplot as plt

true_prob = 0.5  
#n = np.linspace(1, 10000, 10000)
#prior = 2 
prior = np.random.normal(loc=0.5, scale = 0.1)

maxh = 100
HD = []
n = 150
h = np.linspace(1, maxh, maxh)
for i in range(0, maxh):
     prior = np.random.normal(loc=0.5,scale=0.1)
     HD.append(special.binom(n,h[i])*true_prob**h[i]*(1-true_prob)**(n-h[i])* prior)
     
plt.plot(h, HD)
plt.title('H='+str(true_prob)+";n="+str(n))
plt.ylabel("prob H|D")
plt.xlabel("h")
plt.savefig('H='+str(true_prob)+";n="+str(n)+'.jpg')
