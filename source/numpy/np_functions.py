# Crear una matriz de unos - 3 filas 5 columnas
import numpy as np
from numpy import newaxis

ones = np.ones((3, 5))
print(ones)
print()

# Crear una matriz con valores aleatorios
random = np.random.random((9, 2))
print(random)
print()

# Crear una matriz con un solo valor
full = np.full((3, 3), 100)
print(full)
print()

# Crear matrices con valores espaciados
space_one = np.arange(0, 100, 5)
print(space_one)
print()

# Crear matrices con valores espaciados con decimales
space_two = np.linspace(0, 2, 5)
print(space_two)
print()

# Crear una matriz identidad
identity_one = np.eye(4, 4)
print(identity_one)
print()

# Crear con identity
identity_two = np.identity(4)
print(identity_two)
print()

arr = np.array([(1, 2, 3), (4, 5, 6)])
# Conocer las dimensiones de una matriz
print(arr.ndim)
# Conocer el tipo de dato de una matriz
print(arr.dtype)
# Conocer el tamaño y forma de una matriz
print(arr.size)
print(arr.shape)
print()

# Cambiar la forma de una matriz

arr = np.array([(8, 9, 10), (11, 12, 13)])
print(arr)
print()

arr = arr.reshape(3, 2)
print(arr)
print()

arr = np.array([(1, 2, 3, 4), (3, 4, 5, 6)])
print(arr[1, 2])
print()

# Extraer los valores de todas las filas en la columna 3
arr = np.array([(1, 2, 3, 4), (3, 4, 5, 6)])
print(arr[0:, 2])
print()

# Encontrar el mínimo, máximo y la suma
arr = np.array([2, 4, 9])
print(arr.min())
print(arr.max())
print(arr.sum())
print()

# Calcular la raíz cuadrada y la desviación estándar
arr = np.array([(1, 2, 3), (3, 4, 5,)])
print(np.sqrt(arr))
print(np.std(arr))
print()

# Calcular la suma, resta, multiplicación y división de 2 matrices
x = np.array([(1, 2, 3), (3, 4, 5)])
y = np.array([(1, 2, 3), (3, 4, 5)])

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print()

# Redimensionar arrays por la cantidad de arreglos 1D que tengamos
a = np.array([4., 2., 1.])
b = np.array([3., 8., 7.])
c = np.array([2., 5., 6.])
D3 = np.column_stack((a, b, c))
print(np.column_stack((a, b, c)))
print()

# Importante ver como obtener los calores dependiendo del axis
print(D3[0:3:2, newaxis, 2])
# Newaxis genera una matriz 2D para no solo quedarnos con los valores en un arreglo 1D
