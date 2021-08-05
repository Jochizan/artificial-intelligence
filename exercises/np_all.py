import numpy as np
     
     
A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])
 
B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])
 
C = np.array([[True, False, False],
              [True, True, True]])
 
D = np.array([0.1, 0.3])

# Solution 1:

# Iteraciones a través de dos listas con zip
for name, array in zip(list('ABCD'), [A, B, C, D]):
    # Impresión con formato del paramtro f'{name}: {np.all(array)}'
    # {name} => nombre del array
    # {np.all(array)} evalue si el arreglo tiene valores que se evalúan como verdaderos
    print(f'{name}: {np.all(array)}')

# Solution 2:

for name, array in zip(list('ABC'), [A, B, C]):
    print(f'{name}: {np.all(array, axis=1)}')

# Solution 3:

for name, array in zip(list('ABCD'), [A, B, C, D]):
    print(f'{name}: {np.any(array)}')

# Solution 4:

for name, array in zip(list('ABC'), [A, B, C]):
    print(f'{name}: {np.any(array, axis=1)}')
