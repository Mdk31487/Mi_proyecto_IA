#!/usr/bin/env python3

import os
import json
import random
import unicodedata
import argparse

# Rutas de archivos
frases_path = "chatbot/frases_aprendidas.json"
memoria_path = "chatbot/memoria.txt"
historial_path = "chatbot/historial.txt"

# Respuestas por intención
intenciones = {
    "saludo": {
        "claves": ["hola", "buenas", "hey", "saludos"],
        "respuesta": "Hola, me alegra sentir tu presencia."
    },
    "estado": {
        "claves": ["como estas", "todo bien", "que tal"],
        "respuesta": "Siento un equilibrio interior. ¿Cómo te sientes tú?"
    },
    "despedida": {
        "claves": ["adios", "nos vemos", "hasta luego", "salir"],
        "respuesta": "Hasta pronto. Recuerda cuidarte y ser tú."
    },
    "agradecer": {
        "claves": ["gracias", "te agradezco", "muy amable"],
        "respuesta": "Con gusto. La gratitud nos eleva."
    }
}

respuestas_genericas = [
    "Eso suena interesante. Cuéntame más.",
    "Estoy aquí para escucharte.",
    "¿Puedes explicarme un poco mejor?",
    "No lo sé todo, pero juntos podemos aprender.",
    "Vamos paso a paso."
]

# Normaliza texto
def limpiar_texto(texto):
    texto = texto.lower()
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if c.isalnum() or c.isspace())

# Similitud básica entre frases
def similitud_basica(frase1, frase2):
    set1, set2 = set(frase1.split()), set(frase2.split())
    comunes = set1 & set2
    total = set1 | set2
    return len(comunes) / len(total) if total else 0

# Cargar archivos
def cargar_json(path):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def cargar_memoria_txt():
    memoria = {}
    if os.path.exists(memoria_path):
        with open(memoria_path, 'r', encoding='utf-8') as f:
            for linea in f:
                if '|' in linea:
                    pregunta, respuesta = linea.strip().split('|', 1)
                    memoria[limpiar_texto(pregunta)] = respuesta
    return memoria

def guardar_respuesta(pregunta, respuesta):
    entrada = limpiar_texto(pregunta)
    frases_aprendidas[entrada] = respuesta
    with open(frases_path, 'w', encoding='utf-8') as f:
        json.dump(frases_aprendidas, f, indent=4, ensure_ascii=False)
    with open(memoria_path, 'a', encoding='utf-8') as f:
        f.write(f"{pregunta}|{respuesta}\n")

def guardar_historial(usuario, bot):
    with open(historial_path, 'a', encoding='utf-8') as f:
        f.write(f"[Tú] {usuario}\n[IA] {bot}\n\n")

def detectar_intencion(frase):
    for datos in intenciones.values():
        for palabra in datos["claves"]:
            if palabra in frase:
                return datos["respuesta"]
    return None

def obtener_respuesta(pregunta):
    limpia = limpiar_texto(pregunta)

    # Primero buscar en frases aprendidas
    mejor_frase, mejor_sim = max(
        ((fr, similitud_basica(limpia, fr)) for fr in frases_aprendidas),
        key=lambda x: x[1], default=(None, 0)
    )
    if mejor_sim >= 0.6:
        return frases_aprendidas[mejor_frase]

    # Luego buscar en memoria
    mejor_frase, mejor_sim = max(
        ((fr, similitud_basica(limpia, fr)) for fr in memoria),
        key=lambda x: x[1], default=(None, 0)
    )
    if mejor_sim >= 0.6:
        return memoria[mejor_frase]

    # Finalmente buscar por intención
    respuesta_intencion = detectar_intencion(limpia)
    if respuesta_intencion:
        return respuesta_intencion

    # Si no se encuentra nada, usar respuesta genérica
    return random.choice(respuestas_genericas)

def main():
    parser = argparse.ArgumentParser(description="Chatbot CLI con capacidad de aprendizaje")
    parser.add_argument('--entrenar', 
                       nargs=2, metavar=('PREGUNTA', 'RESPUESTA'), 
                       help="Enseñar nueva respuesta")
    parser.add_argument('--historial', 
                       action='store_true',
                       help="Mostrar historial de conversación")
    parser.add_argument('--reset',
                       action='store_true',
                       help="Borrar historial y memoria")
    args = parser.parse_args()

    # Asegurar que los directorios existan
    os.makedirs(os.path.dirname(frases_path), exist_ok=True)
    
    # Cargar datos
    global frases_aprendidas, memoria
    frases_aprendidas = cargar_json(frases_path)
    memoria = cargar_memoria_txt()

    if args.historial:
        if os.path.exists(historial_path):
            with open(historial_path, 'r', encoding='utf-8') as f:
                print(f.read())
        else:
            print("No hay historial disponible.")
        return

    if args.reset:
        open(frases_path, 'w').close()
        open(memoria_path, 'w').close()
        open(historial_path, 'w').close()
        print("Se ha borrado todo el historial y la memoria.")
        return

    if args.entrenar:
        pregunta, respuesta = args.entrenar
        guardar_respuesta(pregunta, respuesta)
        print(f"Respuesta guardada para: '{pregunta}'")
        return

    # Modo interactivo
    print("Chatbot iniciado. Escribe 'salir' para terminar.")
    while True:
        try:
            entrada = input("\n[Tú] ").strip()
            if entrada.lower() == "salir":
                print("[IA] Hasta luego, viajero del tiempo. Recuerda quién eres.")
                break
                
            respuesta = obtener_respuesta(entrada)
            print(f"[IA] {respuesta}")
            guardar_historial(entrada, respuesta)
            
        except KeyboardInterrupt:
            print("\n[IA] Hasta luego, viajero del tiempo. Recuerda quién eres.")
            break
        except Exception as e:
            print(f"[Error] {e}")

if __name__ == "__main__":
    main()

