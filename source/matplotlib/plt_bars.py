import matplotlib.pyplot as plt

# Definir los datos
x1, y1 = [0.25, 1.25, 2.25, 3.25, 4.25], [10, 55, 80, 32, 40]
x2, y2 = [0.75, 1.75, 2.75, 3.75, 4.75], [42, 26, 10, 29, 66]

# Configurar las características del gráfico

plt.bar(x1, y1, label='Datos 1', width=0.5, color='lightblue')
plt.bar(x2, y2, label='Datos 2', width=0.5, color='orange')

# Definir título y nombre de los ejes
plt.title('Gráfico de barras')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

# Mostrar leyenda y figura
plt.legend()
plt.show()
