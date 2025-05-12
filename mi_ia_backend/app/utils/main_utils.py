import re
from hashlib import sha256
import random
import string

def validar_email(email):
    """
    Valida si el correo electrónico tiene un formato correcto.
    """
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(patron, email):
        return True
    return False

def encriptar_contraseña(password):
    """
    Encripta la contraseña usando SHA256.
    """
    return sha256(password.encode()).hexdigest()

class RespuestaAPI:
    def __init__(self, exito, mensaje, datos=None):
        self.exito = exito
        self.mensaje = mensaje
        self.datos = datos or {}

    def formatear_respuesta(self):
        return {
            "exito": self.exito,
            "mensaje": self.mensaje,
            "datos": self.datos
        }

def generar_token(longitud=32):
    """
    Genera un token aleatorio de la longitud especificada.
    """
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))
import re
from hashlib import sha256
import random
import string

def validar_email(email):
    """
    Valida si el correo electrónico tiene un formato correcto.
    """
    try:
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(patron, email):
            return True
        return False
    except Exception as e:
        print(f"Error al validar el correo: {e}")
        return False

def encriptar_contraseña(password):
    """
    Encripta la contraseña usando SHA256.
    """
    try:
        return sha256(password.encode()).hexdigest()
    except Exception as e:
        print(f"Error al encriptar la contraseña: {e}")
        return None

class RespuestaAPI:
    def __init__(self, exito, mensaje, datos=None):
        self.exito = exito
        self.mensaje = mensaje
        self.datos = datos or {}

    def formatear_respuesta(self):
        try:
            return {
                "exito": self.exito,
                "mensaje": self.mensaje,
                "datos": self.datos
            }
        except Exception as e:
            print(f"Error al formatear la respuesta: {e}")
            return {}

def generar_token(longitud=32):
    """
    Genera un token aleatorio de la longitud especificada.
    """
    try:
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(longitud))
    except Exception as e:
        print(f"Error al generar el token: {e}")
        return None
import math

def raiz_cuadrada(x):
    """
    Devuelve la raíz cuadrada de un número.
    """
    try:
        if x < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return math.sqrt(x)
    except Exception as e:
        print(f"Error al calcular la raíz cuadrada: {e}")
        return None

def calcular_factorial(n):
    """
    Devuelve el factorial de un número.
    """
    try:
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        return math.factorial(n)
    except Exception as e:
        print(f"Error al calcular el factorial: {e}")
        return None

def mcd(a, b):
    """
    Devuelve el máximo común divisor de dos números.
    """
    try:
        return math.gcd(a, b)
    except Exception as e:
        print(f"Error al calcular el MCD: {e}")
        return None

def calcular_potencia(base, exponente):
    """
    Devuelve la base elevada al exponente.
    """
    try:
        return math.pow(base, exponente)
    except Exception as e:
        print(f"Error al calcular la potencia: {e}")
        return None

def calcular_logaritmo(x, base=10):
    """
    Devuelve el logaritmo de x en la base especificada (por defecto base 10).
    """
    try:
        if x <= 0:
            raise ValueError("El logaritmo no está definido para números menores o iguales a cero")
        return math.log(x, base)
    except Exception as e:
        print(f"Error al calcular el logaritmo: {e}")
        return Nonedef convertir_a_mayusculas(texto):
    """
    Convierte todo el texto a mayúsculas.
    """
    try:
        return texto.upper()
    except Exception as e:
        print(f"Error al convertir el texto a mayúsculas: {e}")
        return None

def convertir_a_minusculas(texto):
    """
    Convierte todo el texto a minúsculas.
    """
    try:
        return texto.lower()
    except Exception as e:
        print(f"Error al convertir el texto a minúsculas: {e}")
        return None

def contar_palabras(texto):
    """
    Cuenta la cantidad de palabras en una cadena de texto.
    """
    try:
        palabras = texto.split()
        return len(palabras)
    except Exception as e:
        print(f"Error al contar palabras: {e}")
        return Nonedef convertir_a_entero(valor):
    """
    Convierte un valor a entero.
    """
    try:
        return int(valor)
    except Exception as e:
        print(f"Error al convertir a entero: {e}")
        return None

def convertir_a_flotante(valor):
    """
    Convierte un valor a flotante.
    """
    try:
        return float(valor)
    except Exception as e:
        print(f"Error al convertir a flotante: {e}")
        return Nonefrom datetime import datetime

def obtener_fecha_actual():
    """
    Devuelve la fecha y hora actual.
    """
    try:
        return datetime.now()
    except Exception as e:
        print(f"Error al obtener la fecha actual: {e}")
        return None

def formatear_fecha(fecha, formato="%Y-%m-%d %H:%M:%S"):
    """
    Devuelve la fecha en el formato especificado.
    """
    try:
        return fecha.strftime(formato)
    except Exception as e:
        print(f"Error al formatear la fecha: {e}")
        return Nonedef obtener_maximo(lista):
    """
    Devuelve el valor máximo de una lista.
    """
    try:
        return max(lista)
    except Exception as e:
        print(f"Error al obtener el valor máximo: {e}")
        return None

def obtener_minimo(lista):
    """
    Devuelve el valor mínimo de una lista.
    """
    try:
        return min(lista)
    except Exception as e:
        print(f"Error al obtener el valor mínimo: {e}")
        return None

def ordenar_lista(lista):
    """
    Ordena una lista de menor a mayor.
    """
    try:
        return sorted(lista)
    except Exception as e:
        print(f"Error al ordenar la lista: {e}")
        return Noneimport re

def es_email_valido(email):
    """
    Valida si el correo electrónico tiene el formato correcto.
    """
    try:
        patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(patron, email):
            return True
        return False
    except Exception as e:
        print(f"Error al validar el correo electrónico: {e}")
        return False

def es_numero_telefono_valido(telefono):
    """
    Valida si el número de teléfono tiene el formato correcto.
    """
    try:
        patron = r"^\+?1?\d{9,15}$"
        if re.match(patron, telefono):
            return True
        return False
    except Exception as e:
        print(f"Error al validar el número de teléfono: {e}")
        return Falsedef son_iguales(valor1, valor2):
    """
    Compara dos valores y devuelve True si son iguales.
    """
    try:
        return valor1 == valor2
    except Exception as e:
        print(f"Error al comparar valores: {e}")
        return False

def son_distintos(valor1, valor2):
    """
    Compara dos valores y devuelve True si son distintos.
    """
    try:
        return valor1 != valor2
    except Exception as e:
        print(f"Error al comparar valores: {e}")
        return False
from googletrans import Translator

# Función para traducir un texto
def translate_text(text, target_language='en'):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Error: {str(e)}"

# Función para detectar el idioma de un texto
def detect_language(text):
    translator = Translator()
    try:
        detected = translator.detect(text)
        return detected.lang
    except Exception as e:
        return f"Error: {str(e)}"
