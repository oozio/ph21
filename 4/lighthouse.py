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
prior = 1
points =100

prior = np.exp( -(true_prob-1.5)**2 / (2 * 0.1**2) )

#for n in [2**n for n in range(0,10,2)]:   
#     h = hit(n,a,b)
#     x = np.arange(0., 2., 2. / points)
#     posteriors = [lighthouse_prob(len(h),p,b,prior) for p in x]
 #    posteriors -= np.max(posteriors) 
 #    plt.plot(x, posteriors,label='n = '+str(n))  
 #    plt.ylim(-5,5)
#plt.legend()
#plt.savefig('unif.png')
#plt.show()     


for n in [2**n for n in range(0,10,2)]:    
     h = hit(n,a,b)
     x = np.arange(0., 2., 2. / points)
     x1 = np.arange(0.,2.,2./points)
     posteriors = [[lighthouse_prob(len(h),p,p1,prior) for p in x] for p1 in x1]
     posteriors -= np.max(posteriors) 
     i = plt.imshow(posteriors,extent=[0.0, 2.0, 0.0, 2.0])
    # i.set_cmap('rainbow')
 #    plt.ylim(0,2)
     plt.colorbar()
     plt.savefig('gauss_1sigma_n='+str(n)+'.png')     
  #   display.clear_output(wait=True)
     plt.figure().clear()
# The mean is not a good estimator since the Central Limit Theorem doesn't apply to Cauchy distributions, 





















