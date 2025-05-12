from textblob import TextBlob

def analizar_sentimiento_textblob(texto):
    """
    Analiza el sentimiento del texto utilizando TextBlob y devuelve una clasificación.
    
    Retorna:
        - sentimiento (str): "positivo", "negativo" o "neutral"
        - polaridad (float): Valor entre -1 (negativo) y 1 (positivo)
    """
    polaridad = TextBlob(texto).sentiment.polarity

    if polaridad > 0:
        return "positivo", polaridad
    elif polaridad < 0:
        return "negativo", polaridad
    return "neutral", polaridad

def generar_recomendacion(sentimiento):
    """
    Genera una recomendación basada en el sentimiento analizado.

    Retorna:
        - recomendación (str): Mensaje de sugerencia basado en el sentimiento detectado.
    """
    recomendaciones = {
        "positivo": "¡Sigue así! Tu actitud positiva es excelente.",
        "negativo": "Parece que algo te está afectando. Intenta relajarte y buscar apoyo.",
        "neutral": "Mantén la calma, sigue reflexionando y buscando soluciones.",
    }
    return recomendaciones.get(sentimiento, "No se pudo determinar el sentimiento.")
