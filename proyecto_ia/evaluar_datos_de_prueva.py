import tensorflow as tf
import numpy as np

# Definir rutas de los archivos
model_path = "/home/userland/mi_ia_backend/proyecto_ia/modelos/mejor_modelo.h5"
data_path = "/home/userland/mi_ia_backend/proyecto_ia/ruta_a_datos_de_prueba.npy"

# Cargar el modelo
try:
    model = tf.keras.models.load_model(model_path)
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    print("Modelo cargado correctamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    exit()

# Cargar datos de prueba
try:
    data = np.load(data_path, allow_pickle=True)
    if isinstance(data, tuple) and len(data) == 2:
        X_test, y_test = data
    else:
        raise ValueError("El archivo de datos no tiene el formato esperado.")
    print("Datos de prueba cargados correctamente.")
except Exception as e:
    print(f"Error al cargar los datos de prueba: {e}")
    exit()

# Evaluar el modelo en los datos de prueba
try:
    loss, acc = model.evaluate(X_test, y_test, verbose=1)
    print(f"Pérdida: {loss}, Precisión: {acc}")
except Exception as e:
    print(f"Error al evaluar el modelo: {e}")
