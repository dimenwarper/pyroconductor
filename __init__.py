import numpy as np
from rpy2 import robjects as ro
from rpy2.robjects import pandas2ri
from rpy2.robjects.functions import Function, SignatureTranslatedFunction
from rpy2.robjects.vectors import DataFrame, ListVector, Vector

pandas2ri.activate()

def _convert_to_python(x):
    if isinstance(x, DataFrame):
        return pandas2ri.ri2py_dataframe(x)
    elif isinstance(x, ListVector) or isinstance(x, Vector):
        return [_convert_to_python(item) for item in x]
    else:
        return np.array(x)

class R(object):
    def __getattribute__(self, attr):
        try:
            return super(R, self).__getattribute__(attr)
        except AttributeError as ae:
            orig_ae = str(ae)

        try:
            return self.__getitem__(attr)
        except LookupError:
            raise AttributeError(orig_ae)

    def __getitem__(self, item):
        res = ro.r.__getitem__(item)
        if isinstance(res, Function) or\
                isinstance(SignatureTranslatedFunction):
            return lambda *args, **kwargs: _convert_to_python(res(*args, **kwargs))
        else:
            return res
r = R()
