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
a_int = 1.1
b_int = 1.5

# Priors on unknown parameters:a 
#unif = pymc.Uniform('unif',lower=0.0,upper=1.0)
gauss = pymc.Normal('gauss', mu=0.5, tau=1/.01**2)

pa = gauss
pb = gauss

h = hit(n,a,b)+hit(n,a_int,b_int)

# Binomial likelihood for data
hh = pymc.Cauchy('hits', alpha = pa, beta = pb, value = h, observed=True)
