from pulp import LpMinimize, LpProblem, LpStatus, lpSum, LpVariable

# Crear el problema de minimización
problem = LpProblem("Problema de Programación Lineal", LpMinimize)

# Definir las variables de decisión
x = LpVariable('x', lowBound=0)
y = LpVariable('y', lowBound=0)

# Definir la función objetivo
problem += 6*x + 2*y

# Definir las restricciones
problem += 0.5*x + 0.2*y <= 4
problem += 2*x + 3*y >= 20
problem += x + y == 10

# Resolver el problema
problem.solve()

# Imprimir el estado de la solución
print("Estado:", LpStatus[problem.status])

# Imprimir los valores óptimos de las variables de decisión
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)

# Imprimir el valor óptimo de la función objetivo
print("Valor óptimo de la función objetivo:", problem.objective.value())