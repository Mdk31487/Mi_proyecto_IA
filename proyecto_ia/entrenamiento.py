import keras_tuner as kt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, regularizers

# 📌 Cargar y preprocesar los datos (Ejemplo con MNIST)
(x_train, y_train), (x_val, y_val) = keras.datasets.mnist.load_data()
x_train, x_val = x_train / 255.0, x_val / 255.0  # Normalización de datos

# 📌 Función para construir el modelo con hiperparámetros ajustables
def build_model(hp):
    model = keras.Sequential([
        layers.Flatten(input_shape=(28, 28)),  # Aplanar datos de entrada
        layers.Dense(hp.Int('units', 32, 512, step=32), activation='relu',
                     kernel_regularizer=regularizers.l2(0.01)),  # Regularización L2
        layers.Dropout(hp.Float('dropout', 0.0, 0.5, step=0.1)),  # Dropout para evitar sobreajuste
        layers.Dense(10, activation='softmax')  # 10 clases en MNIST
    ])

    model.compile(
        optimizer=keras.optimizers.Adam(hp.Choice('learning_rate', [1e-2, 1e-3, 1e-4])),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    return model

# 📌 Configurar la búsqueda de hiperparámetros con Keras Tuner
tuner = kt.RandomSearch(
    build_model,
    objective='val_accuracy',
    max_trials=5,  # Número de combinaciones de hiperparámetros a probar
    executions_per_trial=2,  # Veces que se ejecuta cada configuración
    directory='tuner_results',
    project_name='hyperparameter_tuning'
)

# 📌 Iniciar la búsqueda de hiperparámetros
tuner.search(x_train, y_train, epochs=10, validation_data=(x_val, y_val))

# 📌 Obtener los mejores hiperparámetros encontrados
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]

# 📌 Construir el mejor modelo con los hiperparámetros óptimos
best_model = tuner.hypermodel.build(best_hps)

# 📌 Guardar el mejor modelo en la carpeta "modelos"
model.save('modelos/mejor_modelo.h5')

print("✅ Entrenamiento completado. El mejor modelo se ha guardado en 'modelos/mejor_modelo.h5'.")
