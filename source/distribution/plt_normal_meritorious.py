import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss

"""
    @sigma -> desviación estándar
    @mu -> media
"""

# Declaramos nuestras variable
mu, sigma = 650, 100

X = ss.norm(mu, sigma)

"""
    a). ¿Qué probabilidad hay de que la demanda no supere los 500kg?
"""

answer = X.cdf(500)

print('La probabilidad de que la demanda no supere los 500kg es: ', answer)

"""
    b). ¿Qué cantidad del bien debe haber mensualmente a fin de satisfacer la demanda de un 89.8% ?
"""

answer = X.ppf(.898)

print('La cantidad del bien mensual para una demanda del 89.8% es: ', answer)
print()

graph = np.arange(X.ppf(0.001), X.ppf(0.999))
plt.plot(graph, X.pdf(graph), 'b')

plt.title('Gráfica de la pregunta')
plt.ylabel('y')
plt.xlabel('peso')
plt.show()

"""
    2.	De una variable normal N(µ; σ) se sabe que P (X ≤ 7 ) = 0.9772  y P (X ≤ 6.5) =  0.8413.
"""

"""
    a). µ  y σ.
"""

"""

    P(X <= 7) = 0.9772
    Z = 2
    Z = (X - µ) / σ
    2 = (7 - µ) / σ
    2σ + µ = 7 (1)
    
    P(x <= 6.5) = 0.8413
    Z = 1
    Z = (X - µ) / σ
    1 = (6.5 - µ) / σ
    σ + µ = 6.5 (2)
    
    -σ = -0.5
    σ = 0.5
    µ = 6.0
"""

mu, sigma = 6.0, 0.5

X = ss.norm(mu, sigma)

"""
    b). P (5.65 ≤ X ≤ 6.25)
"""

b_answer = X.cdf(6.25) - X.cdf(5.65)

"""
    c). El numero k tal que P(X > k) = 0.3
"""

c_answer = X.ppf(0.3)

print('El P(5.65 <= X <= 6.25) es: ', b_answer)
print('El número K en P(X > k) = 0.3 es: ', c_answer)
print()

graph = np.arange(X.ppf(0.00001), X.ppf(0.99999))
plt.plot(graph, X.pdf(graph), 'b')

plt.title('Gráfica de la pregunta')
plt.ylabel('y')
plt.xlabel('x')
plt.show()

"""
    3.	Se quiere realizar un estudio sobre los salarios en una fábrica de computadoras en EUA, en dónde trabajan
     miles de personas. Se sabe que la media poblacional del salario es de $8.00 dólares por hora y con un error 
     estándar de $1.75. Seleccionamos al azar 130 expedientes del personal y registramos los salarios por hora. 
     Calcule la probabilidad que el salario promedio de las pantallas sea por los menos $7.00 por hora.
"""

mu = 8.00
sigma = (1.75 * (130 ** 0.5))
z = (7.00 - 8.00) / sigma

X = ss.norm(mu, sigma)

answer = X.sf(7.00)
print('La probabilidad que el salario por lo menos se $7.00 por hora es: ', answer)
print()

graph = np.arange(X.ppf(0.1), X.ppf(0.9))
plt.plot(graph, X.pdf(graph), 'b')

plt.title('Gráfica de la pregunta')
plt.ylabel('y')
plt.xlabel('pesos')
plt.show()

"""
    4. Una compañía de televisión por cable quisiera estimar la proporción de sus clientes que comprarían 
    una revista con los programa de televisión por cable. La compañía quisiera tener una confianza del 95% 
    de que su estimación sea correcta es una escala de ±0.05 de la proporción real. La experiencia anterior 
    en otras áreas señala que el 30% de los clientes comprarán la revista de programas. ¿Qué tamaño de muestra 
    se necesita?
"""


def desconocida_cualitativa(p, q, z, e):
    return (z ** 2 * p * q) / (e ** 2)


p = 0.3
q = 0.7
z = 1.96
e = 0.05

answer = desconocida_cualitativa(p, q, z, e)
print('El tamaño de muestra que se requerira', answer, 'aprox.', round(answer, 0))
