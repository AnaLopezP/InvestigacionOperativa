import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #x1 + x2 <= 10
f2 = "1+x" #x1 -x2 <= 1
f3 = "4" # x2 <= 4
x = symbols('x')
plot(f1, f2, f3, (x, -1, 15))
# Sol: múltiple