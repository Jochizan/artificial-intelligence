import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss

"""
    b.	Si el peso de las pantallas tiene una distribución normal 
    y x1, x2, ... es una muestra aleatoria simple de tamaño 9 que
    fue obtenida sin reemplazo de una población d 100 pantallas. 
    Calcule la probabilidad de que la media de la muestra sea a 
    lo más 5.5 kg.
"""

mu, sigma = 5, 0.2557
X = ss.norm(mu, sigma)

one_answer = X.cdf(5.5)

graph = np.arange(X.ppf(0.000001), X.ppf(0.999999))
print('Valores aproximados generados con numpy esta entre',
      graph[0], 'y', graph[graph.size - 1], end='\n')

print('La probabilidad de que la media se a lo más 5kg es:', one_answer)

plt.plot(graph, X.pdf(graph), 'b')

# Título y nombres de los ejes
plt.title('Gráfica de la b')
plt.ylabel('probabilidad')
plt.xlabel('pesos')
plt.show()

"""
    c. Si x1, x2, ... es una muestra aleatoria del peso de 45 
    pantallas con media poblacional igual a 5 kg. y varianza de 
    0.64 kg. Se desconoce el tamaño de la población. Calcule la 
    probabilidad que el peso promedio de las pantallas sea menor 
    a los 4.7 kg
"""

sig = 0.64 ** 0.5 / 45 ** 0.5
print(sig)
mu, sigma = 5, 0.119  # raiz de sigma de la muestra / raiz de la muestra
X = ss.norm(mu, sigma)

two_answer = X.cdf(4.7)

graph = np.arange(X.ppf(0.00000001), X.ppf(0.99999999))
print('Valores aproximados generados con numpy esta entre',
      graph[0], 'y', graph[graph.size - 1], end='\n')

print('La probabilidad que el peso promedio sea menor a 4.7kg es:', two_answer)

plt.plot(graph, X.pdf(graph), 'b')

# Título y nombres de los ejes
plt.title('Gráfica de la c')
plt.ylabel('probabilidad')
plt.xlabel('pesos')
plt.show()
