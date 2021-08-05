# LIBRERIAS A UTILIZAR
import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets

# PREPARAR LA DATA

# Importamos los datos de la misma libreria de scikit-learn
boston = datasets.load_boston()
print(boston)
print()

# ENTENDENDIMIENTO DE LA DATA

# Verifico la informacion contenida en el dataset
print('Informacion en el dataset: ')
print(boston.keys())
print()

# Verifico las caracteristicas del dataset
print('Caracteristicas del dataset: ')
print(boston.DESCR)

# Verifico la cantidad de datos que hay en los dataset
print('Cantidad de datos: ')
print(boston.data.shape)
print()

# Verifico la informacion de las columnas
print('Nombre de las columnas: ')
print(boston.feature_names)

# PREPARAR LA DATA BOSQUES ALEATORIOS REGRESIÓN

# Seleccionamos solamente la columna 6 del dataset
X_bar = boston.data[:, np.newaxis, 5]

# Defino los datos correspondientes a las etiquetas
Y_bar = boston.target

# Graficamos los datos correspondientes
plt.scatter(X_bar, Y_bar)
plt.show()

# IMPLEMENTACIÓN DE BOSQUES ALEATORIOS REGRESIÓN

from sklearn.model_selection import train_test_split

# Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, Y_train, Y_test = train_test_split(X_bar, Y_bar, test_size=0.2)

from sklearn.ensemble import RandomForestRegressor

# Defino el algoritmo a utilizar
bar = RandomForestRegressor(n_estimators=300, max_depth=8)

# Entreno el modelo
bar.fit(X_train, Y_train)

# Realizo una predicción
Y_pred = bar.predict(X_test)

# Graficamos los datos de prueba junto con la predicción
X_grid = np.arange(min(X_test), max(X_test), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))

plt.scatter(X_test, Y_test)
plt.plot(X_grid, bar.predict(X_grid), color='r', linewidth=3)
plt.show()

print('DATOS DEL MODELO BOSQUES ALEATORIOS REGRESIÓN')
print()

print('Precisión del modelo: ')
print(bar.score(X_train, Y_train))
