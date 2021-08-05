import os
import time
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}

from keras.layers import Dense
from keras.models import Sequential

data = np.loadtxt('./data.txt', delimiter=',', skiprows=1, usecols=[0, 1, 2, 3, 4, 5])

train_data = np.array(data)

target = np.loadtxt('./data.txt', delimiter=',', max_rows=1)
target_data = np.array(str(target))

print(data, target)

# model = Sequential()
# model.add(Dense(12, input_dim=6, activation='tanh'))
# model.add(Dense(1, activation='tanh'))
#
# model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])
#
# start = time.time()
#
# model.fit(train_data, target_data, epochs=500)
# print('Tiempo de inicio: ', time.asctime(time.localtime(start)))
# print('Tiempo de final: ', time.asctime(time.localtime(time.time())))
#
# scores = model.evaluate(train_data, target_data)
# print('\n%s: %.2f%%' % (model.metrics_names[1], scores[1] * 100))
#
# print(train_data)
# print()
#
# print(model.predict(train_data))
# print()
