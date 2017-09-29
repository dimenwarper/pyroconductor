from setuptools import setup
import os

setup(name='pyroconductor',
        version='0.1',
        description='High level interface to access R from python leveraging r2py.',
        author='Pablo Cordero',
        author_email='dimenwarper@gmail.com',
        url='https://github.com/dimenwarper/pyroconductor',
        packages=['pyroconductor'],
        install_requires=['numpy', 'scipy', 'rpy2', 'pandas', 'matplotlib']
        )

print('Installing some required R packages')
os.system('R CMD BATCH install-packages.R')
