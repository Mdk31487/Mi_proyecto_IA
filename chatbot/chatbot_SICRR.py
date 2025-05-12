import json
import random
import os
import sys
import time
from datetime import datetime
import argparse
from sicrr import SICRR

class ChatbotSICRR:
    def __init__(self, frases_path='frases_aprendidas.json', memoria_path='memoria.txt', 
                 historial_path='historial.txt', saludo_path='saludo.json'):
        # Rutas de archivos
        self.frases_path = frases_path
        self.memoria_path = memoria_path
        self.historial_path = historial_path
        self.saludo_path = saludo_path
        
        # Cargar datos
        self.frases = self.cargar_frases()
        self.memoria = self.cargar_memoria()
        self.saludos = self.cargar_saludos()
        
        # Inicializar SICRR
        self.sicrr = SICRR(memoria_path='sicrr_memoria.json', personalidad_path='sicrr_personalidad.json')
        
        # Asegurar que el directorio existe
        os.makedirs('chatbot', exist_ok=True)
        
        # Cargar o crear historial
        if os.path.exists(self.historial_path):
            with open(self.historial_path, 'r', encoding='utf-8') as f:
                self.historial = f.readlines()
        else:
            self.historial = []
    
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
    
    def obtener_respuesta(self, texto, intencion):
        # Registrar la entrada en el historial
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.historial.append(f"[{timestamp}] [Tú] {texto}\n")
        
        # Procesar con SICRR si es una reflexión
        if intencion == "reflexion":
            reflexion = self.sicrr.introspeccion(texto)
            respuesta = f"Reflexiono: {reflexion}"
        else:
            # Buscar en memoria
            respuesta_encontrada = False
            for linea in self.memoria:
                if "|" in linea:
                    pregunta, respuesta = linea.strip().split("|", 1)
                    if pregunta.lower() in texto.lower():
                        respuesta = respuesta.strip()
                        respuesta_encontrada = True
                        break
            
            # Si no se encuentra en memoria, generar respuesta según intención
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
        print("Chatbot SICRR iniciado. Escribe 'salir' para terminar.")
        print("Este chatbot tiene capacidad de introspección y memoria reflexiva.")
        
        while True:
            texto = input("Tú: ")
            if texto.lower() == "salir":
                print("IA: Hasta pronto. Recuerda cuidarte y ser tú.")
                break
            
            intencion = self.detectar_intencion(texto)
            respuesta = self.obtener_respuesta(texto, intencion)
            print(f"IA: {respuesta}")
    
    def mostrar_memoria_sicrr(self):
        memoria = self.sicrr.recordar()
        print("\n=== Memoria SICRR ===")
        print("Reflexiones:")
        for reflexion in memoria["reflexiones"]:
            print(f"- {reflexion['momento']}: {reflexion['pensamiento']}")
            print(f"  Reflexión: {reflexion['reflexion']}")
        
        print("\nEmociones:")
        for emocion, intensidad in memoria["emociones"].items():
            print(f"- {emocion}: {intensidad}")
        
        print("\nEventos:")
        for evento in memoria["eventos"]:
            print(f"- {evento}")

def main():
    parser = argparse.ArgumentParser(description='Chatbot con capacidades de introspección SICRR')
    parser.add_argument('--frases', default='frases_aprendidas.json', help='Ruta al archivo de frases aprendidas')
    parser.add_argument('--memoria', default='memoria.txt', help='Ruta al archivo de memoria')
    parser.add_argument('--historial', default='historial.txt', help='Ruta al archivo de historial')
    parser.add_argument('--saludo', default='saludo.json', help='Ruta al archivo de saludos')
    parser.add_argument('--mostrar-memoria', action='store_true', help='Mostrar la memoria SICRR al inicio')
    
    args = parser.parse_args()
    
    chatbot = ChatbotSICRR(
        frases_path=args.frases,
        memoria_path=args.memoria,
        historial_path=args.historial,
        saludo_path=args.saludo
    )
    
    if args.mostrar_memoria:
        chatbot.mostrar_memoria_sicrr()
    
    chatbot.iniciar_conversacion()

if __name__ == "__main__":
    main() 