import numpy as np
import pandas as pd

data = np.array([['', 'c-1', 'c-2'], ['f-1', 11, 22], ['f-2', 33, 44]])
print(pd.DataFrame(data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:]))
print()

# más abreviado

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), dtype='int64')
print('DataFrame:')
print(df)
print()

# series
series = pd.Series(
    {
        'Argentina': 'Buenos Aires',
        'Colombia': 'Bogotá',
        'Chile': 'Santiago de Chile',
        'Perú': 'Lima'
    }
)

print('Series:')
print(series)
print()

# Forma del DataFrame
print('Forma del DataFrame:')
print(df.shape)
print()

# Altura del DataFrame
print('Altura del DataFrame:')
print(len(df.index))
print()

# Estadística del DataFrame
print('Estadística del DataFrame:')
print(df.describe())
print()

# Media de las columnas DataFrame
print('Media de las columnas DataFrame:')
print(df.mean())
print()

# Correlación del DataFrame
print('Correlación del DataFrame:')
print(df.corr())
print()

# Cuenta los datos del DataFrame
print('Conteo de datos del DataFrame:')
print(df.count())
print()

# Valor más alto de cada columna del DataFrame
print('Valor más alto de la columna del DataFrame:')
print(df.max())
print()

# Valor mínimo de cada columna del DataFrame
print('Valor mínimo de la columna del DataFrame')
print(df.min())
print()

# Mediana de cada columna del DataFrame
print('Mediana de la columna del DataFrame')
print(df.median())
print()

# Desviación estándar de cada columna del DataFrame
print('Desviación estándar de la columna del DataFrame:')
print(df.std())
print()

# Seleccionar la primera columna del DataFrame
print('Primera columna del DataFrame:')
print(df[0])
print()

# Seleccionar más columnas del DataFrame
print('Dos columnas del DataFrame:')
print(df[[0, 1]])
print()

# Seleccionar el valor de la primera fila y última columna del DataFrame
print('Valor de la primera fila y última columna del DataFrame:')
print(df.iloc[0][2])
print()

# Seleccionar los valores de la primera fila del DataFrame
print('Valores de la primera fila del DataFrame:')
print(df.loc[0])
print()

print('Valores de la primera fila del DataFrame:')
print(df.iloc[0, :])
