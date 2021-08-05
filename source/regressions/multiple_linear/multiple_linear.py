# LIBRERIAS A UTILIZAR

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

# PREPARAR LA DATA PARA REGRESION LINEAL MULTIPLE

# Seleccionamos las columnas 5, 6 y 7 del dataset
X_multiple = boston.data[:, 5:8]
print(X_multiple)

# Defino los datos correspondientes a las etiquetas
Y_multiple = boston.target

# IMPLEMENTACION DE REGRESION LINEAL MULTIPLE

from sklearn.model_selection import train_test_split

# Separo los datos de "train" en entrenamiento y prueba para probar algoritmos
X_train, X_test, Y_train, Y_test = train_test_split(X_multiple, Y_multiple, test_size=0.2)

# Definimos el algoritmo a utilizar
lr_multiple = linear_model.LinearRegression()

# Entreno el modelo
lr_multiple.fit(X_train, Y_train)

# Realizo la prediccion
Y_pred_multiple = lr_multiple.predict(X_test)

print('DATOS DEL MODELO DE REGRESION LINEAL MULTIPLE')
print()

print('Valor de las pendientes o coeficientes "a": ')
print(lr_multiple.coef_)

print('Valor de la interseccion o coeficientes "b": ')
print(lr_multiple.intercept_)

print('Precision del modelo: ')
print(lr_multiple.score(X_train, Y_train))
