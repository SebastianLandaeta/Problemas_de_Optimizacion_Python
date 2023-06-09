from scipy.optimize import linprog

# Coeficientes de la función objetivo
c = [6, 2]

# Coeficientes de las restricciones
A = [[-1, -2], [-3, -2]]
b = [-4, -8]

# Coeficientes de las variables de holgura
A_eq = [[1, 0], [0, 1]]
b_eq = [0, 0]

# Resolver el problema utilizando el método de dos fases
result = linprog(c, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, method='simplex')

# Imprimir el resultado
if result.success:
    print("Estado: El problema se resolvió correctamente.")
    print("Valor óptimo de la función objetivo:", result.fun)
    print("Valores óptimos de las variables:")
    for i, variable in enumerate(result.x):
        print(f"x{i+1} =", variable)
else:
    print("Estado: El problema no pudo ser resuelto.")