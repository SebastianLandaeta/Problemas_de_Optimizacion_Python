# Importar librerías
import numpy as np
import pulp

from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

# Creamos el objeto Lp, para un problema de maximización
problema = pulp.LpProblem("Ejercicio", pulp.LpMaximize)

# Creamos las variables de decisión
x = pulp.LpVariable('x', lowBound=0, cat='Integer')
y = pulp.LpVariable('y', lowBound=0, cat='Integer')

# Función Objetivo
problema += 9000*x + 1200*y

# Restricciones
problema += (x <= 20)
problema += (y <= 10)
problema += ((3*x + 4*y) >= 12)

# Resolver el problema
resultado = problema.solve()

# Buscamos la solución óptima
assert resultado == pulp.LpStatusOptimal

# Visualizar resultados
for var in (x, y):
    print('{}: {:1.0f}'.format(var.name, var.value()))

# Creamos nuestro gráfico
fig, ax = plt.subplots(figsize=(8, 8))
s = np.linspace(0, 50)

# Restricción 1
plt.plot(20 * np.ones_like(s), s, lw=3, label='R1')

# Restricción 2
plt.plot(s, 10*np.ones_like(s), lw=3, label='R2')

# Restricción 3
plt.plot(np.linspace(4, 0), np.linspace(0, 3), lw=3, label='R3')

# Restricción de no negatividad
plt.plot(np.zeros_like(s), s, lw=3, label ='y non-negative')
plt.plot(s, np.zeros_like(s), lw=3, label='x non-negative')

# Región factible
path = Path([
    (0., 3.),
    (0., 10.),
    (20., 10.),
    (20., 0.),
    (4., 0),
])

patch = PathPatch(path, label='Región Factible', alpha=0.5)
ax.add_patch(patch)

# Etiquetas y relleno
plt.xlabel('X', fontsize=16)
plt.ylabel('Y', fontsize=16)
plt.xlim(-0.5, 35)
plt.ylim(-0.5, 35)
plt.legend(fontsize=14)

# Mostrar
plt.show()