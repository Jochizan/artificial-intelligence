# LIBRERIAS QUE UTILIZAREMOS

from sklearn import datasets, linear_model

import numpy as np
import matplotlib.pyplot as plt

# Importamos los datos de la misma librería scikit-learn

boston = datasets.load_boston()

# Verificar la información contenida en el dataset
print('Información en el dataset: ')
# print(boston)
print(boston.keys())
print()

# Verifico las caracteristicas del dataset
print('Caracteristicas del dataset: ')
print(boston.DESCR)

# Verifico la cantidad de datos que hay en los dataset
print(boston.data.shape)
print()

# Verifico la información de las columnas
print('Nombres de las columnas: ')
print(boston.feature_names)

# PREPARAR LA DATA REGRESIÓN LINEAL SIMPLE

# Seleccionamos solamente la columna 5 del dataset
X = boston.data[:, np.newaxis, 5]
# print(X)

# Defino los datos correspondientes a las etiquetas
Y = boston.target

# Graficamos los datos correspondientes
plt.scatter(X, Y)
plt.xlabel('Número de habitaciones')
plt.ylabel('Valor medio')
plt.show()

# IMPLEMENTAR LA REGRESIÓN LINEAL SIMPLE

from sklearn.model_selection import train_test_split

# Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Definimos el algoritmo a utilizar
lr = linear_model.LinearRegression()

# Entrenamos el modelo
lr.fit(X_train, Y_train)

# Realizo una predicción
Y_pred = lr.predict(X_test)

# Graficamos los datos junto con el modelo
plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=3)
plt.title('Regresión Lineal Simple')
plt.xlabel('Número de habitaciones')
plt.ylabel('Valor medio')
plt.show()

print()
print('DATOS DEL MODELO DE REGRESIÓN LINEAL SIMPLE')
print()
print('Valor de la pendiente o coeficiente "a": ', end='')
print(lr.coef_)
print('Valor de la intersección o coeficiente "b": ', end='')
print(lr.intercept_)
print()
print('La ecuación del modelo es igual a: ')
print('y =', lr.coef_, 'x =', lr.intercept_)

print()
print('La precisión del modelo: ', end='')
print(lr.score(X_train, Y_train))
