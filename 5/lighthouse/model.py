# Import relevant modules
import pymc
import numpy as np


def hit(n,a,b):
    h = np.tan(np.random.uniform(low=np.pi/2., high=3*np.pi/2., size=n))*b+a
    return h

# Some data
n = 300
a = 1.
b = 1.5


# Priors on unknown parameters:a 
unif = pymc.Uniform('unif',lower=0.5,upper=1.5)
gauss = pymc.Normal('gauss', mu=1.0, tau=1/.01**2)

pa = unif
pb = unif
h = hit(n,a,b)

# Binomial likelihood for data
hh = pymc.Cauchy('hits', alpha = pa, beta = pb, value = h, observed=True)
