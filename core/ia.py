# core/ia.py
def detectar_emocion_basica(mensaje):
    mensaje = mensaje.lower()
    if "feliz" in mensaje:
        return "feliz"
    elif "triste" in mensaje:
        return "triste"
    elif "solo" in mensaje:
        return "solo"
    else:
        return "neutral"

def generar_respuesta_ia(mensaje):
    mensaje = mensaje.lower()
    if "feliz" in mensaje:
        return "¡Me alegra saber que estás feliz!"
    elif "triste" in mensaje:
        return "Siento que estés triste. Estoy aquí para ti."
    elif "solo" in mensaje:
        return "No estás solo. Cuenta conmigo."
    else:
        return "Gracias por compartir cómo te sientes."
