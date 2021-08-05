import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss

mu, sigma = 36, 8

X = ss.norm(mu, sigma)

answer = X.ppf(0.05)
print(answer)

graph = np.arange(X.ppf(0.01), X.ppf(0.99))
plt.plot(graph, X.pdf(graph), 'b')

plt.title('Distribución Normal')
plt.ylabel('Probabilidad')
plt.xlabel('Duración (meses)')

plt.show()
