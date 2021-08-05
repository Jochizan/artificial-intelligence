import matplotlib.pyplot as plt

# Definir los datos
x1, y1 = [3, 4, 5, 6], [5, 6, 3, 4]
x2, y2 = [2, 5, 8], [3, 4, 3]

# Configurar las características del gráfico
plt.plot(x1, y1, label='Línea 1', linewidth=4, color='blue')
plt.plot(x2, y2, label='Línea 2', linewidth=4, color='red')

# Definir título y nombre de ejes
plt.title('Diagrama de Líneas')
plt.ylabel('Eje Y')
plt.xlabel('Eje X')

# Mostrar leyenda, cuadrícula, figura
plt.legend()
plt.grid()
plt.show()
