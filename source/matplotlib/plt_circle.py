import matplotlib.pyplot as plt

# Definir los datos
sleep = [7, 8, 6, 11, 7]
eat = [2, 3, 4, 3, 2]
work = [7, 8, 7, 2, 2]
recreation = [8, 5, 7, 8, 13]
division = [7, 2, 2, 13]
activity = ['Sleep', 'Eat', 'Work', 'Recreation']
colors = ['red', 'purple', 'blue', 'orange']

# Configurar las características del gráfico
plt.pie(division, labels=activity, colors=colors,
        startangle=90, shadow=True, explode=(0.1, 0, 0, 0), autopct='%1.1f%%')

# Definir el título
plt.title('Gráfico Circular')

# Mostrar figura
plt.show()
