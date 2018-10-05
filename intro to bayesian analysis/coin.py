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
     
true_prob = 0.8  
prior = 1.
#prior = np.exp( -(true_prob-0.7)**2 / (2 * 0.05**2) )
points = 100

for n in [2**n for n in range(0,10,2)]:     
     h = heads(n, true_prob)
     p_grid = np.arange(0., 1., 1. / points)
     posterior_grid = [coin_prob(h,prior,p) for p in p_grid]
     posterior_grid -= np.max(posterior_grid) # normalize
     plt.plot(p_grid, posterior_grid, label='n = '+str(n))#label='guessed true_probability = '+ str(p))
     plt.ylim(-5,5)
plt.legend()
plt.savefig('coin_unif.png')     
#plt.savefig('H='+str(true_prob)+";n="+str(n)+'.jpg')
