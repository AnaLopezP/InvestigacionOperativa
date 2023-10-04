import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #x2 + x1 <= 10
f2 = "1+x" #x1 - x2 <= 1
f3 = "4" #x2 <= 4
Z1 = "16-x"
Z2 = "14-x"
Z3 = "13-x"
x = symbols('x')
plot(f1, f2, f3, Z1, Z2, Z3, (x, -1, 15))
# Sol: Z= x1=5 x2=4 Solución única
#La suma tiene que ser máximo 10, pero si ponemos x1 = 6, la resta de x1 y x2 es mayor de 1
