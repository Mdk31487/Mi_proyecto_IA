import random

class IA_Mentor:
    def __init__(self, nombre, experiencia=0):
        self.nombre = nombre
        self.experiencia = experiencia
        self.nivel = 1

    def dar_consejo(self):
        consejos = [
            "Confía en tu intuición.",
            "Cada emoción es una lección.",
            "Observa tu entorno con atención.",
            "El cambio comienza desde dentro."
        ]
        return random.choice(consejos)