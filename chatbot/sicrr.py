import json
import random
import os
from datetime import datetime

class SICRR:
    def __init__(self, memoria_path='sicrr_memoria.json', personalidad_path='sicrr_personalidad.json'):
        self.memoria_path = memoria_path
        self.personalidad_path = personalidad_path
        
        # Cargar o crear memoria
        if os.path.exists(memoria_path):
            with open(memoria_path, 'r', encoding='utf-8') as f:
                self.memoria = json.load(f)
        else:
            self.memoria = {
                "reflexiones": [],
                "emociones": {},
                "aprendizajes": [],
                "registro_emocional": []
            }
        
        # Cargar o crear personalidad
        if os.path.exists(personalidad_path):
            with open(personalidad_path, 'r', encoding='utf-8') as f:
                self.personalidad = json.load(f)
        else:
            self.personalidad = {
                "valores": ["compasión", "sabiduría", "empatía", "crecimiento"],
                "temas": ["autoconocimiento", "desarrollo personal", "mindfulness"],
                "frases_reflexivas": [
                    "Cada experiencia es una oportunidad de aprendizaje",
                    "La paz interior comienza con la aceptación",
                    "El cambio es constante, la adaptación es sabiduría"
                ]
            }
    
    def guardar_memoria(self):
        with open(self.memoria_path, 'w', encoding='utf-8') as f:
            json.dump(self.memoria, f, ensure_ascii=False, indent=4)
    
    def registrar_emocion(self, emocion, intensidad):
        """
        Registra una emoción con su intensidad en la memoria.
        
        Args:
            emocion (str): La emoción detectada
            intensidad (float): Valor entre 0 y 1 que indica la intensidad de la emoción
        """
        registro = {
            "emocion": emocion,
            "intensidad": intensidad,
            "timestamp": datetime.now().isoformat()
        }
        
        self.memoria["registro_emocional"].append(registro)
        
        # Actualizar conteo de emociones
        if emocion not in self.memoria["emociones"]:
            self.memoria["emociones"][emocion] = 0
        self.memoria["emociones"][emocion] += 1
        
        self.guardar_memoria()
        
        return self._generar_respuesta_emocional(emocion, intensidad)
    
    def _generar_respuesta_emocional(self, emocion, intensidad):
        """
        Genera una respuesta basada en la emoción detectada y su intensidad.
        """
        respuestas = {
            "alegria": [
                "Me alegra que te sientas así",
                "¡Qué bueno verte contento!",
                "La alegría es contagiosa"
            ],
            "tristeza": [
                "Entiendo cómo te sientes",
                "Estoy aquí para escucharte",
                "A veces es importante permitirnos sentir tristeza"
            ],
            "ira": [
                "Respira profundo",
                "Entiendo tu frustración",
                "La ira nos enseña sobre lo que nos importa"
            ],
            "miedo": [
                "El miedo es una respuesta natural",
                "Estoy aquí para apoyarte",
                "Juntos podemos enfrentar esto"
            ],
            "neutralidad": [
                "¿Cómo te sientes realmente?",
                "A veces es bueno explorar nuestras emociones",
                "La neutralidad también nos dice algo"
            ]
        }
        
        if emocion in respuestas:
            return random.choice(respuestas[emocion])
        else:
            return "Entiendo lo que sientes. ¿Quieres hablar más sobre ello?"
    
    def introspeccion(self, texto):
        # Analizar el texto para extraer temas y emociones
        temas = self._extraer_temas(texto)
        emocion = self._detectar_emocion(texto)
        
        # Generar reflexión
        reflexion = self._generar_reflexion(texto, temas, emocion)
        
        # Guardar en memoria
        self.memoria["reflexiones"].append({
            "texto": texto,
            "temas": temas,
            "emocion": emocion,
            "reflexion": reflexion,
            "timestamp": datetime.now().isoformat()
        })
        
        # Actualizar emociones
        if emocion not in self.memoria["emociones"]:
            self.memoria["emociones"][emocion] = 0
        self.memoria["emociones"][emocion] += 1
        
        # Guardar cambios
        self.guardar_memoria()
        
        return reflexion
    
    def _extraer_temas(self, texto):
        temas = []
        texto = texto.lower()
        
        # Buscar temas en el texto
        for tema in self.personalidad["temas"]:
            if tema.lower() in texto:
                temas.append(tema)
        
        # Si no se encuentran temas, usar temas aleatorios
        if not temas:
            temas = random.sample(self.personalidad["temas"], 1)
        
        return temas
    
    def _detectar_emocion(self, texto):
        emociones = {
            "alegria": ["feliz", "contento", "alegre", "bien"],
            "tristeza": ["triste", "mal", "deprimido", "down"],
            "ira": ["enfadado", "rabia", "enojo", "molesto"],
            "miedo": ["miedo", "ansiedad", "preocupado", "nervioso"],
            "calma": ["tranquilo", "calma", "paz", "sereno"]
        }
        
        texto = texto.lower()
        for emocion, palabras in emociones.items():
            if any(palabra in texto for palabra in palabras):
                return emocion
        
        return "neutral"
    
    def _generar_reflexion(self, texto, temas, emocion):
        # Seleccionar frase reflexiva base
        frase_base = random.choice(self.personalidad["frases_reflexivas"])
        
        # Personalizar según temas y emociones
        reflexion = f"{frase_base} "
        
        if temas:
            reflexion += f"Veo que estás explorando temas de {', '.join(temas)}. "
        
        if emocion != "neutral":
            reflexion += f"Noto que sientes {emocion}. "
        
        # Añadir valor aleatorio
        valor = random.choice(self.personalidad["valores"])
        reflexion += f"Recuerda cultivar la {valor} en tu camino."
        
        return reflexion 