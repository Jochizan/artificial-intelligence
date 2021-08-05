import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss

# Graficando la Distribución Normal

mu, sigma = 850, 45  # media y desviación estandar
X = ss.norm(mu, sigma)  # Objeto de la distribución normal de scipy.stats.norm

""" 
    ¿Cuál es la probabilidad que al seleccionar un componente 
        al azar tenga un duración mayor a los 855 días?
"""

# 1 - CDF ("sf" Es una abreviación para ""1 - función acumulada de la distribución normal de X"")
one_answer = X.sf(855)
other_answer = 1 - X.cdf(855)
print('La probabilidad de que la duración sea mayor a 855 es: ',
      str(one_answer), 'o', str(other_answer * 100), '%',
      (one_answer == other_answer), end='\n\n')

"""
    ¿Cuál es la probabilidad que al seleccionar un componente 
        al azar tenga un duración entre 760 a 860 días?
"""

two_answer = X.cdf(860) - X.cdf(760)  # Función de distribución acumulada
print('La probabilidad de que la duración este entre 760 a 860 es: ',
      str(two_answer), 'o', str(two_answer * 100), '%', end='\n\n')

# Función de punto porcentual (ppf = inversa de CDF --- percentiles)
# Generar un arreglo con valores aproximados con numpy
graph = np.arange(X.ppf(0.01), X.ppf(0.99))
print('Valores aproximados generados con numpy esta entre',
      graph[0], 'y', graph[graph.size - 1], end='\n')


"""
    ¿Cuál es el número de días de duración del 25% de los que más duran? 
"""

# Función inversa al CDF entregandole el porcentaje = 1 - 25% = 75% => 0.75
three_answer = X.ppf(.75)
print('La duración del 25% que más duran esta desde: ', str(three_answer), end='\n')

# Función de densidad de probabilidad (pdf) y representación gráfica
plt.plot(graph, X.pdf(graph), 'b')

# Titulo y nombres de los ejes
plt.title('Distribución Normal')
plt.ylabel('probabilidad')
plt.xlabel('duración')

# Mostrar el frame generado en el "plot"
plt.show()
