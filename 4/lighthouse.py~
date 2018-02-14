import numpy as np
from scipy import special
from scipy.stats import cauchy
import matplotlib.pyplot as plt


n = 500
a = 1000.
b = 1000.

xks = np.tan(np.random.uniform(low=-np.pi/2., high=np.pi/2., size=n))*b+a

prior = 1./a

logHD = []
c = b/np.pi * ((xks-a)**2+b**2)

logHD = ( np.log(c) + np.log(prior)          )
print np.exp(np.mean(logHD))
print np.exp(np.median(logHD))

h = np.linspace(1, a, a)     
plt.plot(h[::2], logHD, 'r+')
#plt.title("n="+str(n))
plt.ylabel("prob H|D")
plt.xlabel("a")
#plt.savefig('H='+str(true_prob)+";n="+str(n)+'.jpg')
plt.show()


# The mean is not a good estimator since the Central Limit Theorem doesn't apply to Cauchy distributions, 
