from sympy import *

x = symbols('x')
f = (2*x-1)**4
y = diff(f)
print(y)
