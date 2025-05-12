import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Cargar modelo previamente entrenado
model = keras.models.load_model('modelos/mejor_modelo.h5')

# Cargar datos de prueba (Ejemplo con MNIST)
(_, _), (x_test, y_test) = keras.datasets.mnist.load_data()
x_test = x_test / 255.0  # Normalización

# Ajustar la forma de entrada si el modelo lo requiere (ejemplo: redes convolucionales)
if len(model.input_shape) == 4:  # Si el modelo espera 4D (ej. CNN)
    x_test = x_test.reshape(-1, 28, 28, 1)  

# Evaluar el modelo en los datos de prueba
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f'Precisión en test: {test_acc:.4f}')

# Generar predicciones
y_pred = model.predict(x_test, verbose=0).argmax(axis=1)

# Calcular la matriz de confusión
cm = confusion_matrix(y_test, y_pred)

# Visualizar la matriz de confusión
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", linewidths=0.5)
plt.xlabel("Predicción")
plt.ylabel("Real")
plt.title("Matriz de Confusión")
plt.tight_layout()
plt.show()
