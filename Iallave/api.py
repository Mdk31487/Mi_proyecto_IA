from flask import Flask, request, jsonify
import pickle
import numpy as np
from transformers import pipeline

app = Flask(__name__)

# Cargar el modelo previamente entrenado de predicción
try:
    with open('modelo_mejorado.pkl', 'rb') as file:
        model = pickle.load(file)
    print("Modelo de predicción cargado exitosamente.")
except Exception as e:
    print(f"Error al cargar el modelo de predicción: {e}")
    model = None

# Usar un modelo de lenguaje preentrenado para conversación (actualizado)
conversational_pipeline = pipeline("text-generation", model="facebook/blenderbot-400M-distill")

# Endpoint para hacer predicciones
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Modelo de predicción no cargado correctamente.'}), 500

    # Verificar si los datos están en el formato correcto
    try:
        data = request.get_json()
        features = data['features']

        # Convertir los datos a un formato adecuado para hacer la predicción
        sample_data = np.array(features).reshape(1, -1)

        # Realizar la predicción
        prediction = model.predict(sample_data)[0]

        # Devolver la respuesta en formato JSON
        response = jsonify({'prediction': int(prediction)})
        response.charset = 'utf-8'  # Asegura que la respuesta esté en UTF-8
        return response

    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al procesar los datos: {e}'}), 400

# Endpoint para conversar con la IA
@app.route('/ask', methods=['POST'])
def ask():
    try:
        question = request.get_json()['question']  # Obtener la pregunta

        # Procesar la pregunta y dar una respuesta
        if "nombre" in question.lower():
            answer = "Soy un modelo entrenado para clasificar flores y responder preguntas simples."
        elif "cómo estás" in question.lower():
            answer = "¡Estoy bien, gracias por preguntar! ¿Y tú?"
        else:
            # Usar el modelo de conversación para preguntas más complejas
            response = conversational_pipeline(question, max_length=50, num_return_sequences=1)
            answer = response[0]['generated_text']

        # Asegurarse de que la respuesta esté en UTF-8
        response = jsonify({'answer': answer})
        response.charset = 'utf-8'  # Asegura que la respuesta esté en UTF-8
        return response

    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al procesar la pregunta: {e}'}), 400

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
