# coding: utf-8
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("mainTask",  ["mainPy.py"]),
    Extension("timeSeries",  ["lib/timeSeries.py"]),
    Extension("expPy",  ["lib/expPy.py"]),
    Extension("sqrtPy",  ["lib/sqrtPy.py"]),
#   ... all your modules that need be compiled ...
]
setup(
    name = 'ProtectingPythonProj',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)

