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

# IMPLEMENTACIÓN DE LA REGRESIÓN LOGISTICA

from sklearn.model_selection import train_test_split

# Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# Se escalan todos los datos
from sklearn.preprocessing import StandardScaler

escalar = StandardScaler()
X_train = escalar.fit_transform(X_train)
X_test = escalar.transform(X_test)

# Defino el algoritmo a utilizar
from sklearn.linear_model import LogisticRegression

algorithm = LogisticRegression()

# Entreno el modelo
algorithm.fit(X_train, Y_train)

# Realizo una predicción
Y_pred = algorithm.predict(X_test)

# Verifico la matriz de confusión
from sklearn.metrics import confusion_matrix

matriz = confusion_matrix(Y_test, Y_pred)
print('Matriz de confusión:')
print(matriz)

# Calculo de la precisión del modelo
from sklearn.metrics import precision_score

precision = precision_score(Y_test, Y_pred)
print('Precisión del modelo:')
print(precision)

# Calculo de la exactitud del modelo
from sklearn.metrics import accuracy_score

exactitud = accuracy_score(Y_test, Y_pred)
print('Exactitud del modelo:')
print(exactitud)

# Calculo de la sensibilidad del modelo
from sklearn.metrics import recall_score

sensibilidad = recall_score(Y_test, Y_pred)
print('Sensibilidad del modelo:')
print(sensibilidad)

# Calculo el Puntaje F1 del modelo
from sklearn.metrics import f1_score

puntajef1 = f1_score(Y_test, Y_pred)
print('Puntaje F1 del modelo:')
print(puntajef1)

# Caculo de la curva ROC - AUC del modelo
from sklearn.metrics import roc_auc_score

roc_auc = roc_auc_score(Y_test, Y_pred)
print('Curva ROC - AUC del modelo:')
print(roc_auc)

print('Precisión del modelo:', precision)
print('Exactitud del modelo:', exactitud)
print('Sensibilidad del modelo:', sensibilidad)
print('Puntaje F1 del modelo', puntajef1)
print('Curva ROC - AUC del modelo:', roc_auc)
