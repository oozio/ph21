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
alpha = pymc.Uniform('pa',lower=0.0,upper=2.0)
#alpha = pymc.Normal('pa', mu=1.0, tau=1/.3**2)

beta = pymc.Uniform('pb',lower=0.0,upper=2.0)
#beta = pymc.Normal('pb', mu=1.0, tau=1/.3**2)

h = hit(n,a,b)

# Binomial likelihood for data
hh = pymc.Cauchy('hits', alpha = alpha, beta = beta, value = h, observed=True)
