# IMPORTAR LAS LIBRERIAS

# Se importan las libreria a utilizar
from sklearn import datasets

# PREPARAR LA DATA

# Importamos los datos de la misma libreria de scikit-learn
dataset = datasets.load_breast_cancer()
print(dataset)

# ENTENDIMIENTO DE LA DATA

# Verifico la información contenida en el dataset
print('Información en el dataset:')
print(dataset.keys())
print()

# Verifico las características del dataset
print('Características del dataset:')
print(dataset.DESCR)

# Seleccionamos todas las columnas
X = dataset.data

# Defino los datos correspondientes a las etiquetas
Y = dataset.target

# IMPLEMENTACIÓN DE ÁRBOLES DE DECISIÓN CLASIFICACIÓN

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Defino el algoritmo a utilizar
# Arboles de decision
from sklearn.tree import DecisionTreeClassifier

algorithm = DecisionTreeClassifier(criterion='entropy')

# Entrenar el modelo
algorithm.fit(X_train, Y_train)

# Realizo una predicción
Y_pred = algorithm.predict(X_test)

# Verifico la matriz de confusión
from sklearn.metrics import confusion_matrix
matriz = confusion_matrix(Y_test, Y_pred)
print('Matriz de confusión:')
print(matriz)

# Calculo la precisión del modelo
from sklearn.metrics import precision_score
precision = precision_score(Y_test, Y_pred)
print('Precisión del modelo:')
print(precision)
