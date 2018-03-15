import numpy as np
from scipy import special
import matplotlib.pyplot as plt


def heads(n, true_prob):
    h = 0
    for i in range(0, n):
        if np.random.random() < true_prob:
            h += 1
    return h

def coin_prob(h,prior,true_prob):
     logHD = np.log(special.binom(n,h)*true_prob**h*(1-true_prob)**(n-h)) + np.log(prior)
     return logHD
     
true_prob = 0.4  
#prior = 1
prior = np.exp( -(true_prob-0.5)**2 / (2 * 0.1**2) )
points = 300

for n in [2**n for n in range(0,10)]:     
     h = heads(n, true_prob)
     p_grid = np.arange(0., 1., 1. / points)
     posterior_grid = [coin_prob(h,prior,p) for p in p_grid]
     posterior_grid -= np.max(posterior_grid) # normalize
     print len(posterior_grid)
     plt.plot(p_grid, posterior_grid)
plt.show()     
#plt.savefig('H='+str(true_prob)+";n="+str(n)+'.jpg')
