from sympy import *
import numpy as np

x = Symbol('x')
y = x**6+x**5 + 1

derivada = y.diff(x)
print(derivada)