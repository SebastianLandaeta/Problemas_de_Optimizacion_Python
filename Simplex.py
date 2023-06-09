import numpy as np
from scipy.optimize import linprog

# Definir la función objetivo y las restricciones en forma matricial
c = np.array([110, 150])
A = np.array([[4, 6], [20, 10]])
b = np.array([480, 1500])

# Resolver el problema utilizando el método Simplex a través de la función linprog
resultado = linprog(-c, A_ub = A, b_ub = b, method = 'simplex')

# Imprimir el resultado
print("Status:", resultado.message)
print("Solución óptima: ")
print("X =", round(resultado.x[0], 2))
print("Y =", round(resultado.x[1], 2))
print("Valor óptimo de la función objetivo: Z =", round(-resultado.fun, 2))