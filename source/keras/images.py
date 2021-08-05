import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

digits = load_digits()

images_and_labels = list(zip(digits.images, digits.target))

plt.figure(figsize=(5, 5))

for index, (image, label) in enumerate(images_and_labels[:15]):
    plt.subplot(3, 5, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('%i' % label)

n_samples = len(digits.images)
print('Number of samples in the data set is:' + str(n_samples))

x_data = digits.images.reshape((n_samples, - 1))
y_data = digits.target

X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

X_train = X_train.T
X_test = X_test.T

y_train = y_train.reshape(y_train.shape[0], 1)
y_test = y_test.reshape(y_test.shape[0], 1)

y_train = y_train.T
y_test = y_test.T

Y_train_ = np.zeros((10, y_train.shape[1]))

for i in range(y_train.shape[1]):
    Y_train_[y_train[0, i], i] = 1

Y_test_ = np.zeros((10, y_test.shape[1]))

for i in range(y_test.shape[1]):
    Y_test_[y_test[0, i], i] = 1
