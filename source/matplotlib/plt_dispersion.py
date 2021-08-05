import matplotlib.pyplot as plt

# Define los datos
x1, y1 = [0.25, 1.25, 2.25, 3.25, 4.25], [10, 55, 80, 32, 40]
x2, y2 = [0.75, 1.75, 2.75, 3.75, 4.75], [42, 26, 10, 29, 66]

# Configurar las características del gráfico
plt.scatter(x1, y1, label='Datos 1', color='red')
plt.scatter(x2, y2, label='Datos 2', color='purple')

# Definir título y nombres de los ejes
plt.title('Gráfico de dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar leyenda y figura
plt.legend()
plt.show()
