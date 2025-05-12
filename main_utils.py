import re
import random
import string
from hashlib import sha256
from datetime import datetime
from googletrans import Translator
from spellchecker import SpellChecker
import nltk
from nltk.corpus import wordnet
import math

# Funciones de validación
def validar_email(email):
    """Valida si el correo electrónico tiene un formato correcto."""
    try:
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(patron, email))
    except Exception as e:
        print(f"Error al validar el correo: {e}")
        return False

def es_numero_telefono_valido(telefono):
    """Valida si el número de teléfono tiene un formato correcto."""
    try:
        patron = r"^\+?1?\d{9,15}$"
        return bool(re.match(patron, telefono))
    except Exception as e:
        print(f"Error al validar el número de teléfono: {e}")
        return False

# Funciones de encriptación y generación
def encriptar_contraseña(password):
    """Encripta la contraseña usando SHA256."""
    try:
        return sha256(password.encode()).hexdigest()
    except Exception as e:
        print(f"Error al encriptar la contraseña: {e}")
        return None

def generar_token(longitud=32):
    """Genera un token aleatorio de la longitud especificada."""
    try:
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(longitud))
    except Exception as e:
        print(f"Error al generar el token: {e}")
        return None

# Funciones matemáticas
def raiz_cuadrada(x):
    """Devuelve la raíz cuadrada de un número."""
    try:
        if x < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(x)
    except Exception as e:
        print(f"Error al calcular la raíz cuadrada: {e}")
        return None

def calcular_factorial(n):
    """Devuelve el factorial de un número."""
    try:
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        return math.factorial(n)
    except Exception as e:
        print(f"Error al calcular el factorial: {e}")
        return None

def mcd(a, b):
    """Devuelve el máximo común divisor de dos números."""
    try:
        return math.gcd(a, b)
    except Exception as e:
        print(f"Error al calcular el MCD: {e}")
        return None

def calcular_potencia(base, exponente):
    """Devuelve la base elevada al exponente."""
    try:
        return math.pow(base, exponente)
    except Exception as e:
        print(f"Error al calcular la potencia: {e}")
        return None

def calcular_logaritmo(x, base=10):
    """Devuelve el logaritmo de x en la base especificada (por defecto base 10)."""
    try:
        if x <= 0:
            raise ValueError("El logaritmo no está definido para números menores o iguales a cero.")
        return math.log(x, base)
    except Exception as e:
        print(f"Error al calcular el logaritmo: {e}")
        return None

# Funciones de manejo de texto
def convertir_a_mayusculas(texto):
    """Convierte todo el texto a mayúsculas."""
    try:
        return texto.upper()
    except Exception as e:
        print(f"Error al convertir el texto a mayúsculas: {e}")
        return None

def convertir_a_minusculas(texto):
    """Convierte todo el texto a minúsculas."""
    try:
        return texto.lower()
    except Exception as e:
        print(f"Error al convertir el texto a minúsculas: {e}")
        return None

def convertir_a_titulo(texto):
    """Convierte el texto a formato título (capitaliza la primera letra de cada palabra)."""
    try:
        return texto.title()
    except Exception as e:
        print(f"Error al convertir el texto a formato título: {e}")
        return None

def contar_palabras(texto):
    """Cuenta la cantidad de palabras en una cadena de texto."""
    try:
        palabras = texto.split()
        return len(palabras)
    except Exception as e:
        print(f"Error al contar palabras: {e}")
        return None

# Funciones de fecha y hora
def obtener_fecha_actual():
    """Devuelve la fecha y hora actual."""
    try:
        return datetime.now()
    except Exception as e:
        print(f"Error al obtener la fecha actual: {e}")
        return None

def formatear_fecha(fecha, formato="%Y-%m-%d %H:%M:%S"):
    """Devuelve la fecha en el formato especificado."""
    try:
        return fecha.strftime(formato)
    except Exception as e:
        print(f"Error al formatear la fecha: {e}")
        return None

# Funciones adicionales
def obtener_sinonimos(palabra):
    """Devuelve una lista de sinónimos para una palabra."""
    try:
        nltk.download('wordnet')
        sinonimos = set()
        for syn in wordnet.synsets(palabra):
            for lemma in syn.lemmas():
                sinonimos.add(lemma.name())
        return list(sinonimos)
    except Exception as e:
        print(f"Error al obtener los sinónimos: {e}")
        return None

def limpiar_texto(texto):
    """Elimina todos los caracteres no alfabéticos del texto."""
    try:
        return re.sub(r'[^a-zA-Z\s]', '', texto)
    except Exception as e:
        print(f"Error al limpiar el texto: {e}")
        return None

def traducir_texto(texto, idioma_destino='es'):
    """Traduce el texto al idioma de destino especificado (por defecto es español)."""
    try:
        traductor = Translator()
        traduccion = traductor.translate(texto, dest=idioma_destino)
        return traduccion.text
    except Exception as e:
        print(f"Error al traducir el texto: {e}")
        return None

def es_palabra_valida(palabra, idioma='es'):
    """Verifica si una palabra es válida en el idioma especificado (por defecto español)."""
    try:
        corrector = SpellChecker(language=idioma)
        if palabra in corrector:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al validar la palabra: {e}")
        return False
