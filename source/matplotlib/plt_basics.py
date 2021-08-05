import matplotlib.pyplot as plt

a, b = [1, 2, 3, 4], [11, 22, 33, 44]

plt.plot(a, b, color='blue', linewidth=3, label='Línea')
plt.legend()
plt.show()
