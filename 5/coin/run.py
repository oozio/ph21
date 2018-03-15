import pymc
import model


M = pymc.MCMC(model)
M.sample(iter = 10000, burn = 0, thin = 1)
pymc.Matplot.plot(M)
M.p.summary()
