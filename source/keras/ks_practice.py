import os
import time
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}

from keras.layers import Dense
from keras.models import Sequential

training_data = np.array([[1, 1],
                          [1, 0],
                          [0, 1],
                          [0, 0]], 'float32')

# Y estos son los resultados que se obtienen, en el mismo orden
target_data = np.array([[1],
                        [0],
                        [0],
                        [0]], 'float32')

model = Sequential()
model.add(Dense(24, input_dim=2, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])

start = time.time()
model.fit(training_data, target_data, epochs=5000)
print('Tiempo de inicio: ', time.asctime(time.localtime(start)))
print('Tiempo de ejecución: ', time.asctime(time.localtime(time.time())))

scores = model.evaluate(training_data, target_data)
print('\n%s: %.2f%%' % (model.metrics_names[1], scores[1] * 100))
print()

print(training_data)
print()

print(model.predict(training_data))
print()
