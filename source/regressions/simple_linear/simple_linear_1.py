from sklearn import linear_model

training_x = [[100, 10, 17, 37, 51, 20]]
training_y = [[200, 20, 34, 74, 102, 40]]

test_x = [[50, 5, 8, 18, 25, 10]]
test_y = [[100, 10, 16, 36, 50, 20]]

# Definir algoritmo de regresión lineal
algorithm = linear_model.LinearRegression()

# Entrenar el modelo
algorithm.fit(training_x, training_y)

# Predecir modelo
algorithm.predict(test_x)

# Conocer pendiente
a = algorithm.coef_

# Conocer intersección
b = algorithm.intercept_

print(a, b)

# Conocer precisión
precision = algorithm.score(test_x, test_y)
