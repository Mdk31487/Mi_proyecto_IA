# inteligencia_artificial.py

import sqlite3

# Funciones de procesamiento
def obtener_sinonimos(palabra):
    # Aquí iría la lógica para obtener sinónimos
    return ["alegre", "contento", "jovial"]  # Ejemplo

def limpiar_texto(texto):
    # Aquí iría la lógica para limpiar texto
    return texto.lower().strip()

def traducir_texto(texto, idioma_destino='es'):
    # Aquí iría la lógica para traducir texto
    return "Hola, ¿cómo estás?"  # Ejemplo

def es_palabra_valida(palabra, idioma='es'):
    # Aquí iría la lógica para verificar si una palabra es válida
    return True  # Ejemplo

# Funciones para manejar la base de datos
def crear_base_de_datos():
    conn = sqlite3.connect('ia.db')  # Conectar a la base de datos
    cursor = conn.cursor()
    
    # Crear tablas si no existen
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sinonimos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        palabra TEXT,
        sinonimos TEXT
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS traducciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        texto_original TEXT,
        traduccion TEXT,
        idioma_destino TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS palabras_validas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        palabra TEXT,
        es_valida INTEGER
    )''')
    
    conn.commit()
    conn.close()

# Funciones para guardar datos en la base de datos
def guardar_sinonimos(palabra, sinonimos):
    conn = sqlite3.connect('ia.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sinonimos (palabra, sinonimos) VALUES (?, ?)", (palabra, ', '.join(sinonimos)))
    conn.commit()
    conn.close()

def guardar_traduccion(texto_original, traduccion, idioma_destino):
    conn = sqlite3.connect('ia.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO traducciones (texto_original, traduccion, idioma_destino) VALUES (?, ?, ?)", (texto_original, traduccion, idioma_destino))
    conn.commit()
    conn.close()

def guardar_palabra_valida(palabra, es_valida):
    conn = sqlite3.connect('ia.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO palabras_validas (palabra, es_valida) VALUES (?, ?)", (palabra, 1 if es_valida else 0))
    conn.commit()
    conn.close()

# Clase principal de la IA
class InteligenciaArtificial:
    def __init__(self):
        pass

    def obtener_sinonimos(self, palabra):
        try:
            sinonimos = obtener_sinonimos(palabra)
            if sinonimos:
                guardar_sinonimos(palabra, sinonimos)  # Guardamos los sinónimos en la base de datos
            return sinonimos
        except Exception as e:
            print(f"Error al obtener los sinónimos: {e}")
            return None

    def limpiar_texto(self, texto):
        try:
            return limpiar_texto(texto)
        except Exception as e:
            print(f"Error al limpiar el texto: {e}")
            return None

    def traducir_texto(self, texto, idioma_destino='es'):
        try:
            traduccion = traducir_texto(texto, idioma_destino)
            if traduccion:
                guardar_traduccion(texto, traduccion, idioma_destino)  # Guardamos la traducción
            return traduccion
        except Exception as e:
            print(f"Error al traducir el texto: {e}")
            return None

    def es_palabra_valida(self, palabra, idioma='es'):
        try:
            es_valida = es_palabra_valida(palabra, idioma)
            guardar_palabra_valida(palabra, es_valida)  # Guardamos si la palabra es válida
            return es_valida
        except Exception as e:
            print(f"Error al validar la palabra: {e}")
            return False
