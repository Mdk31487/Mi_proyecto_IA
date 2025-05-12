import pickle
from sklearn.metrics import accuracy_score

# Cargar el modelo
with open('modelo_iris_9.pkl', 'rb') as file:
    model = pickle.load(file)

# Ver el tipo de modelo cargado
print(f"Modelo cargado: {type(model)}")

# Datos de ejemplo para predicción
sample_data = [[5.1, 3.5, 1.4, 0.2]]  # Cambia estos valores si necesitas probar otros casos
prediction = model.predict(sample_data)
probabilities = model.predict_proba(sample_data)

# Mostrar resultados
print(f"Predicción: {prediction}")
print(f"Probabilidades: {probabilities}")

# Si tienes datos de prueba (X_test, y_test), puedes evaluar la precisión del modelo
# Descomenta las siguientes líneas y proporciona X_test e y_test
"""
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Precisión del modelo: {accuracy:.2f}")
"""
