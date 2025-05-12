import nltk

# Descargar los datos necesarios (esto solo se ejecuta una vez)
nltk.download('punkt')  # Tokenización de palabras y oraciones
nltk.download('stopwords')  # Palabras vacías (stopwords)
nltk.download('averaged_perceptron_tagger')  # Etiquetado gramatical

print("NLTK está listo para procesar lenguaje natural.")
