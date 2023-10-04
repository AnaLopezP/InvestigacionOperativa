import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "1+x" #<=
#y=4
f2 = "4" #<=
Z1 = "(16-x)/2"
Z2 = "(14-x)/2"
Z3 = "(13-x)/2"
x = symbols('x')
plot(f1, f2, Z1, Z2, Z3, (x, -1, 15))
# Sol: No acotada