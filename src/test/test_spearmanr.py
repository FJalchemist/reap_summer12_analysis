from scipy.stats.stats import spearmanr
import numpy as np

np.random.seed()
x2n=np.random.randn(100,4)
(rho, pval) = spearmanr(x2n)
print rho
print pval