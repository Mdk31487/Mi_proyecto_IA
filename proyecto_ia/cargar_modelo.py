import tensorflow as tf

# Cargar el modelo
model = tf.keras.models.load_model("modelos/mejor_modelo.h5")

# Verificar que el modelo se ha cargado correctamente
model.summary()

# Compilar el modelo
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
