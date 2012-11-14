from scipy.stats.stats import spearmanr
import numpy as np

np.random.seed()
x2n=np.random.randn(4,100)
print np.shape(x2n)

(rho, pval) = spearmanr(x2n, axis=1)
print rho
print pval