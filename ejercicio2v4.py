#Aquí queremos divertirnos lo máximo posible, sin excluir estudiar
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #x1 + x2 <= 10
f2 = "1+x" #x1 -x2 <= 1
f3 = "4" # x2 <= 4
x = symbols('x')
plot(f1, f2, f3, (x, -1, 15))
#La solución es la recta acotada desde x1 = 3 a x1 = 6 y x2 = 4, ya que 4 son las horas máximas de diversión y el resto de horas para estudiar.