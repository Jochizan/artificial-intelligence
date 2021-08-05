import numpy as np
import time
import sys

arr_one = np.array([1, 2, 3])
print('1D array:')
print(arr_one)
print()

arr_two = np.array([(1, 2, 3), (4, 5, 6)])
print('2D array:')
print(arr_two)
print()

# comparativa lista de "python" vs array de "numpy"

S = range(1000)
print('Resultado lista de Python:')
print(sys.getsizeof(100) * len(S))
print()

D = np.arange(1000)
print('Resultado NumPy array:')
print(D.size * D.itemsize)
print()

# comparativa en tiempo

SIZE = 1000000

L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()
result = [(x, y) for x, y in zip(L1, L2)]

print('Resultado lista de Python:')
print((time.time() - start) * 1000)
print()

start = time.time()
result = A1 + A2

print('Resultado NumPy array:')
print((time.time() - start) * 1000)
print()

print('Numpy sen and cos')
print(np.sin(np.pi / 180))
print(np.cos(np.pi / 180))
print(np.tan(np.pi / 180))
print(np.arcsin(0.8))
print(np.arccos(0.8))
print(np.arctan(0.8))
