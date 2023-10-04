import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" # x2 + x1 <= 10
f2 = "1+x" # x1 - x2 <= 1
f3 = "4" #x2 <= 4
Z1 = "(16-x)/2"
Z2 = "(14-x)/2"
Z3 = "(13-x)/2"
x = symbols('x')
plot(f1, f2, f3, Z1, Z2, Z3, (x, -15, 15))
# Sol: Z=14 x1=5 x2=5 solución única
#El área óptima es la parte de abajo de las rectas que representan las ecuaciones, y la solución concreta es el corte con la Z
