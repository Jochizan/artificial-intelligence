"""
    Script de python para crear una red neuronal con keras para el reconocimiento
    de números con este y su posterior implementación en nuestra pequeña
    aplicación web con Flask
"""

"""
    Importamos las librerías necesarias para poder crear nuestras redes neuronales
"""
import os
import time
import unittest
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

"""
    Esta clase con unittest nos ayudara a ver que tan buena es
    la red neuronal que creamos con tensorflow los datos de
    prediction son una lista de 10 posiciones así que debe 
    predecir bien en los 10 arreglos que da como respuesta 
    la red neuronal de la siguiente forma:

    prediction = prediction[0]
    prediction[0] => aprox. 1
    prediction[1] => aprox. 1
    prediction[2] => aprox. 1
    ...
    prediction[9] => aprox. 1
"""


class TestCasePrediction(unittest.TestCase):
    def test_prediction(self):
        count, i = 0, 0

        for array in list(prediction):
            approx = array[i]

            print(array)
            print()

            print(
                approx,
                'round fixed =>', round(approx, 2),
                'porcentual =>', str(round(approx * 100, 2)) + '%'
            )
            print()

            if round(approx) == 1:
                count += 1

            i += 1

        print()
        print(
            'test accuracy =>', str(round(count / 10 * 100, 2)) + '%'
        )

        self.assertEqual(10, count)


"""
    Primero compilamos la red definiendo una función de pérdida y un optimizador: en nuestro caso seleccionamos 
    categorical_crossentropy, porque tenemos múltiples categorías (como en los números 0-9). La función 
    number_recognition_model nos crea un modelo de Sequential para la predicción de números expresados en patrones de 35 
    números entre 0 y 1 esta función genera tre capas la primera con 32 neuronas con función de activación "relu" otra 
    con el doble de la anterior con 64 y también función de activación "relu" y la capa de salida con 10 neuronas con 
    función de activación "softmax". 
"""


def number_recognition_model():
    dropout = Dropout(0.20)
    layer_one = Dense(8, activation='sigmoid', input_shape=(35,))
    layer_two = Dense(16, activation='sigmoid')
    layer_three = Dense(10, activation='softmax')

    number_model = Sequential()
    number_model.add(dropout)
    number_model.add(layer_one)
    number_model.add(layer_two)
    number_model.add(layer_three)
    number_model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

    return number_model


"""
    Cargamos los datos de entrenamiento para la primera versión de los datos de entrada
"""

train_data = np.loadtxt('./number_patterns_primary.txt', delimiter=',')
batch = train_data

"""
    Mostramos los datos de entrada 
"""

print("data = ", train_data)
print()

"""
    Graficamos los datos de entrada del modelo
"""

# view_data = train_data.reshape((20, 7, 5))
#
# pl.gray()
#
# for array in list(view_data):
#     pl.matshow(array)
#
# pl.show()

"""
    Cargamos los datos de salida de la primera versión de los datos de salida
"""

target_data = np.loadtxt('./number_target_primary.txt', delimiter=',')

"""
    Mostramos los datos de salida
"""

print("target = ", target_data)
print()

"""
    Llamar la función para tener el modelo creado con anterioridad
"""

model = number_recognition_model()

"""
    Tomar muestra del tiempo para ver cuanto demora la ejecución en milisegundos
"""
start = time.time()

"""
    Entrenamiento del modelo con variaciones en epochs y batch_size
"""
model.fit(train_data, target_data, epochs=6000)

"""
    Muestra del tiempo en el que comenzó y finalizo
"""
finish = time.time()

print()
print((finish - start) * 1000, 'ms o', (finish - start), 's')
print()

print('Tiempo de inicio: ', time.asctime(time.localtime(start)))
print('Tiempo de finalización: ', time.asctime(time.localtime(finish)))
print()

"""
    Evaluamos el modelo con sus datos de entrenamiento y verificamos la precisión de este
"""
scores = model.evaluate(train_data, target_data)
print('\n%s: %.2f%%' % (model.metrics_names[1], scores[1] * 100))
print()

"""
    Hacemos una predicción con los datos generales de entrada
"""
predict_data = model.predict(train_data)
print(predict_data)
print()

"""
    Ingresamos datos de test para el número 6 para luego verificar el resultado
"""

test_data = np.loadtxt('./testing_data_primary.txt', delimiter=',')
print(test_data)

"""
    Hacemos una predicción con los datos de test
"""
prediction = model.predict(test_data)
print("predicted softmax output => ", prediction)

"""
    Salvamos el modelo para poder volver a utilizar nuestra red neuronal
"""
model.save('numbers_model_primary.h5')

if __name__ == '__main__':
    unittest.main()
