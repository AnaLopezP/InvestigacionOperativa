#Max Z = 4x1 + 5x2
#Restricciones: 
# 2x1 + x2 <= 8
# x2 <= 5

import sympy as sym
from sympy import symbols
from sympy.plotting import plot

f1 = "(8-2*x)" # 2x1 + x2 <= 8 (azul abajo)
f2 = "5" # x2 <= 5 (naranja abajo)
Z1 = "(32-4*x)/5"
Z2 = "(33-4*x)/5"
Z3 = "(35-4*x)/5"

x = symbols('x')
plot(f1, f2, Z1, Z2, Z3 (x, 0, 4))