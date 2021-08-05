# LIBRERIAS A UTILIZAR
import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, linear_model

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

# PREPARAR LA DATA DE VECTORES DE SOPORTE REGRESIÓN

# Seleccionamos solamente la columna 6 del dataset

X_svr = boston.data[:, np.newaxis, 5]

# Defino los datos correspondientes a las etiquetas

Y_svr = boston.target

# Graficamos los datos correspondientes
plt.scatter(X_svr, Y_svr)
plt.show()

# IMPLEMENTACIÓN DE VECTORES DE SOPORTE REGRESIÓN

from sklearn.model_selection import train_test_split

# Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, Y_train, Y_test = train_test_split(X_svr, Y_svr, test_size=0.2)

from sklearn.svm import SVR

# Defino el algoritmo a utilizar
svr = SVR(kernel='linear', C=1.0, epsilon=0.2)
# IMPORTANTE
# Si dejamos los valores por defecto de SVR kernel='rbf', C=1.0 y epsilon=0.1
# Tendriamos mejores resultados

# Entrenar el modelo
svr.fit(X_train, Y_train)


# Realizar la predicción

Y_pred = svr.predict(X_test)

# Graficamos los datos junto con el modelo

plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_pred, color='red', linewidth=3)
plt.show()

print()
print('DATOS DEL MODELO VECTORES DE SOPORTE DE REGRESIÓN')
print()

print('Precisión del modelo: ')
print(svr.score(X_train, Y_train))
