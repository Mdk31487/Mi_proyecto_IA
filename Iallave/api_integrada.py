from flask import Flask, request, jsonify
import pickle
import numpy as np
import tensorflow as tf
import os
import sys
from transformers import pipeline
import base64
from PIL import Image
import io

# Añadir el directorio del proyecto_ia al path para importar sus módulos
sys.path.append('../proyecto_ia')

app = Flask(__name__)

# Cargar el modelo de clasificación Iris previamente entrenado
try:
    with open('modelo_mejorado.pkl', 'rb') as file:
        iris_model = pickle.load(file)
    print("Modelo de clasificación Iris cargado exitosamente.")
except Exception as e:
    print(f"Error al cargar el modelo de clasificación Iris: {e}")
    iris_model = None

# Cargar el modelo de clasificación de imágenes MNIST
try:
    mnist_model = tf.keras.models.load_model('../proyecto_ia/modelos/mejor_modelo.h5')
    mnist_model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    print("Modelo de clasificación MNIST cargado exitosamente.")
except Exception as e:
    print(f"Error al cargar el modelo de clasificación MNIST: {e}")
    mnist_model = None

# Usar un modelo de lenguaje preentrenado para conversación
try:
    conversational_pipeline = pipeline("text-generation", model="facebook/blenderbot-400M-distill")
    print("Modelo de conversación cargado exitosamente.")
except Exception as e:
    print(f"Error al cargar el modelo de conversación: {e}")
    conversational_pipeline = None

# Endpoint para clasificación de flores Iris
@app.route('/predict/iris', methods=['POST'])
def predict_iris():
    if iris_model is None:
        return jsonify({'error': 'Modelo de clasificación Iris no cargado correctamente.'}), 500

    try:
        data = request.get_json()
        features = data['features']

        # Convertir los datos a un formato adecuado para hacer la predicción
        sample_data = np.array(features).reshape(1, -1)

        # Realizar la predicción
        prediction = iris_model.predict(sample_data)[0]
        probabilities = iris_model.predict_proba(sample_data)[0]

        # Mapear la predicción a nombres de especies
        especies = ["Setosa", "Versicolor", "Virginica"]
        especie_predicha = especies[int(prediction)]

        # Devolver la respuesta en formato JSON
        response = jsonify({
            'prediction': int(prediction),
            'especie': especie_predicha,
            'probabilidades': {
                "Setosa": float(probabilities[0]),
                "Versicolor": float(probabilities[1]),
                "Virginica": float(probabilities[2])
            }
        })
        response.charset = 'utf-8'
        return response

    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al procesar los datos: {e}'}), 400

# Endpoint para clasificación de dígitos MNIST
@app.route('/predict/mnist', methods=['POST'])
def predict_mnist():
    if mnist_model is None:
        return jsonify({'error': 'Modelo de clasificación MNIST no cargado correctamente.'}), 500

    try:
        # Obtener la imagen en formato base64
        data = request.get_json()
        image_base64 = data['image']
        
        # Decodificar la imagen base64
        image_data = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_data))
        
        # Preprocesar la imagen para MNIST (convertir a escala de grises, redimensionar a 28x28, normalizar)
        image = image.convert('L')  # Convertir a escala de grises
        image = image.resize((28, 28))  # Redimensionar a 28x28
        image_array = np.array(image) / 255.0  # Normalizar
        
        # Reshape para el modelo
        image_array = image_array.reshape(1, 28, 28, 1)
        
        # Realizar la predicción
        prediction = mnist_model.predict(image_array, verbose=0)
        digit = np.argmax(prediction[0])
        confidence = float(prediction[0][digit])
        
        # Devolver la respuesta en formato JSON
        response = jsonify({
            'digit': int(digit),
            'confidence': confidence,
            'probabilities': {str(i): float(prediction[0][i]) for i in range(10)}
        })
        response.charset = 'utf-8'
        return response

    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al procesar la imagen: {e}'}), 400

# Endpoint para conversar con la IA
@app.route('/ask', methods=['POST'])
def ask():
    if conversational_pipeline is None:
        return jsonify({'error': 'Modelo de conversación no cargado correctamente.'}), 500

    try:
        question = request.get_json()['question']  # Obtener la pregunta

        # Procesar la pregunta y dar una respuesta
        if "nombre" in question.lower():
            answer = "Soy un asistente de IA integrado que puede clasificar flores, reconocer dígitos y mantener conversaciones."
        elif "cómo estás" in question.lower():
            answer = "¡Estoy bien, gracias por preguntar! ¿Y tú?"
        elif "qué puedes hacer" in question.lower():
            answer = "Puedo clasificar especies de flores Iris, reconocer dígitos escritos a mano y mantener conversaciones. ¿En qué puedo ayudarte?"
        else:
            # Usar el modelo de conversación para preguntas más complejas
            response = conversational_pipeline(question, max_length=50, num_return_sequences=1)
            answer = response[0]['generated_text']

        # Asegurarse de que la respuesta esté en UTF-8
        response = jsonify({'answer': answer})
        response.charset = 'utf-8'
        return response

    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al procesar la pregunta: {e}'}), 400

# Endpoint para obtener información sobre los modelos
@app.route('/models/info', methods=['GET'])
def models_info():
    info = {
        'iris_model': {
            'loaded': iris_model is not None,
            'type': str(type(iris_model).__name__) if iris_model else None,
            'description': 'Modelo para clasificar especies de flores Iris basado en características de pétalos y sépalos.'
        },
        'mnist_model': {
            'loaded': mnist_model is not None,
            'type': 'Sequential' if mnist_model else None,
            'description': 'Modelo para reconocer dígitos escritos a mano (0-9) en imágenes.'
        },
        'conversational_model': {
            'loaded': conversational_pipeline is not None,
            'type': 'Pipeline' if conversational_pipeline else None,
            'description': 'Modelo para mantener conversaciones naturales con los usuarios.'
        }
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False) 