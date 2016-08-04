from setuptools import setup

setup(name='pyroconductor',
        version='0.1',
        description='High level interface to access R from python leveraging r2py.',
        author='Pablo Cordero',
        author_email='dimenwarper@gmail.com',
        url='https://github.com/dimenwarper/pyroconductor',
        packages=['corpcor', 'glasso'],
        install_requires=['numpy', 'scipy', 'rpy2', 'pandas', 'matplotlib']
        )
