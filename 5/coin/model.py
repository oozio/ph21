# Import relevant modules
import pymc
import numpy as np

def heads(n, true_prob):
    h = 0
    for i in range(0, n):
        if np.random.random() < true_prob:
            h += 1
    return h

# Some data
n = 300
true_prob = 0.4

# Priors on unknown parameters
unif = pymc.Uniform('unif',lower=0.3,upper=0.5)
gauss = pymc.Normal('gauss', mu=0.4, tau=1/.01**2)

p = unif
h = heads(n,true_prob)
# Binomial likelihood for data
hh = pymc.Binomial('heads', n=n, p=p, value=h,observed=True)
