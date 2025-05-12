import json
import random
import os
import sys
import time
import numpy as np
from datetime import datetime
import argparse
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sicrr import SICRR

class ChatbotIntegrado:
    def __init__(self, frases_path='frases_aprendidas.json', memoria_path='memoria.txt', 
                 historial_path='historial.txt', saludo_path='saludo.json',
                 modelo_path='modelo_chatbot.pkl', vectorizer_path='vectorizer.pkl', 
                 sicrr_memoria_path='sicrr_memoria.json', sicrr_personalidad_path='sicrr_personalidad.json'):
        # Rutas de archivos
        self.frases_path = frases_path
        self.memoria_path = memoria_path
        self.historial_path = historial_path
        self.saludo_path = saludo_path
        self.modelo_path = modelo_path
        self.vectorizer_path = vectorizer_path
        
        # Cargar datos
        self.frases = self.cargar_frases()
        self.memoria = self.cargar_memoria()
        self.saludos = self.cargar_saludos()
        
        # Inicializar SICRR
        self.sicrr = SICRR(memoria_path=sicrr_memoria_path, personalidad_path=sicrr_personalidad_path)
        
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
        if os.path.exists(self.modelo_path) and os.path.exists(self.vectorizer_path):
            try:
                # Cargar modelo y vectorizador
                with open(self.modelo_path, 'rb') as f:
                    self.modelo = pickle.load(f)
                with open(self.vectorizer_path, 'rb') as f:
                    self.vectorizer = pickle.load(f)
                print("Modelo de lenguaje cargado exitosamente.")
            except Exception as e:
                print(f"Error al cargar el modelo: {e}")
                self.crear_modelo()
        else:
            self.crear_modelo()
    
    def crear_modelo(self):
        # Crear un modelo simple usando scikit-learn
        self.vectorizer = TfidfVectorizer(max_features=5000)
        
        # Preparar datos de entrenamiento
        textos = []
        etiquetas = []
        for linea in self.memoria:
            if "|" in linea:
                pregunta, respuesta = linea.strip().split("|", 1)
                textos.append(pregunta)
                etiquetas.append(respuesta.strip())
        
        if textos:
            # Entrenar vectorizador
            X = self.vectorizer.fit_transform(textos)
            
            # Crear y entrenar modelo
            self.modelo = MultinomialNB()
            self.modelo.fit(X, etiquetas)
            
            # Guardar modelo y vectorizador
            with open(self.modelo_path, 'wb') as f:
                pickle.dump(self.modelo, f)
            with open(self.vectorizer_path, 'wb') as f:
                pickle.dump(self.vectorizer, f)
            
            print("Modelo de lenguaje creado y guardado exitosamente.")
        else:
            print("No hay suficientes datos para crear el modelo. Se usará el modo básico.")
            self.modelo = None
    
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
        
        # Detectar reflexiones
        if any(palabra in texto for palabra in ["pienso", "creo", "opino", "reflexiono"]):
            return "reflexion"
        
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
    
    def generar_respuesta_modelo(self, texto):
        # Generar respuesta usando el modelo de scikit-learn
        if not hasattr(self, 'modelo') or not self.modelo or not self.vectorizer:
            return None
        
        # Vectorizar el texto
        texto_vectorizado = self.vectorizer.transform([texto])
        
        # Generar predicción
        try:
            respuesta = self.modelo.predict(texto_vectorizado)[0]
            return respuesta
        except Exception as e:
            print(f"Error al generar respuesta: {e}")
            return None
    
    def obtener_respuesta(self, texto, intencion):
        # Registrar la entrada en el historial
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.historial.append(f"[{timestamp}] [Tú] {texto}\n")
        
        # Procesar con SICRR si es una reflexión
        if intencion == "reflexion":
            reflexion = self.sicrr.introspeccion(texto)
            respuesta = f"Reflexiono: {reflexion}"
        else:
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
            
            # Si aún no se encuentra, generar respuesta con el modelo
            if not respuesta_encontrada:
                respuesta_modelo = self.generar_respuesta_modelo(texto)
                if respuesta_modelo and len(respuesta_modelo) > 10:  # Asegurar que la respuesta tenga sentido
                    respuesta = respuesta_modelo
                    respuesta_encontrada = True
            
            # Si aún no se encuentra, generar respuesta según intención
            if not respuesta_encontrada:
                if intencion == "saludo":
                    respuesta = random.choice(self.saludos["respuestas_saludo"])
                elif intencion == "despedida":
                    respuesta = "Hasta pronto. Recuerda cuidarte y ser tú."
                elif intencion == "pregunta":
                    respuesta = "Interesante pregunta. Estoy procesando la información para darte una respuesta adecuada."
                else:
                    respuesta = "Entiendo lo que dices. ¿Podrías contarme más sobre eso?"
        
        # Registrar la respuesta en el historial
        self.historial.append(f"[{timestamp}] [IA] {respuesta}\n")
        self.guardar_historial()
        
        # Registrar emoción en SICRR
        emociones = {
            "saludo": "amabilidad",
            "despedida": "nostalgia",
            "pregunta": "curiosidad",
            "reflexion": "contemplacion",
            "general": "neutralidad"
        }
        self.sicrr.registrar_emocion(emociones.get(intencion, "neutralidad"), 0.7)
        
        return respuesta
    
    def iniciar_conversacion(self):
        print("Chatbot Integrado iniciado. Escribe 'salir' para terminar.")
        print("Este chatbot combina técnicas de aprendizaje automático con capacidades de introspección.")
        
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
        
        # Reentrenar modelo
        self.crear_modelo()
        
        print("Modelo reentrenado con nuevos datos.")
    
    def mostrar_memoria_sicrr(self):
        print("\n=== Memoria SICRR ===")
        print("Reflexiones:")
        for reflexion in self.sicrr.memoria["reflexiones"]:
            print(f"- {reflexion['timestamp']}: {reflexion['texto']}")
            print(f"  Reflexión: {reflexion['reflexion']}")
        
        print("\nEmociones:")
        for emocion, conteo in self.sicrr.memoria["emociones"].items():
            print(f"- {emocion}: {conteo}")
        
        print("\nRegistro Emocional:")
        for registro in self.sicrr.memoria["registro_emocional"]:
            print(f"- {registro['timestamp']}: {registro['emocion']} (intensidad: {registro['intensidad']})")

