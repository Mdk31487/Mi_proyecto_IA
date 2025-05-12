from app.utils import main_utils

text = "Hola, ¿cómo estás?"
print(f"Texto original: {text}")

# Traducir al inglés
translated_text = main_utils.translate_text(text, 'en')
print(f"Texto traducido: {translated_text}")

# Detectar idioma
language = main_utils.detect_language(text)
print(f"Idioma detectado: {language}")
