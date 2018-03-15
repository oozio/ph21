import numpy as np
from scipy import special
from scipy.stats import cauchy
import matplotlib.pyplot as plt

def hit(n,a,b):
    h = np.tan(np.random.uniform(low=np.pi/2., high=3*np.pi/2., size=n))*b+a
    return h

def lighthouse_prob(h,a,b,prior):
     logHD = []
     for hit in h:
          logHD.append(np.sum(np.log((b/(2*np.pi))/((hit - a)**2 + b**2))) + np.log(prior))
     return logHD

a = 1.
b = 1.5

prior = 1
points =300
#logHD = np.log( special.binom(n,h) * true_prob*h*(1-true_prob)**(n-h) ) + np.log(prior)

for n in [2**n for n in range(0,10)]:  
     h = hit(n,a,b)
     p_grid = np.arange(0., 1., 1. / points)
     posterior_grid = [lighthouse_prob(h,p,b,prior) for p in p_grid]
     posterior_grid -= np.max(posterior_grid) # normalize
     plt.plot(p_grid, posterior_grid)
plt.show()     


# The mean is not a good estimator since the Central Limit Theorem doesn't apply to Cauchy distributions, 
