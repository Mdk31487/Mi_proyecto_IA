import json
import random
import os
import sys
import time
import numpy as np
from datetime import datetime
import argparse
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ChatbotAvanzado:
    def __init__(self, frases_path='frases_aprendidas.json', memoria_path='memoria.txt', 
                 historial_path='historial.txt', saludo_path='saludo.json',
                 modelo_path='modelo_chatbot.h5', tokenizer_path='tokenizer.pkl',
                 vectorizer_path='vectorizer.pkl'):
        # Rutas de archivos
        self.frases_path = frases_path
        self.memoria_path = memoria_path
        self.historial_path = historial_path
        self.saludo_path = saludo_path
        self.modelo_path = modelo_path
        self.tokenizer_path = tokenizer_path
        self.vectorizer_path = vectorizer_path
        
        # Cargar datos
        self.frases = self.cargar_frases()
        self.memoria = self.cargar_memoria()
        self.saludos = self.cargar_saludos()
        
        # Asegurar que el directorio existe
        os.makedirs('chatbot', exist_ok=True)
        
        # Cargar o crear historial
        if os.path.exists(self.historial_path):
            with open(self.historial_path, 'r', encoding='utf-8') as f:
                self.historial = f.readlines()
        else:
            self.historial = []
        
        # Inicializar o cargar modelos
        self.inicializar_modelos()
    
    def cargar_frases(self):
        try:
            with open(self.frases_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"saludos": [], "despedidas": [], "preguntas": [], "respuestas": []}
    
    def cargar_memoria(self):
        try:
            with open(self.memoria_path, 'r', encoding='utf-8') as f:
                return f.readlines()
        except FileNotFoundError:
            return []
    
    def cargar_saludos(self):
        try:
            with open(self.saludo_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {"saludos": ["Hola", "Buenos días", "Buenas tardes", "Buenas noches"]}
    
    def guardar_historial(self):
        with open(self.historial_path, 'w', encoding='utf-8') as f:
            f.writelines(self.historial)
    
    def inicializar_modelos(self):
        # Verificar si existen modelos preentrenados
        if os.path.exists(self.modelo_path) and os.path.exists(self.tokenizer_path):
            try:
                # Cargar modelo y tokenizer
                self.modelo = load_model(self.modelo_path)
                with open(self.tokenizer_path, 'rb') as f:
                    self.tokenizer = pickle.load(f)
                print("Modelo de lenguaje cargado exitosamente.")
            except Exception as e:
                print(f"Error al cargar el modelo: {e}")
                self.crear_modelo()
        else:
            self.crear_modelo()
        
        # Inicializar o cargar vectorizador para búsqueda semántica
        if os.path.exists(self.vectorizer_path):
            try:
                with open(self.vectorizer_path, 'rb') as f:
                    self.vectorizer = pickle.load(f)
                print("Vectorizador cargado exitosamente.")
            except Exception as e:
                print(f"Error al cargar el vectorizador: {e}")
                self.vectorizer = TfidfVectorizer()
                self.entrenar_vectorizador()
        else:
            self.vectorizer = TfidfVectorizer()
            self.entrenar_vectorizador()
    
    def crear_modelo(self):
        # Crear un modelo simple de LSTM para generación de texto
        self.tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
        
        # Entrenar el tokenizer con las frases de memoria
        textos = []
        for linea in self.memoria:
            if "|" in linea:
                pregunta, respuesta = linea.strip().split("|", 1)
                textos.append(pregunta)
                textos.append(respuesta.strip())
        
        if textos:
            self.tokenizer.fit_on_texts(textos)
            
            # Crear secuencias para entrenamiento
            sequences = self.tokenizer.texts_to_sequences(textos)
            padded_sequences = pad_sequences(sequences, maxlen=20, padding='post', truncating='post')
            
            # Crear modelo
            self.modelo = Sequential([
                Embedding(5000, 128, input_length=20),
                LSTM(128, return_sequences=True),
                LSTM(64),
                Dense(64, activation='relu'),
                Dropout(0.5),
                Dense(5000, activation='softmax')
            ])
            
            self.modelo.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
            
            # Guardar modelo y tokenizer
            self.modelo.save(self.modelo_path)
            with open(self.tokenizer_path, 'wb') as f:
                pickle.dump(self.tokenizer, f)
            
            print("Modelo de lenguaje creado y guardado exitosamente.")
        else:
            print("No hay suficientes datos para crear el modelo. Se usará el modo básico.")
            self.modelo = None
    
    def entrenar_vectorizador(self):
        # Entrenar el vectorizador con las frases de memoria
        textos = []
        for linea in self.memoria:
            if "|" in linea:
                pregunta, respuesta = linea.strip().split("|", 1)
                textos.append(pregunta)
                textos.append(respuesta.strip())
        
        if textos:
            self.vectorizer.fit(textos)
            
            # Guardar vectorizador
            with open(self.vectorizer_path, 'wb') as f:
                pickle.dump(self.vectorizer, f)
            
            print("Vectorizador entrenado y guardado exitosamente.")
        else:
            print("No hay suficientes datos para entrenar el vectorizador.")
    
    def detectar_intencion(self, texto):
        texto = texto.lower()
        
        # Detectar saludos
        if any(saludo.lower() in texto for saludo in self.saludos["saludos"]):
            return "saludo"
        
        # Detectar despedidas
        if any(despedida.lower() in texto for despedida in ["adiós", "hasta luego", "chao", "salir"]):
            return "despedida"
        
        # Detectar preguntas
        if "?" in texto or any(palabra in texto for palabra in ["qué", "cómo", "cuándo", "dónde", "por qué"]):
            return "pregunta"
        
        return "general"
    
    def buscar_respuesta_semantica(self, texto):
        # Buscar respuesta semántica usando similitud de coseno
        if not hasattr(self, 'vectorizer') or not self.vectorizer:
            return None
        
        # Vectorizar el texto de entrada
        texto_vectorizado = self.vectorizer.transform([texto])
        
        # Vectorizar todas las preguntas en memoria
        preguntas = []
        respuestas = []
        for linea in self.memoria:
            if "|" in linea:
                pregunta, respuesta = linea.strip().split("|", 1)
                preguntas.append(pregunta)
                respuestas.append(respuesta.strip())
        
        if not preguntas:
            return None
        
        preguntas_vectorizadas = self.vectorizer.transform(preguntas)
        
        # Calcular similitud
        similitudes = cosine_similarity(texto_vectorizado, preguntas_vectorizadas)[0]
        
        # Encontrar la pregunta más similar
        indice_max = np.argmax(similitudes)
        similitud_max = similitudes[indice_max]
        
        # Si la similitud es mayor a un umbral, devolver la respuesta correspondiente
        if similitud_max > 0.5:
            return respuestas[indice_max]
        
        return None
    
    def generar_respuesta_lstm(self, texto):
        # Generar respuesta usando el modelo LSTM
        if not hasattr(self, 'modelo') or not self.modelo or not self.tokenizer:
            return None
        
        # Tokenizar y secuenciar el texto
        secuencia = self.tokenizer.texts_to_sequences([texto])
        secuencia_padded = pad_sequences(secuencia, maxlen=20, padding='post', truncating='post')
        
        # Generar predicción
        prediccion = self.modelo.predict(secuencia_padded, verbose=0)
        
        # Convertir predicción a texto
        indices = np.argsort(prediccion[0])[-5:][::-1]  # Top 5 palabras más probables
        palabras = []
        for idx in indices:
            for palabra, i in self.tokenizer.word_index.items():
                if i == idx:
                    palabras.append(palabra)
                    break
        
        # Construir respuesta
        respuesta = " ".join(palabras)
        return respuesta
    
    def obtener_respuesta(self, texto, intencion):
        # Registrar la entrada en el historial
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.historial.append(f"[{timestamp}] [Tú] {texto}\n")
        
        # Buscar en memoria exacta
        respuesta_encontrada = False
        for linea in self.memoria:
            if "|" in linea:
                pregunta, respuesta = linea.strip().split("|", 1)
                if pregunta.lower() in texto.lower():
                    respuesta = respuesta.strip()
                    respuesta_encontrada = True
                    break
        
        # Si no se encuentra en memoria exacta, buscar respuesta semántica
        if not respuesta_encontrada:
            respuesta_semantica = self.buscar_respuesta_semantica(texto)
            if respuesta_semantica:
                respuesta = respuesta_semantica
                respuesta_encontrada = True
        
        # Si aún no se encuentra, generar respuesta con LSTM
        if not respuesta_encontrada:
            respuesta_lstm = self.generar_respuesta_lstm(texto)
            if respuesta_lstm and len(respuesta_lstm) > 10:  # Asegurar que la respuesta tenga sentido
                respuesta = respuesta_lstm
                respuesta_encontrada = True
        
        # Si aún no se encuentra, generar respuesta según intención
        if not respuesta_encontrada:
            if intencion == "saludo":
                respuesta = random.choice(self.saludos["saludos"])
            elif intencion == "despedida":
                respuesta = "Hasta pronto. Recuerda cuidarte y ser tú."
            elif intencion == "pregunta":
                respuesta = "Interesante pregunta. Estoy procesando la información para darte una respuesta adecuada."
            else:
                respuesta = "Entiendo lo que dices. ¿Podrías contarme más sobre eso?"
        
        # Registrar la respuesta en el historial
        self.historial.append(f"[{timestamp}] [IA] {respuesta}\n")
        self.guardar_historial()
        
        return respuesta
    
    def iniciar_conversacion(self):
        print("Chatbot Avanzado iniciado. Escribe 'salir' para terminar.")
        print("Este chatbot utiliza técnicas de aprendizaje profundo para mejorar sus respuestas.")
        
        while True:
            texto = input("Tú: ")
            if texto.lower() == "salir":
                print("IA: Hasta pronto. Recuerda cuidarte y ser tú.")
                break
            
            intencion = self.detectar_intencion(texto)
            respuesta = self.obtener_respuesta(texto, intencion)
            print(f"IA: {respuesta}")
    
    def entrenar_con_nuevos_datos(self, preguntas, respuestas):
        # Añadir nuevos datos a la memoria
        for pregunta, respuesta in zip(preguntas, respuestas):
            self.memoria.append(f"{pregunta}|{respuesta}\n")
        
        # Guardar memoria actualizada
        with open(self.memoria_path, 'w', encoding='utf-8') as f:
            f.writelines(self.memoria)
        
        # Reentrenar modelos
        self.entrenar_vectorizador()
        self.crear_modelo()
        
        print("Modelos reentrenados con nuevos datos.")

def main():
    parser = argparse.ArgumentParser(description='Chatbot Avanzado con técnicas de aprendizaje profundo')
    parser.add_argument('--frases', default='frases_aprendidas.json', help='Ruta al archivo de frases aprendidas')
    parser.add_argument('--memoria', default='memoria.txt', help='Ruta al archivo de memoria')
    parser.add_argument('--historial', default='historial.txt', help='Ruta al archivo de historial')
    parser.add_argument('--saludo', default='saludo.json', help='Ruta al archivo de saludos')
    parser.add_argument('--modelo', default='modelo_chatbot.h5', help='Ruta al archivo del modelo')
    parser.add_argument('--tokenizer', default='tokenizer.pkl', help='Ruta al archivo del tokenizer')
    parser.add_argument('--vectorizer', default='vectorizer.pkl', help='Ruta al archivo del vectorizador')
    
    args = parser.parse_args()
    
    chatbot = ChatbotAvanzado(
        frases_path=args.frases,
        memoria_path=args.memoria,
        historial_path=args.historial,
        saludo_path=args.saludo,
        modelo_path=args.modelo,
        tokenizer_path=args.tokenizer,
        vectorizer_path=args.vectorizer
    )
    
    chatbot.iniciar_conversacion()

if __name__ == "__main__":
    main() 