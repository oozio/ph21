import pymc
import model


M = pymc.MCMC(model)
M.sample(iter = 100000, burn = 8000, thin = 80)
pymc.Matplot.plot(M)
M.alpha.summary()
M.beta.summary()
