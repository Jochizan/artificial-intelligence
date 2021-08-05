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

# Seleccionamos solamente al columna 6 del dataset
X_adr = boston.data[:, np.newaxis, 5]

# Defino los datos correspondientes a las etiquetas
Y_adr = boston.target

# Graficamos los datos correspondientes
plt.scatter(X_adr, Y_adr)
plt.show()

# IMPLEMENTACIÓN DE ARBOLES DE DECESIÓN REGRESIÓN

from sklearn.model_selection import train_test_split

# Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, Y_train, Y_test = train_test_split(X_adr, Y_adr, test_size=0.2)

from sklearn.tree import DecisionTreeRegressor

# Defino el algoritmo a utilizar
adr = DecisionTreeRegressor(max_depth=5)

# Entreno el modelo
adr.fit(X_train, Y_train)

# Realizo una predicción
Y_pred = adr.predict(X_test)

# Graficamos los datos de prueba junto con la predicción
X_grid = np.arange(min(X_test), max(X_test), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X_test, Y_test)
plt.plot(X_grid, adr.predict(X_grid), color='red', linewidth=3)
plt.show()

print('DATOS DEL MODELO ARBOLES DE DECISIÓN REGRESIÓN')
print()

print('Precisión del modelo: ')
print(adr.score(X_train, Y_train))
