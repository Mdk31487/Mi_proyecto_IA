import os
import json
import random
import unicodedata
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Rutas
frases_path = "frases_aprendidas.json"
historial_path = "historial.txt"

# Intenciones básicas
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
        "claves": ["adios", "nos vemos", "hasta luego"],
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

def limpiar_texto(texto):
    texto = texto.lower()
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if c.isalnum() or c.isspace())

def cargar_frases():
    if os.path.exists(frases_path):
        with open(frases_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def guardar_frases(frases):
    with open(frases_path, "w", encoding="utf-8") as f:
        json.dump(frases, f, indent=4, ensure_ascii=False)

def guardar_historial(usuario, bot):
    with open(historial_path, "a", encoding="utf-8") as f:
        f.write(f"[Tú] {usuario}\n[IA] {bot}\n\n")

def detectar_intencion(frase):
    for datos in intenciones.values():
        for clave in datos["claves"]:
            if clave in frase:
                return datos["respuesta"]
    return None

def obtener_respuesta_tfidf(pregunta, frases_aprendidas):
    if not frases_aprendidas:
        return None

    preguntas = list(frases_aprendidas.keys())
    vectorizador = TfidfVectorizer()
    tfidf = vectorizador.fit_transform(preguntas + [pregunta])
    similitudes = cosine_similarity(tfidf[-1], tfidf[:-1]).flatten()

    indice_max = similitudes.argmax()
    if similitudes[indice_max] > 0.4:
        return frases_aprendidas[preguntas[indice_max]]
    return None

# Carga inicial
frases_aprendidas = cargar_frases()

print("IA: Hola, ¿en qué te puedo ayudar hoy?")
print("Escribe 'salir' para terminar.\n")

while True:
    entrada = input("Tú: ").strip()
    limpia = limpiar_texto(entrada)
    if limpia == "salir":
        print("IA: Que estés bien. Hasta la próxima.")
        break

    # 1. Intención
    respuesta = detectar_intencion(limpia)

    # 2. Buscar en frases aprendidas por similitud
    if not respuesta:
        respuesta = obtener_respuesta_tfidf(limpia, frases_aprendidas)

    # 3. Si no hay nada, usar respuesta genérica
    if not respuesta:
        respuesta = random.choice(respuestas_genericas)

    print(f"IA: {respuesta}")
    guardar_historial(entrada, respuesta)

    # 4. Entrenar si es algo nuevo
    if limpia not in frases_aprendidas:
        entrenar = input("¿Quieres enseñarme cómo responder mejor a esto? (s/n): ").strip().lower()
        if entrenar == "s":
            nueva = input("Escribe la respuesta que debo dar: ").strip()
            frases_aprendidas[limpia] = nueva
            guardar_frases(frases_aprendidas)
            print("IA: Gracias. Aprendo contigo.\n")
