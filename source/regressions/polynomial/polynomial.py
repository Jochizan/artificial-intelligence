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

# PREPARAR LA DATA REGRESIÓN POLINOMIAL

# Seleccionamos solamente la columna 6 del dataset
X_p = boston.data[:, np.newaxis, 5]
print(X_p)

# Defino los datos correpondientes a las etiquetas
Y_p = boston.target

# Graficamos los datos correspodientes
plt.scatter(X_p, Y_p)
plt.show()

# IMPLEMENTACIÓN DE REGRESIÓN POLINOMIAL

from sklearn.model_selection import train_test_split

# Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train_p, X_test_p, Y_train_p, Y_test_p = train_test_split(X_p, Y_p, test_size=0.2)

from sklearn.preprocessing import PolynomialFeatures

# Se define el grado del polinomio
poli_reg = PolynomialFeatures(degree=2)

# Se transforma las características existentes en características de mayor grado
X_train_poli = poli_reg.fit_transform(X_train_p)
X_test_poli = poli_reg.fit_transform(X_test_p)

# Defino el algoritmo a utilizar
pr = linear_model.LinearRegression()

# Entreno el modelo
pr.fit(X_train_poli, Y_train_p)

# Realizo una predicción
Y_pred_pr = pr.predict(X_test_poli)

# Graficamos los datos juntos con el modelo
print(X_test_p, Y_test_p)
plt.scatter(X_test_p, Y_test_p)
plt.plot(X_test_p, Y_pred_pr, color='red', linewidth=3)
plt.show()

print()
print('DATOS DEL MODELO REGRESIÓN POLINOMIAL')
print()

print('Valor de la pendiente o coeficiente "a": ')
print(pr.coef_)

print('Valor de la intersección o coeficiente "b": ')
print(pr.intercept_)

print('Precisión del modelo: ')
print(pr.score(X_train_poli, Y_train_p))
