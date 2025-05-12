import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Cargar el modelo
model = tf.keras.models.load_model("modelos/mejor_modelo.h5")

# Asegurar que el modelo esté compilado
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Cargar los datos
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Determinar la forma esperada por el modelo
input_shape = model.input_shape[1:]  # Extraer la forma esperada (ej. (28, 28) o (784,))
flatten_required = len(input_shape) == 1  # Verificar si el modelo espera (784,)

# Preprocesar los datos (normalización y one-hot encoding)
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

if flatten_required:
    X_train = X_train.reshape(-1, 784)  # Convertir a (None, 784) si es necesario
    X_test = X_test.reshape(-1, 784)

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Evaluar el modelo
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Pérdida: {loss:.4f}, Precisión: {accuracy:.4f}")
