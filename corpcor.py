from rpy2 import robjects
from rpy2.robjects import pandas2ri
import numpy as np
pandas2ri.activate()

def cov_shrink(data_array, weights=None, **kwargs):
    robjects.r('library(corpcor)')
    if weights is None:
        res = robjects.r['cov.shrink'](data_array, **kwargs)
    else:
        res = robjects.r['cov.shrink'](data_array, w=robjects.FloatVector(weights),
                                       **kwargs)
    return np.array(res)
