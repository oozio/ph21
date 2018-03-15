import numpy as np
from scipy import special
from scipy.stats import cauchy
import matplotlib.pyplot as plt

def hit(n,a,b):
     h = []
     angle = [np.random.uniform(0, 2*np.pi) for i in range(0, n)]
     for an in angle:
          if an < np.pi/2 or an > 3*np.pi/2:
               h.append(b*np.tan(an) + a)
     return h

def lighthouse_prob(hits,a,b,prior):
     logHD = (np.sum(np.log((b/(2*np.pi))/((h - a)**2 + b**2))) + np.log(prior))
     return logHD

   
a = 1.
b = 1.5
true_prob = 0.4
#prior = 1
points =300
#logHD = np.log( special.binom(n,h) * true_prob*h*(1-true_prob)**(n-h) ) + np.log(prior)

prior = np.exp( -(true_prob-0.5)**2 / (2 * 0.01**2) )

for n in [2**n for n in range(0,5)]:   
     h = hit(n,a,b)
#     print h
     x = np.arange(0., 2., 2. / points)
     posteriors = [lighthouse_prob(len(h),p,b,prior) for p in x]
   #  posteriors -= np.max(posteriors) 
 #    print len(posteriors)
     plt.plot(x, posteriors)  
plt.legend()
plt.show()     


for n in [2**n for n in range(0,5)]:    
     h = hit(n,a,b)
     x = np.arange(0., 2., 2. / points)
     x1 = np.arange(0.,2.,2./points)
     posteriors = [[lighthouse_prob(len(h),p,p1,prior) for p in x] for p1 in x1]
     #posteriors -= np.max(posteriors) 
     plt.contourf(x,x1,posteriors)
#     plt.plot(x, posteriors)  
plt.colorbar()
plt.show()     

# The mean is not a good estimator since the Central Limit Theorem doesn't apply to Cauchy distributions, 





















