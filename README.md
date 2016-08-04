# pyroconductor

A high-level interface to access commonly-used R tools from python using the low-level r2py. Goal is to 'iron out' r2py conversion interfaces (e.g. like those provided by `pandas2ri`) and even manually create pythonic interfaces for R functions and objects that are hard to automatically translate.

Install by simply doing:

```bash
python setup.py install
```

To use `your.favorite.r.package` in a python script, simply call:

```python
import pyroconductor as pyr

pyr.your_favorite_r_package.function_in_package(args)
```
