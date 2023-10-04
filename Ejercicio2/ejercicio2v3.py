#Aquí queremos estudiar todo lo posible, sin divertirnos.
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #x1 + x2 <= 10
f2 = "1+x" #x1 -x2 <= 1
f3 = "4" # x2 <= 4
x = symbols('x')
plot(f1, f2, f3, (x, -1, 15))
# Sol: múltiple, ya que las horas de estudio pueden ir de 1 a 10 (eje x), y las horas de diversión se mantienen en 0 