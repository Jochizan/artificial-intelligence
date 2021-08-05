import os
import numpy as np
import pylab as pl

from keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

"""
    Cargamos el modelo con la función load_model del modulo de "models" de keras
"""

# re_model = load_model('numbers_model_primary.h5')

"""
    Resumen de las características del modelo cargado
"""

# re_model.summary()

"""
    Cargamos los datos de testing
"""

test_data = np.loadtxt('./testing_data_primary.txt', delimiter=',')
print(test_data)

view_data = test_data.reshape((10, 7, 5))

pl.gray()

for array in list(view_data):
    pl.matshow(array)

pl.show()

# """
#     Predicción del modelo cargado
# """
# pred = re_model.predict(test_data)
# print("predicted softmax output => ", pred)
