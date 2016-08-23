from rpy2 import robjects
from rpy2.robjects import pandas2ri
import numpy as np
pandas2ri.activate()

def glasso(s, rho):
    robjects.r('library(glasso)')
    cov, prec, loglik, errflg, approx, dl, niter = robjects.r['glasso'](s, rho)
    return np.array(cov), np.array(prec), loglik[0], errflg[0], approx[0], dl[0], niter[0]
