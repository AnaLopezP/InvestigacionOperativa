#Recursos: plástico 1200kg, horas 40h
#Requerimientos: producción total <= 800, x1 - x2 <= 450
#x1 --> space rays: 2kg, 3min
#x2 --> Zappers: 1kg, 4min


#max Z = 8x1 + 5x2 (sol. 4900€)
#Plástico: 2x1 + x2 <= 1200
#Horas: 3x1 + 4x2 <= 2400
#x1 + x2 <= 800
#x1 - x2 <= 450
#sol. x1 = 550, x2 = 100

import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "(1200-2*x)" # 2x1 + x2 <= 1200 (azul abajo)
f2 = "(2400-3*x)/4" # 3x1 + 4x2 <= 2400 (naranja abajo)
f3 = "800-x" # x1 + x2 <= 800 (verde abajo)
f4 = "x-450" # x1 - x2 <= 450 (rojo arriba)
Z1 = "(4900-8*x)/5"
Z2 = "(3000-8*x)/5"
Z3 = "(1000-8*x)/5"
x = symbols('x')
plot(f1, f2, f3, f4, Z1, (x, 0, 800))

#b) ¿se puede hacer mejor?
'''Si, ya que hay otros puntos que equilibran más la producción de los juguetes. En la gráfica se ve que la función Z (morado) corta con el área óptima en el punto (450, 260). Z sigue valiendo 4900, pero la producción de juguetes está más equilibrada.'''

#c)Calcular Z, x1 y x2 para el mejor plan de producción sin Zapper
'''En el caso que no se produzcan Zapper, es decir que x2 = 0, el valor máximo de x1 = 450 y Z = 3600'''

#d)Calcular Z, x1 y x2 para el mejor plan de producción sin Space Ray 
'''Si no se producen Space Ray, es decir que x1 = 0, el valor máximo de x2 = 600 y Z = 3000'''

#e) ¿x1 = 100; x2 = 150 es una solución factible? ¿Por qué?
'''Es una solución factible, ya que está dentro de del área óptima.'''

#f) ¿x1 = 500; x2 = 150 es una solución factible? ¿Por qué? 
'''Es una solución factible, ya que está dentro de del área óptima.'''
