import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "(8-2*x)/4" # 2x1 + 4x2 <= 8 azul
f2 = "(4+x)/4" # -x1 + 4x2 <= 4 naranja
f3 = "x -2" #x1 - x2 <= 2 verde
Z1 = "(20-6*x)/3"
Z2 = "(15-6*x)/3"
Z3 = "(10-6*x)/3"
x = symbols('x')
plot(f1, f2, f3, Z1, Z2, Z3, (x, 0, 5))
#Es solución única porque la función a optimizar corta con el área óptima en un punto que optimiza las dos variables.