def main():
    parser = argparse.ArgumentParser(description='Chatbot Integrado con técnicas de aprendizaje automático y capacidades de introspección')
    parser.add_argument('--frases', default='frases_aprendidas.json', help='Ruta al archivo de frases aprendidas')
    parser.add_argument('--memoria', default='memoria.txt', help='Ruta al archivo de memoria')
    parser.add_argument('--historial', default='historial.txt', help='Ruta al archivo de historial')
    parser.add_argument('--saludo', default='saludo.json', help='Ruta al archivo de saludos')
    parser.add_argument('--modelo', default='modelo_chatbot.pkl', help='Ruta al archivo del modelo')
    parser.add_argument('--vectorizer', default='vectorizer.pkl', help='Ruta al archivo del vectorizador')
    parser.add_argument('--sicrr-memoria', default='sicrr_memoria.json', help='Ruta al archivo de memoria SICRR')
    parser.add_argument('--sicrr-personalidad', default='sicrr_personalidad.json', help='Ruta al archivo de personalidad SICRR')
    parser.add_argument('--mostrar-memoria', action='store_true', help='Mostrar la memoria SICRR al inicio')
    
    args = parser.parse_args()
    
    chatbot = ChatbotIntegrado(
        frases_path=args.frases,
        memoria_path=args.memoria,
        historial_path=args.historial,
        saludo_path=args.saludo,
        modelo_path=args.modelo,
        vectorizer_path=args.vectorizer,
        sicrr_memoria_path=args.sicrr_memoria,
        sicrr_personalidad_path=args.sicrr_personalidad
    )
    
    if args.mostrar_memoria:
        chatbot.mostrar_memoria_sicrr()
    
    chatbot.iniciar_conversacion()

if __name__ == "__main__":
    main() 