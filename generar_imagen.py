import openai

# Configurar la API Key
client = openai.OpenAI(api_key="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")

def generar_imagen_de_palabra(palabra):
    prompt = f"Genera una imagen de un {palabra}"
    respuesta = client.images.generate(
        model="dall-e-3",  # Puedes cambiar a "dall-e-2" si no tienes acceso a "dall-e-3"
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    url_imagen = respuesta.data[0].url
    return url_imagen

def procesar_y_generar_imagen(pregunta):
    # Lista de palabras clave (puedes mejorar esto con procesamiento de lenguaje natural)
    palabras_clave = ['carro', 'rojo']

    imagenes = {}

    for palabra in palabras_clave:
        imagenes[palabra] = generar_imagen_de_palabra(palabra)

    return imagenes

# Ejemplo de uso
pregunta = "¿Dónde se encuentra el carro rojo?"
imagenes_generadas = procesar_y_generar_imagen(pregunta)

# Mostrar los resultados
for palabra, url in imagenes_generadas.items():
    print(f"Imagen para '{palabra}': {url}")
